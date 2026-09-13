/* Complete taxon records in lossless, bounded shards; strain tables page locally. */
(() => {
  "use strict";
  const container = document.getElementById("taxon-record");
  const identifier = new URLSearchParams(window.location.search).get("id") || "";
  const match = /^NCBITaxon:([1-9][0-9]*)$/.exec(identifier);
  function install(target, html) {
    const template = document.createElement("template");
    template.innerHTML = html; // Generated through the same autoescaping templates as static pages.
    target.replaceChildren(template.content);
  }
  async function run() {
    if (!match || !Number.isSafeInteger(Number(match[1]))) throw new Error("Select a valid NCBI taxon from Browse.");
    const bucket = String(Math.floor(Number(match[1]) / 1000)).padStart(4, "0");
    const shard = await window.TaxonMechData.loadJSON("taxon-details/" + bucket + ".json.gz");
    const record = shard[identifier];
    if (!record) throw new Error("This taxon is not in the published scope. Choose a record from Browse.");
    document.title = record.label + " · TaxonMech";
    install(container, record.html);
    const pages = record.strain_pages || [];
    let current = 0;
    const table = document.getElementById("taxon-strain-table");
    const status = document.getElementById("strain-page-status");
    const previous = document.getElementById("strain-page-previous");
    const next = document.getElementById("strain-page-next");
    function show(number) {
      if (!pages.length || number < 0 || number >= pages.length) return;
      current = number;
      install(table, pages[number].html);
      status.textContent = "Strain page " + (number + 1) + " of " + pages.length;
      previous.disabled = number === 0;
      next.disabled = number === pages.length - 1;
    }
    function followAnchor() {
      let anchor = window.location.hash.slice(1);
      try { anchor = decodeURIComponent(anchor); } catch (_) { /* Preserve literal malformed escapes. */ }
      const page = pages.findIndex(item => item.anchors.includes(anchor));
      if (page >= 0 && page !== current) show(page);
      if (anchor) document.getElementById(anchor)?.scrollIntoView();
    }
    if (pages.length) {
      previous.addEventListener("click", () => show(current - 1));
      next.addEventListener("click", () => show(current + 1));
      show(0);
    }
    window.addEventListener("hashchange", followAnchor);
    followAnchor();
  }
  run().catch(error => {
    container.textContent = error.message || "Could not load this record. Reload the page or use Browse.";
    container.setAttribute("role", "alert");
  });
})();
