// Run the shipped browser with its actual DOM operations and lazy detail files.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const path = require("node:path");
class Node {
  constructor(tag = "div") { this.tag = tag; this.children = []; this.events = {}; this.value = ""; }
  append(...items) { this.children.push(...items); }
  replaceChildren(...items) { this.children = items; }
  set textContent(value) { this.children = [String(value)]; }
  get textContent() { return this.children.map(x => typeof x === "string" ? x : x.textContent).join(""); }
  set innerHTML(_) { throw new Error("Source metadata must not become HTML"); }
  addEventListener(name, fn) { this.events[name] = fn; }
}
const nodes = new Map();
const get = id => { if (!nodes.has(id)) nodes.set(id, new Node()); return nodes.get(id); };
global.document = {getElementById: get, querySelector: get, createElement: tag => new Node(tag)};
const events = {};
global.window = {location: {href: "https://example.org/TaxonMech/pages/straininfo.html", hash: ""},
  addEventListener: (name, fn) => { events[name] = fn; }};
const compression = process.argv[4];
if (compression !== "json") window.DecompressionStream = global.DecompressionStream;
const data = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
const fetched = [];
global.fetch = async url => {
  fetched.push(url);
  if (url.endsWith(".gz")) return new Response(compression === "broken_gzip" ? "corrupt" :
    fs.readFileSync(path.join(path.dirname(process.argv[3]), url)));
  if (url === "straininfo-index.json") return {ok: true, json: async () => data};
  const batch = JSON.parse(fs.readFileSync(path.join(path.dirname(process.argv[3]), url), "utf8"));
  batch[1].url = "javascript:alert('unsafe')";
  return {ok: true, json: async () => batch};
};
vm.runInThisContext(fs.readFileSync(process.argv[2], "utf8"));
function descendants(node) { return [node, ...node.children.filter(x => x instanceof Node).flatMap(descendants)]; }
function search(value) { get("straininfo-query").value = value; get("straininfo-query").events.input(); }
const settled = () => new Promise(resolve => setImmediate(resolve));
setImmediate(async () => {
  for (let tries = 0; tries < 200 && get("#straininfo-results tbody").children.length !== 2; tries++) {
    await new Promise(resolve => setTimeout(resolve, 5));
  }
  assert.equal(get("#straininfo-results tbody").children.length, 2);
  for (const query of ["SI-ID1", "SI-DP11", "straininfo.deposit:12", "DSM 1", "bacdive:1",
    "kgmicrobe.strain:DSM-1", "10.60712/SI-ID1.3", "GCA_000000001", "X12345"]) {
    search(query);
    assert.equal(get("#straininfo-results tbody").children.length, 1, query);
  }
  for (const query of ["GCA_000000009", "GCA_000000001.1", "no such deposit"]) {
    search(query);
    assert.equal(get("#straininfo-results tbody").children.length, 0, query);
  }
  search("");
  window.location.hash = "#straininfo.strain:1";
  events.hashchange();
  await settled();
  const detail = get("straininfo-detail");
  assert.match(detail.textContent, /Record-version DOI/);
  assert.match(detail.textContent, /Original <sequence>/);
  assert.match(detail.textContent, /Existing TaxonMech strain associations/);
  assert.match(detail.textContent, /Their presence here does not establish a StrainInfo deposit assertion/);
  assert(!detail.textContent.includes("StrainInfo does not assert these associations"));
  const anchors = descendants(detail).filter(x => x.tag === "a");
  assert(anchors.some(x => x.href === "https://straininfo.dsmz.de/strain/1?SI-DP11"));
  assert(anchors.some(x => x.href === "https://doi.org/10.60712/SI-ID1.3"));
  assert(anchors.some(x => x.href === "https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000000001"));
  const sections = detail.children.filter(x => x instanceof Node && x.tag === "section");
  assert(!sections[0].textContent.includes("GCA_000000002"));
  assert(!sections[1].textContent.includes("GCA_000000001"));
  assert(sections[2].textContent.includes("GCA_000000001"), "An identifier can have both source assertions");
  window.location.hash = "#SI-ID3";
  events.hashchange();
  await settled();
  assert.match(detail.textContent, /Not listed on a taxon page/);
  assert(!descendants(detail).some(x => x.href && x.href.startsWith("javascript:")));
  const indexRequests = compression === "json" ? ["straininfo-index.json"] :
    compression === "gzip" ? ["straininfo-index.json.gz"] : ["straininfo-index.json.gz", "straininfo-index.json"];
  assert.deepEqual(fetched, [...indexRequests, "straininfo-details/0000.json"]);
  window.location.hash = "#straininfo.strain:999";
  events.hashchange();
  assert.match(detail.textContent, /not in the linked snapshot browser/);
  console.log("StrainInfo search, native links, URL safety and deposit boundaries passed");
});
