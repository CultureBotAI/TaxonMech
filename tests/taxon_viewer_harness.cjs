const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const script = fs.readFileSync(process.argv[2], "utf8");

// A small DOM surface for the real viewer script, including node reparenting.
// Keep each complete table string immutable so wrapping cannot discard evidence.
class Element {
  constructor(tagName, textContent = "", outerHTML = "") {
    this.tagName = tagName; this.textContent = textContent; this.outerHTML = outerHTML;
    this.children = []; this.parentNode = null; this.attributes = {}; this.events = {};
  }
  setAttribute(name, value) { this.attributes[name] = value; }
  removeAttribute(name) { delete this.attributes[name]; }
  appendChild(child) {
    if (child.parentNode) child.parentNode.children.splice(child.parentNode.children.indexOf(child), 1);
    this.children.push(child); child.parentNode = this;
  }
  before(other) {
    const parent = this.parentNode;
    parent.children.splice(parent.children.indexOf(this), 0, other); other.parentNode = parent;
  }
  querySelectorAll(selector) {
    const tags = selector.split(",").map(tag => tag.trim().toUpperCase()), result = [];
    function visit(parent) {
      for (const child of parent.children) {
        if (tags.includes(child.tagName)) result.push(child);
        visit(child);
      }
    }
    visit(this); return result;
  }
  replaceChildren(...contents) {
    this.rendered = contents[0]?.html; this.children = [];
    for (const content of contents) {
      for (const child of content.tagName === "FRAGMENT" ? [...content.children] : [content]) {
        this.appendChild(child);
      }
    }
  }
  addEventListener(name, fn) { this.events[name] = fn; }
  scrollIntoView() { this.scrolled = true; }
}

function fragment(html) {
  const root = new Element("FRAGMENT"); root.html = html;
  const text = value => value.replace(/<[^>]*>/g, "").replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">").replace(/&amp;/g, "&");
  for (const match of html.matchAll(/<(h2|h3|table)\b[^>]*>([\s\S]*?)<\/\1>/gi)) {
    const node = new Element(match[1].toUpperCase(), text(match[2]), match[0]);
    const caption = /<caption\b[^>]*>([\s\S]*?)<\/caption>/i.exec(match[0]);
    if (caption) node.caption = {textContent: text(caption[1])};
    root.appendChild(node);
  }
  return root;
}

async function exercise(search, shard) {
  const nodes = new Map(), events = {}, calls = [];
  function node(id) {
    if (!nodes.has(id)) nodes.set(id, new Element("DIV"));
    return nodes.get(id);
  }
  const document = {
    getElementById: node,
    createElement(tag) {
      if (tag === "template") return {set innerHTML(value) { this.content = fragment(value); }};
      return new Element(tag.toUpperCase());
    }
  };
  const window = {
    location: {search, hash: "#strains-last"},
    addEventListener(name, fn) { events[name] = fn; },
    TaxonMechData: {loadJSON: async path => {
      calls.push(path); return typeof shard === "function" ? shard(path, calls.length) : shard;
    }}
  };
  vm.runInNewContext(script, {document, window, URLSearchParams});
  await new Promise(resolve => setImmediate(resolve));
  return {node, document, window, events, calls};
}

