/* Search and facet-filter the complete corpus while keeping the displayed table bounded. */
(() => {
  "use strict";
  const browser = document.getElementById("taxon-browser");
  if (!browser) return;
  const root = browser.dataset.root;
  const pageSize = Number(browser.dataset.size);
  const query = document.getElementById("taxon-query");
  const domainFilter = document.getElementById("taxon-domain-filter");
  const rankFilter = document.getElementById("taxon-rank-filter");
  const sourceFilter = document.getElementById("taxon-source-filter");
  const typeFilter = document.getElementById("taxon-type-filter");
  const statusFilter = document.getElementById("taxon-status-filter");
  const sortSelect = document.getElementById("taxon-sort");
  const resetBtn = document.getElementById("taxon-reset");
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
  function syncUrl(term) {
    if (!window.history || typeof window.history.replaceState !== "function" ||
        !window.location || typeof window.location.pathname !== "string") return;
    const params = new URLSearchParams(window.location.search || "");
    if (term) params.set("q", term);
    else params.delete("q");
    const sortVal = sortSelect ? (sortSelect.value || "") : "";
    if (sortVal) params.set("sort", sortVal);
    else params.delete("sort");
    const qs = params.toString();
    window.history.replaceState(null, "", window.location.pathname + (qs ? "?" + qs : "") + (window.location.hash || ""));
  }
  function render() {
    page = Math.max(0, Math.min(page, Math.ceil(filtered.length / pageSize) - 1));
    tbody.replaceChildren();
    for (const row of filtered.slice(page * pageSize, (page + 1) * pageSize)) {
      const tr = element("tr"), name = element("td"), link = element("a");
      link.href = root + row.page;
      link.append(element("em", row.label));
      name.append(link);
      tr.append(name);
      const mappings = (row.gtdb_mapping_count || 0) +
        (row.gtdb_pooled_mapping_count ? " (" + row.gtdb_pooled_mapping_count + " pooled)" : "");
      for (const value of [row.identifier, row.rank, row.domain, row.sources.length,
        row.strain_count, mappings, row.status]) tr.append(element("td", value ?? ""));
      tbody.append(tr);
    }
    status.textContent = filtered.length + " of " + rows.length + " records match · page " +
      (page + 1) + " of " + Math.max(1, Math.ceil(filtered.length / pageSize)) + ".";
    previous.disabled = page === 0;
    next.disabled = (page + 1) * pageSize >= filtered.length;
  }
  function search() {
    const term = (query.value || "").toLowerCase().trim();
    const domVal = domainFilter ? (domainFilter.value || "") : "";
    const rankVal = rankFilter ? (rankFilter.value || "") : "";
    const srcVal = sourceFilter ? (sourceFilter.value || "") : "";
    const typeVal = typeFilter ? (typeFilter.value || "") : "";
    const statusVal = statusFilter ? (statusFilter.value || "") : "";
    const sortVal = sortSelect ? (sortSelect.value || "") : "";
    filtered = rows.filter(row => {
      if (term && !row.searchText.includes(term)) return false;
      if (domVal && row.domain !== domVal) return false;
      if (rankVal && (row.rank || "NO_RANK") !== rankVal) return false;
      if (srcVal && !(row.sources || []).includes(srcVal)) return false;
      if (typeVal === "typed" && !row.has_type_strain) return false;
      if (typeVal === "strains" && !(row.strain_count > 0)) return false;
      if (typeVal === "gtdb" && !(row.gtdb_mapping_count > 0)) return false;
      if (statusVal && row.status !== statusVal) return false;
      return true;
    });
    if (sortVal) {
      filtered = filtered.slice().sort((a, b) => {
        if (sortVal === "label_asc") return String(a.label || "").localeCompare(String(b.label || ""));
        if (sortVal === "label_desc") return String(b.label || "").localeCompare(String(a.label || ""));
        if (sortVal === "id_asc") {
          const na = Number(String(a.identifier || "").split(":")[1]) || 0;
          const nb = Number(String(b.identifier || "").split(":")[1]) || 0;
          return na - nb;
        }
        if (sortVal === "rank_asc") return String(a.rank || "ZZZ").localeCompare(String(b.rank || "ZZZ")) || String(a.label || "").localeCompare(String(b.label || ""));
        if (sortVal === "strains_desc") return ((b.strain_count || 0) - (a.strain_count || 0)) || String(a.label || "").localeCompare(String(b.label || ""));
        if (sortVal === "gtdb_desc") return ((b.gtdb_mapping_count || 0) - (a.gtdb_mapping_count || 0)) || String(a.label || "").localeCompare(String(b.label || ""));
        if (sortVal === "sources_desc") return (((b.sources || []).length) - ((a.sources || []).length)) || String(a.label || "").localeCompare(String(b.label || ""));
        return 0;
      });
    }
    page = 0;
    syncUrl(query.value ? query.value.trim() : "");
    render();
  }
  if (window.location && typeof window.location.search === "string" && typeof URLSearchParams !== "undefined") {
    const params = new URLSearchParams(window.location.search);
    const initialQ = params.get("q") || "";
    if (initialQ && !query.value) query.value = initialQ;
    const initialSort = params.get("sort") || "";
    if (initialSort && sortSelect && !sortSelect.value) sortSelect.value = initialSort;
  }
  window.TaxonMechData.loadJSON(root + "index.json.gz").then(data => {
    rows = data.filter(row => (!browser.dataset.domain || row.domain === browser.dataset.domain) &&
      (browser.dataset.typed !== "true" || row.has_type_strain)).map(row => ({...row,
      searchText: [row.identifier, row.label, row.rank, row.domain, ...(row.sources || [])].join(" ").toLowerCase()}));
    filtered = rows;
    document.getElementById("taxon-search").hidden = false;
    document.getElementById("taxon-static-pages").hidden = true;
    document.getElementById("taxon-dynamic-pages").hidden = false;
    query.addEventListener("input", search);
    for (const control of [domainFilter, rankFilter, sourceFilter, typeFilter, statusFilter, sortSelect]) {
      if (control && typeof control.addEventListener === "function") {
        control.addEventListener("change", search);
      }
    }
    if (resetBtn && typeof resetBtn.addEventListener === "function") {
      resetBtn.addEventListener("click", () => {
        query.value = "";
        if (domainFilter) domainFilter.value = browser.dataset.domain || "";
        if (rankFilter) rankFilter.value = "";
        if (sourceFilter) sourceFilter.value = "";
        if (typeFilter) typeFilter.value = browser.dataset.typed === "true" ? "typed" : "";
        if (statusFilter) statusFilter.value = "";
        if (sortSelect) sortSelect.value = "";
        search();
      });
    }
    document.getElementById("taxon-search").addEventListener("submit", event => {
      event.preventDefault(); search();
    });
    previous.addEventListener("click", () => { page--; render(); });
    next.addEventListener("click", () => { page++; render(); });
    if (query.value || (sortSelect && sortSelect.value)) search();
    else render();
  }).catch(() => {
    status.append(" Search is unavailable; use the page links to browse all records.");
  });
})();
