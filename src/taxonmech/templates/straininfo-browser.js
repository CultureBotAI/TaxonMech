/* StrainInfo's own-deposit sequence assertions stay separate from local context. */
"use strict";
(() => {
  const pageSize = 25;
  const query = document.getElementById("straininfo-query");
  const status = document.getElementById("straininfo-status");
  const tbody = document.querySelector("#straininfo-results tbody");
  const detail = document.getElementById("straininfo-detail");
  const previous = document.getElementById("straininfo-prev");
  const next = document.getElementById("straininfo-next");
  let rows = [], filtered = [], page = 0, selection = 0;
  const cache = new Map();
  const element = (tag, text) => {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    return node;
  };
  function link(label, href) {
    const node = element("a", label);
    if (typeof href !== "string" || !href) return node;
    try {
      const url = new URL(href, window.location.href);
      if (["http:", "https:"].includes(url.protocol)) node.href = url.href;
    } catch (_) { /* Unusable source links remain readable text. */ }
    return node;
  }
  function evidence(label, value) {
    const node = element("details");
    node.append(element("summary", label), element("pre", JSON.stringify(value, null, 2)));
    return node;
  }
  const displayId = id => id.replace("straininfo.strain:", "SI-ID").replace("straininfo.deposit:", "SI-DP");
  async function showRecord(identifier) {
    const request = ++selection;
    detail.replaceChildren();
    detail.hidden = !identifier;
    if (!identifier) return;
    const index = rows.find(row => row.straininfo_strain_id === identifier);
    if (!index) {
      detail.append(element("p", "This source strain record is not in the linked snapshot browser."));
      return;
    }
    detail.append(element("p", "Loading deposits and source evidence…"));
    let row;
    try {
      if (!cache.has(index.detail_path)) {
        cache.set(index.detail_path, await window.TaxonMechData.loadJSON(index.detail_path));
      }
      if (request !== selection) return;
      row = cache.get(index.detail_path).find(item => item.straininfo_strain_id === identifier);
      if (!row) throw new Error("Record absent from detail batch");
    } catch (_) {
      if (request === selection) detail.replaceChildren(element("p", "Could not load source evidence. Reload this page or use the committed inventories."));
      return;
    }
    detail.replaceChildren(element("h2", displayId(identifier)), link("Native StrainInfo record", row.url),
      element("p", "Source record status: " + row.strain_status));
    if (row.strain_doi) detail.append(element("p", "Record-version DOI: "), link(row.strain_doi, row.doi_url));
    detail.append(element("h3", "Matched deposits and their explicit source sequences"));
    for (const match of row.matches) {
      const section = element("section");
      section.append(element("h4", match.deposit_designation + " · " + displayId(match.straininfo_deposit_id)),
        link("Native deposit view", match.url),
        element("p", match.strain_id + " · matched " + match.matched_strain_id + " · deposit status: " + match.deposit_status));
      const sourceEvidence = match.related_records.find(item => item.straininfo_evidence)?.straininfo_evidence;
      if (sourceEvidence?.bacdive_reference_conflict) section.append(element("p",
        "The source BacDive reference differs from the matched local BacDive record. The culture-deposit match and both references are retained."));
      section.append(element("h5", "NCBI assemblies asserted for this deposit"));
      if (!match.assemblies.length) section.append(element("p", "No NCBI assembly assertion imported for this deposit."));
      const assemblies = element("ul");
      for (const assembly of match.assemblies) {
        const item = element("li");
        item.append(link(assembly.assembly_id, assembly.url),
          evidence("Inspect explicit deposit-to-assembly evidence", assembly));
        assemblies.append(item);
      }
      section.append(assemblies);
      const sequences = match.related_records.filter(item => item.record_type === "NUCLEOTIDE_SEQUENCE");
      if (sequences.length) {
        section.append(element("h5", "Nucleotide sequence references (not genome counts)"));
        const list = element("ul");
        for (const sequence of sequences) {
          const item = element("li");
          item.append(link(sequence.record_id, sequence.url), " · " + sequence.straininfo_evidence.sequence_type,
            evidence("Inspect deposit-to-sequence evidence", sequence));
          list.append(item);
        }
        section.append(list);
      }
      section.append(evidence("Inspect matched deposit and related-record evidence", match));
      detail.append(section);
    }
    detail.append(element("h3", "Existing TaxonMech strain associations"), element("p",
      "These genome links belong to the local BacDive strain and retain their original sources. Their presence here does not establish a StrainInfo deposit assertion or genome equivalence; inspect the explicit deposit evidence above."));
    for (const strain of row.strains) {
      const section = element("section");
      section.append(element("h4", strain.strain_id),
        link(strain.source_id, "https://bacdive.dsmz.de/strain/" + strain.source_id.replace(/^bacdive:/, "")),
        element("p", strain.designation), element("p", strain.culture_collection_ids.join(" · ")));
      for (const taxon of strain.taxon_pages) section.append(link(taxon.label + " strain listing", taxon.page), " ");
      if (!strain.taxon_pages.length) section.append(element("p", "Not listed on a taxon page; retained in the uncapped inventory."));
      const list = element("ul");
      for (const association of strain.existing_genome_associations) {
        const item = element("li");
        item.append(link(association.genome_id, association.url),
          evidence("Inspect original TaxonMech genome assertion", association.source_evidence));
        list.append(item);
      }
      section.append(list);
      if (!strain.existing_genome_associations.length) section.append(element("p", "No prior genome association imported for this local strain."));
      detail.append(section);
    }
    detail.append(evidence("Source record metadata and matched deposit metadata", row.source_metadata));
  }
  function render() {
    tbody.replaceChildren();
    const start = page * pageSize;
    for (const row of filtered.slice(start, start + pageSize)) {
      const tr = element("tr"), identifier = element("td");
      identifier.append(link(displayId(row.straininfo_strain_id), "#" + row.straininfo_strain_id));
      const deposits = [...new Set(row.matches.map(item => item.deposit_designation))];
      const preview = deposits.slice(0, 4).join(" · ") + (deposits.length > 4 ? " · +" + (deposits.length - 4) + " more" : "");
      tr.append(identifier, element("td", preview),
        element("td", String(new Set(row.matches.map(item => item.strain_id)).size)),
        element("td", String(row.assembly_ids.length)), element("td", row.strain_status));
      tbody.append(tr);
    }
    status.textContent = filtered.length + " of " + rows.length + " linked source strain records match.";
    document.getElementById("straininfo-page").textContent = filtered.length ?
      (start + 1) + "–" + Math.min(start + pageSize, filtered.length) : "No results";
    previous.disabled = page === 0;
    next.disabled = start + pageSize >= filtered.length;
  }
  function search() {
    const term = query.value.toLowerCase().trim();
    filtered = rows.filter(row => row.searchText.includes(term));
    page = 0;
    render();
  }
  function selectHash() {
    let identifier;
    try { identifier = decodeURIComponent(window.location.hash.slice(1)); }
    catch (_) { identifier = window.location.hash.slice(1); }
    if (identifier.startsWith("SI-ID")) identifier = identifier.replace("SI-ID", "straininfo.strain:");
    showRecord(identifier);
  }
  document.getElementById("straininfo-search").addEventListener("submit", event => { event.preventDefault(); search(); });
  query.addEventListener("input", search);
  previous.addEventListener("click", () => { page--; render(); });
  next.addEventListener("click", () => { page++; render(); });
  window.addEventListener("hashchange", selectHash);
  async function loadIndex() {
    if (typeof window.DecompressionStream === "function") {
      try {
        const response = await fetch("straininfo-index.json.gz");
        if (!response.ok || !response.body) throw new Error("Compressed index request failed");
        const stream = response.body.pipeThrough(new window.DecompressionStream("gzip"));
        return await new Response(stream).json();
      } catch (_) { /* Plain JSON also supports older browsers and incomplete deployments. */ }
    }
    const response = await fetch("straininfo-index.json");
    if (!response.ok) throw new Error("Index request failed");
    return response.json();
  }
  loadIndex().then(data => {
    rows = data.records.map(row => ({...row, searchText: [row.straininfo_strain_id,
      displayId(row.straininfo_strain_id), row.strain_doi, ...row.assembly_ids, ...row.sequence_ids,
      ...row.matches.flatMap(match => [match.strain_id, match.strain_id.replace("kgmicrobe.strain:bacdive_", "bacdive:"),
        match.straininfo_deposit_id, displayId(match.straininfo_deposit_id), match.matched_strain_id,
        match.deposit_designation])].join(" ").toLowerCase()}));
    search();
    selectHash();
  }).catch(() => { status.textContent = "Could not load the strain index. Reload this page or use the linked inventories."; });
})();
