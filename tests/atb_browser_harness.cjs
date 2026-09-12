// Exercise the shipped browser script with the DOM operations it uses.
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
  set innerHTML(_) { throw new Error("Source metadata must not be interpreted as HTML"); }
  addEventListener(name, fn) { this.events[name] = fn; }
}
const nodes = new Map();
const get = id => { if (!nodes.has(id)) nodes.set(id, new Node()); return nodes.get(id); };
global.document = {getElementById: get, querySelector: get, createElement: tag => new Node(tag)};
const events = {};
global.window = {location: {href: "https://example.org/TaxonMech/atb.html", hash: ""},
  addEventListener: (name, fn) => { events[name] = fn; }};
const data = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
const fetched = [];
global.fetch = async url => {
  fetched.push(url);
  if (url === "atb-index.json") return {ok: true, json: async () => data};
  const batch = JSON.parse(fs.readFileSync(path.join(path.dirname(process.argv[3]), url), "utf8"));
  batch[1].metadata.aws_url = "javascript:alert('unsafe download')";
  return {ok: true, json: async () => batch};
};
vm.runInThisContext(fs.readFileSync(process.argv[2], "utf8"));
function descendants(node) { return [node, ...node.children.filter(x => x instanceof Node).flatMap(descendants)]; }
function search(value) { get("atb-query").value = value; get("atb-query").events.input(); }
const settled = () => new Promise(resolve => setImmediate(resolve));
setImmediate(async () => {
  assert.equal(get("#atb-results tbody").children.length, 2);
  assert.match(get("atb-status").textContent, /^2 of 2/);
  for (const query of ["GCA_000000001.2", "ERZ1", "DSM-2", "bacdive:2", "SAMN2", "atb.assembly:202505.SAMN1"]) {
    search(query);
    assert.equal(get("#atb-results tbody").children.length, 1, query);
  }
  search("missing accession");
  assert.equal(get("#atb-results tbody").children.length, 0);
  assert.equal(get("atb-page").textContent, "No results");
  search("");
  window.location.hash = "#atb.assembly:202505.SAMN2";
  events.hashchange();
  await settled();
  let detail = get("atb-detail");
  assert.match(detail.textContent, /Not listed on a taxon page/);
  assert.match(detail.textContent, /No genome crosslink with a matching source chain/);
  let anchors = descendants(detail).filter(x => x.tag === "a");
  assert(anchors.some(x => x.href === "https://bacdive.dsmz.de/strain/2"));
  assert(!anchors.some(x => x.href && /javascript:|ena\/browser/.test(x.href)));
  window.location.hash = "#atb.assembly:202505.SAMN1";
  events.hashchange();
  await settled();
  detail = get("atb-detail");
  anchors = descendants(detail).filter(x => x.tag === "a");
  assert(anchors.some(x => x.href === "https://example.org/1.fa.gz"));
  assert(anchors.some(x => x.href === "https://www.ebi.ac.uk/ena/browser/view/ERZ1"));
  assert.match(detail.textContent, /PROJECT NCBI BIOSAMPLE ID/);
  assert.match(detail.textContent, /DSM 1 <original>/);
  assert.match(detail.textContent, /shares_biosample/);
  assert(detail.textContent.indexOf("ncbi.assembly:GCA_") < detail.textContent.indexOf("img.taxon:1"));
  assert.deepEqual(fetched, ["atb-index.json", "atb-details/0000.json"], "Details are lazy and cached");
  window.location.hash = "#atb.assembly:202505.SAMN3";
  events.hashchange();
  assert.match(get("atb-detail").textContent, /not in the linked snapshot browser/);
  console.log("Browser search, deep links, source evidence and URL safety passed");
});
