/* Search the complete corpus while keeping the displayed table bounded. */
(() => {
  "use strict";
  const browser = document.getElementById("taxon-browser");
  if (!browser) return;
  const root = browser.dataset.root;
  const pageSize = Number(browser.dataset.size);
  const query = document.getElementById("taxon-query");
  const tbody = document.querySelector("#taxon-results tbody");
  const status = document.getElementById("taxon-status");
  const previous = document.getElementById("taxon-prev");
  const next = document.getElementById("taxon-next");
  let rows = [], filtered = [], page = Number(browser.dataset.page) - 1;
  const element = (tag, text) => {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = String(text);
    return node;
  };
  function render() {
    page = Math.max(0, Math.min(page, Math.ceil(filtered.length / pageSize) - 1));
    tbody.replaceChildren();
    for (const row of filtered.slice(page * pageSize, (page + 1) * pageSize)) {
      const tr = element("tr"), name = element("td"), link = element("a");
      link.href = root + row.page;
      link.append(element("em", row.label));
      name.append(link);
      tr.append(name);
      for (const value of [row.identifier, row.rank, row.domain, row.sources.length,
        row.strain_count, row.genomes, row.status]) tr.append(element("td", value ?? ""));
      tbody.append(tr);
    }
    status.textContent = filtered.length + " of " + rows.length + " records match · page " +
      (page + 1) + " of " + Math.max(1, Math.ceil(filtered.length / pageSize)) + ".";
    previous.disabled = page === 0;
    next.disabled = (page + 1) * pageSize >= filtered.length;
  }
  function search() {
    const term = query.value.toLowerCase().trim();
    filtered = rows.filter(row => row.searchText.includes(term));
    page = 0;
    render();
  }
  window.TaxonMechData.loadJSON(root + "index.json.gz").catch(() =>
    window.TaxonMechData.loadJSON(root + "index.json")
  ).then(data => {
    rows = data.filter(row => (!browser.dataset.domain || row.domain === browser.dataset.domain) &&
      (browser.dataset.typed !== "true" || row.has_type_strain)).map(row => ({...row,
      searchText: [row.identifier, row.label, row.rank, row.domain, ...row.sources].join(" ").toLowerCase()}));
    filtered = rows;
    document.getElementById("taxon-search").hidden = false;
    document.getElementById("taxon-static-pages").hidden = true;
    document.getElementById("taxon-dynamic-pages").hidden = false;
    query.addEventListener("input", search);
    document.getElementById("taxon-search").addEventListener("submit", event => {
      event.preventDefault(); search();
    });
    previous.addEventListener("click", () => { page--; render(); });
    next.addEventListener("click", () => { page++; render(); });
    render();
  }).catch(() => {
    status.append(" Search is unavailable; use the page links to browse all records.");
  });
})();
