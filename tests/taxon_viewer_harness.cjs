const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const script = fs.readFileSync(process.argv[2], "utf8");

async function exercise(search, shard) {
  const nodes = new Map(), events = {}, calls = [];
  function node(id) {
    if (!nodes.has(id)) nodes.set(id, {
      events: {}, attributes: {}, textContent: "", rendered: "", disabled: false,
      replaceChildren(content) { this.rendered = content.html; },
      addEventListener(name, fn) { this.events[name] = fn; },
      setAttribute(name, value) { this.attributes[name] = value; },
      scrollIntoView() { this.scrolled = true; }
    });
    return nodes.get(id);
  }
  const document = {
    getElementById: node,
    createElement(tag) {
      assert.equal(tag, "template");
      return {content: {}, set innerHTML(value) { this.content.html = value; }};
    }
  };
  const window = {
    location: {search, hash: "#strains-last"},
    addEventListener(name, fn) { events[name] = fn; },
    TaxonMechData: {loadJSON: async path => {calls.push(path); return shard;}}
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
  const absent = await exercise("?id=NCBITaxon:1234", {});
  assert.deepEqual(absent.calls, ["taxon-details/0001.json.gz"]);
  assert.equal(absent.node("taxon-record").attributes.role, "alert");
  console.log("Shared taxon viewer, complete strain pages and incoming anchors passed");
})().catch(error => { console.error(error); process.exitCode = 1; });
