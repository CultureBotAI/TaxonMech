/* Complete taxon records in lossless, bounded shards; strain tables page locally. */
(() => {
  "use strict";
  const container = document.getElementById("taxon-record");
  const identifier = new URLSearchParams(window.location.search).get("id") || "";
  const match = /^NCBITaxon:([1-9][0-9]*)$/.exec(identifier);
  function install(target, html, fallbackLabel = "Taxon record") {
    const template = document.createElement("template");
    template.innerHTML = html; // Generated through the same autoescaping templates as static pages.
    let label = fallbackLabel;
    for (const element of template.content.querySelectorAll("h2, h3, table")) {
      if (element.tagName !== "TABLE") {
        label = element.textContent.trim() || fallbackLabel;
        continue;
      }
      const region = document.createElement("div");
      region.className = "table-scroll";
      region.setAttribute("role", "region");
      region.setAttribute("aria-label", element.caption?.textContent.trim() || label);
      region.setAttribute("tabindex", "0");
      element.before(region);
      region.appendChild(element);
    }
    target.replaceChildren(template.content);
  }
  async function run() {
    if (!match || !Number.isSafeInteger(Number(match[1]))) {
      const error = new Error("Select a valid NCBI taxon from Browse.");
      error.outsideScope = true;
      throw error;
    }
    const bucket = String(Math.floor(Number(match[1]) / 1000)).padStart(4, "0");
    let shard;
    try {
      shard = await window.TaxonMechData.loadJSON("taxon-details/" + bucket + ".json.gz");
    } catch (error) {
      if (error.status === 404) {
        // A missing published file can be a deployment failure. Only the
        // publication inventory can establish that this bucket is out of scope.
        try {
          const inventory = await window.TaxonMechData.loadJSON("taxon-details/index.json");
          if (Array.isArray(inventory.buckets) && !inventory.buckets.includes(bucket)) {
            error.outsideScope = true;
            error.message = "This taxon is not in the published scope. Choose a record from Browse.";
          }
        } catch (_) { /* An unreadable inventory does not prove record absence. */ }
      }
      throw error;
    }
    const record = shard[identifier];
    if (!record) {
      const error = new Error("This taxon is not in the published scope. Choose a record from Browse.");
      error.outsideScope = true;
      throw error;
    }
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
      install(table, pages[number].html, "Strains");
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
  async function start() {
    container.removeAttribute("role");
    container.setAttribute("aria-busy", "true");
    try {
      await run();
    } catch (error) {
      const message = document.createElement("p");
      message.textContent = error.outsideScope ? error.message :
        "Could not load this taxon record. The data may be temporarily unavailable. Try again or use Browse.";
      const browse = document.createElement("a");
      browse.href = "browse.html";
      browse.textContent = "Browse taxon records";
      container.replaceChildren(message, browse);
      if (!error.outsideScope) {
        const retry = document.createElement("button");
        retry.type = "button";
        retry.textContent = "Try again";
        retry.addEventListener("click", start);
        container.appendChild(retry);
      }
      container.setAttribute("role", "alert");
    } finally {
      container.setAttribute("aria-busy", "false");
    }
  }
  start();
})();