(async () => {
  const state = await exercise("?id=NCBITaxon:562", {"NCBITaxon:562": {
    label: "Source <name>", html: "complete taxon body", strain_pages: [
      {html: "first 200 strains", anchors: ["strains-first"]},
      {html: "last strain and its genome evidence", anchors: ["strains-last"]}
    ]
  }});
  assert.deepEqual(state.calls, ["taxon-details/0000.json.gz"]);
  assert.equal(state.document.title, "Source <name> · TaxonMech");
  assert.equal(state.node("taxon-strain-table").rendered, "last strain and its genome evidence");
  assert.equal(state.node("strain-page-next").disabled, true);
  assert.equal(state.node("strains-last").scrolled, true);
  state.node("strain-page-previous").events.click();
  assert.equal(state.node("taxon-strain-table").rendered, "first 200 strains");
  assert.equal(state.node("strain-page-previous").disabled, true);
  state.events.hashchange();
  assert.equal(state.node("taxon-strain-table").rendered, "last strain and its genome evidence");
  for (const query of ["?id=NCBITaxon:0", "?id=NCBITaxon:9007199254740992", "?id=<script>"]) {
    const invalid = await exercise(query, {});
    assert.equal(invalid.calls.length, 0);
    assert.equal(invalid.node("taxon-record").attributes.role, "alert");
  }
  const absent = await exercise("?id=NCBITaxon:1234", {
    "NCBITaxon:1235": {label: "Other published taxon", html: "Other complete record"}
  });
  assert.deepEqual(absent.calls, ["taxon-details/0001.json.gz"]);
  assert.equal(absent.node("taxon-record").attributes.role, "alert");
  assert.match(absent.node("taxon-record").children[0].textContent, /not in the published scope/);
  assert.equal(absent.node("taxon-record").querySelectorAll("button").length, 0);
  for (const inventory of [{buckets: []}, {buckets: ["0001"]}, null]) {
    const missing = await exercise("?id=NCBITaxon:1234", async path => {
      if (path.endsWith("index.json") && inventory) return inventory;
      throw Object.assign(new Error("HTTP 404: raw transport detail"), {status: 404});
    });
    const container = missing.node("taxon-record");
    assert.equal(container.querySelectorAll("a")[0].href, "browse.html");
    const outside = inventory && inventory.buckets.length === 0;
    assert.match(container.children[0].textContent, outside ? /not in the published scope/ : /temporarily unavailable/);
    assert.equal(container.querySelectorAll("button").length, outside ? 0 : 1);
    assert.doesNotMatch(container.children[0].textContent, /HTTP 404|raw transport/);
  }
  const retry = await exercise("?id=NCBITaxon:562", async (path, count) => {
    if (count === 1) throw new Error("network error");
    return {"NCBITaxon:562": {label: "Recovered", html: "complete recovered record"}};
  });
  await retry.node("taxon-record").querySelectorAll("button")[0].events.click();
  assert.equal(retry.node("taxon-record").rendered, "complete recovered record");
  assert.equal(retry.node("taxon-record").attributes.role, undefined);
  assert.equal(retry.node("taxon-record").attributes["aria-busy"], "false");

  for (const invalid of [null, {}, [], "unavailable", {error: "unavailable"},
      {"NCBITaxon:777": null}, {"NCBITaxon:562": null},
      {"NCBITaxon:1562": {label: "Wrong bucket", html: "body"}},
      {"NCBITaxon:9007199254740992": {label: "Unsafe integer", html: "body"}},
      {"NCBITaxon:0562": {label: "Noncanonical identifier", html: "body"}},
      {"NCBITaxon:562": {label: "Missing HTML"}},
      {"NCBITaxon:562": {label: "", html: ""}},
      {"NCBITaxon:562": {label: "Valid label", html: "  \n "}},
      {"NCBITaxon:562": {label: "Valid label", html: "body",
        strain_pages: [{html: " ", anchors: []}] }},
      {"NCBITaxon:562": {label: "Bad strain pages", html: "body", strain_pages: {}}},
      {"NCBITaxon:562": {label: "Bad anchors", html: "body",
        strain_pages: [{html: "strains", anchors: [7]}]}}]) {
    const corrupt = await exercise("?id=NCBITaxon:562", async (path, count) => {
      if (count === 1) return invalid;
      return {"NCBITaxon:562": {label: "Recovered", html: "complete recovered record"}};
    });
    const container = corrupt.node("taxon-record");
    assert.equal(container.attributes.role, "alert");
    assert.match(container.children[0].textContent, /temporarily unavailable/);
    assert.equal(container.querySelectorAll("button").length, 1);
    await container.querySelectorAll("button")[0].events.click();
    assert.equal(corrupt.calls.length, 2, "Retry must fetch fresh data");
    assert.equal(container.rendered, "complete recovered record");
    assert.equal(container.attributes.role, undefined);
  }

  for (const inventory of [null, [], "unavailable", {buckets: null},
      {buckets: [1234]}, {buckets: ["not-a-bucket"]}, {buckets: ["1"]},
      {buckets: ["00001"]}, {buckets: ["9007199254740992"]}]) {
    let attempt = 0;
    const corrupt = await exercise("?id=NCBITaxon:562", async path => {
      if (path.endsWith("index.json")) return inventory;
      if (++attempt === 1) throw Object.assign(new Error("missing deployment file"), {status: 404});
      return {"NCBITaxon:562": {label: "Recovered", html: "complete recovered record"}};
    });
    const container = corrupt.node("taxon-record");
    assert.match(container.children[0].textContent, /temporarily unavailable/);
    assert.equal(container.querySelectorAll("button").length, 1);
    await container.querySelectorAll("button")[0].events.click();
    assert.equal(container.rendered, "complete recovered record");
  }
  for (const buckets of [[], ["0001"], ["10000"]]) {
    const outside = await exercise("?id=NCBITaxon:562", async path => {
      if (path.endsWith("index.json")) return {buckets};
      throw Object.assign(new Error("missing bucket"), {status: 404});
    });
    assert.match(outside.node("taxon-record").children[0].textContent, /not in the published scope/);
    assert.equal(outside.node("taxon-record").querySelectorAll("button").length, 0);
  }

  let completeRetry;
  const concurrent = await exercise("?id=NCBITaxon:562", async (path, count) => {
    if (count === 1) throw new Error("Initial failure");
    return new Promise(resolve => { completeRetry = resolve; });
  });
  const oldRetry = concurrent.node("taxon-record").querySelectorAll("button")[0];
  const firstRetry = oldRetry.events.click();
  const secondRetry = oldRetry.events.click();
  assert.equal(oldRetry.disabled, true);
  assert.equal(concurrent.calls.length, 2, "Repeated Retry must not start another request");
  completeRetry({"NCBITaxon:562": {label: "Recovered", html: "Latest complete record"}});
  await Promise.all([firstRetry, secondRetry]);
  assert.equal(concurrent.node("taxon-record").rendered, "Latest complete record");
  assert.equal(concurrent.node("taxon-record").attributes.role, undefined);

  const failsAgain = await exercise("?id=NCBITaxon:562", async () => { throw new Error("offline"); });
  await failsAgain.node("taxon-record").querySelectorAll("button")[0].events.click();
  const availableRetry = failsAgain.node("taxon-record").querySelectorAll("button")[0];
  assert.ok(!availableRetry.disabled, "A completed failed retry must offer an enabled new Retry");
  assert.equal(failsAgain.node("taxon-record").attributes["aria-busy"], "false");

  const table = id => '<table><thead><tr><th>Scientific evidence</th></tr></thead>' +
    '<tbody><tr id="' + id + '"><td><a href="https://pubmed.ncbi.nlm.nih.gov/123/">' +
    'PMID:123 &amp; exact source quotation</a></td></tr></tbody></table>';
  const recordTables = [table("source"), table("mapping"), table("graph")];
  const recordHtml = '<h2>Source &lt;literal&gt; attestations</h2>' + recordTables[0] +
    '<h2>Taxonomy mappings</h2>' + recordTables[1] +
    '<h2>Causal graphs</h2><h3>Declared graph title</h3>' + recordTables[2];
  const strainTables = [table("strains-first"), table("strains-last")];
  const payload = {"NCBITaxon:562": {label: "Record", html: recordHtml, strain_pages: [
    {html: strainTables[0], anchors: ["strains-first"]},
    {html: strainTables[1], anchors: ["strains-last"]}
  ]}};
  const unchanged = JSON.stringify(payload);
  const wrapped = await exercise("?id=NCBITaxon:562", payload);
  function assertRegions(target, names, originals) {
    const tables = target.querySelectorAll("table");
    assert.equal(tables.length, originals.length);
    for (const [index, item] of tables.entries()) {
      assert.equal(item.outerHTML, originals[index], "Original scientific table and links changed");
      const region = item.parentNode;
      assert.equal(region.className, "table-scroll", "Loaded table must have its own scroll region");
      assert.equal(region.attributes.role, "region");
      assert.equal(region.attributes.tabindex, "0");
      assert.equal(region.attributes["aria-label"], names[index]);
      assert.deepEqual(region.children, [item]);
    }
  }
  assertRegions(wrapped.node("taxon-record"),
    ["Source <literal> attestations", "Taxonomy mappings", "Declared graph title"], recordTables);
  assertRegions(wrapped.node("taxon-strain-table"), ["Strains"], [strainTables[1]]);
  assert.equal(wrapped.node("strains-last").scrolled, true);
  wrapped.node("strain-page-previous").events.click();
  assertRegions(wrapped.node("taxon-strain-table"), ["Strains"], [strainTables[0]]);
  wrapped.node("strain-page-next").events.click();
  assertRegions(wrapped.node("taxon-strain-table"), ["Strains"], [strainTables[1]]);
  wrapped.node("strain-page-previous").events.click(); wrapped.events.hashchange();
  assertRegions(wrapped.node("taxon-strain-table"), ["Strains"], [strainTables[1]]);
  assert.equal(JSON.stringify(payload), unchanged, "Stored corpus payload changed");
  const captioned = table("captioned").replace("<table>", "<table><caption>Explicit table name</caption>");
  const captionState = await exercise("?id=NCBITaxon:562", {"NCBITaxon:562": {
    label: "Record", html: "<h2>Section name</h2>" + captioned + table("fallback"), strain_pages: []
  }});
  assertRegions(captionState.node("taxon-record"), ["Explicit table name", "Section name"],
    [captioned, table("fallback")]);
  console.log("Shared taxon viewer, complete strain pages and incoming anchors passed");
})().catch(error => { console.error(error); process.exitCode = 1; });
