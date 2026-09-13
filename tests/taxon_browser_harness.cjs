// Exercise the shipped search against records beyond the first static page.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
class Node {
  constructor() { this.children = []; this.events = {}; this.value = ""; }
  append(...items) { this.children.push(...items); }
  replaceChildren(...items) { this.children = items; }
  set textContent(value) { this.children = [String(value)]; }
  get textContent() { return this.children.map(x => typeof x === "string" ? x : x.textContent).join(""); }
  set innerHTML(_) { throw Error("Taxon source text must not become HTML"); }
  addEventListener(name, fn) { this.events[name] = fn; }
}
const nodes = new Map();
const get = id => { if (!nodes.has(id)) nodes.set(id, new Node()); return nodes.get(id); };
global.document = {getElementById: get, querySelector: get, createElement: () => new Node()};
get("taxon-browser").dataset = {root: "../", domain: "", typed: "false", page: "1", size: "200"};
const rows = Array.from({length: 451}, (_, i) => ({identifier: `NCBITaxon:${i}`, label:
  i === 450 ? "Last <script>taxon</script>" : `Taxon ${i}`, rank: "SPECIES", domain: "BACTERIA",
  sources: ["NCBITAXON"], strain_count: 1, genomes: 2, status: "SEEDED", page: `taxa/bacteria/${i}.html`}));
global.window = {TaxonMechData: {loadJSON: async () => rows}};
vm.runInThisContext(fs.readFileSync(process.argv[2], "utf8"));
setImmediate(() => {
  const body = get("#taxon-results tbody");
  assert.equal(body.children.length, 200);
  get("taxon-next").events.click();
  assert.equal(body.children.length, 200);
  get("taxon-next").events.click();
  assert.equal(body.children.length, 51);
  assert.equal(get("taxon-next").disabled, true);
  get("taxon-query").value = "LAST <script>";
  get("taxon-query").events.input();
  assert.equal(body.children.length, 1);
  assert(body.textContent.includes("Last <script>taxon</script>"));
  assert.equal(body.children[0].children[0].children[0].href, "../taxa/bacteria/450.html");
  get("taxon-query").value = "NCBITaxon:99999";
  get("taxon-query").events.input();
  assert.equal(body.children.length, 0);
  assert.equal(get("taxon-next").disabled, true);
  assert.equal(get("taxon-prev").disabled, true);
  console.log("Complete-corpus search and bounded pagination passed");
});
