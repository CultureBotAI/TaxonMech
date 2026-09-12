/* The browser reads only TaxonMech's committed overlap, never the full catalog. */
"use strict";
(() => {
  const pageSize = 25;
  const query = document.getElementById("atb-query");
  const status = document.getElementById("atb-status");
  const tbody = document.querySelector("#atb-results tbody");
  const detail = document.getElementById("atb-detail");
  const previous = document.getElementById("atb-prev");
  const next = document.getElementById("atb-next");
  let rows = [], filtered = [], page = 0;
  const detailCache = new Map();
  let selection = 0;
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
    } catch (_) { /* Invalid source URLs remain readable text. */ }
    return node;
  }
  function sourceDetails(label, evidence) {
    const node = element("details");
    node.append(element("summary", label), element("pre", JSON.stringify(evidence, null, 2)));
    return node;
  }
  function sampleLink(sample) {
    return link(sample, "https://www.ncbi.nlm.nih.gov/biosample/" + sample.replace(/^biosample:/, ""));
  }
  async function showAssembly(identifier) {
    const request = ++selection;
    let row = rows.find(item => item.atb_id === identifier);
    detail.replaceChildren();
    detail.hidden = !identifier;
    if (!identifier) return;
    if (!row) {
      detail.append(element("p", "This assembly is not in the linked snapshot browser. Search the full catalog with the command-line query."));
      return;
    }
    if (row.detail_path) {
      detail.append(element("p", "Loading assembly metadata and source evidence…"));
      try {
        if (!detailCache.has(row.detail_path)) {
          const response = await fetch(row.detail_path);
          if (!response.ok) throw new Error("Assembly detail request failed");
          detailCache.set(row.detail_path, await response.json());
        }
        if (request !== selection) return;
        row = detailCache.get(row.detail_path).find(item => item.atb_id === identifier);
        if (!row) throw new Error("Assembly is missing from its detail batch");
        detail.replaceChildren();
      } catch (_) {
        if (request === selection) detail.replaceChildren(element("p", "Could not load assembly evidence. Reload this page or use the committed TSV inventories."));
        return;
      }
    }
    const m = row.metadata;
    detail.append(element("h2", row.atb_id), element("p", m.scientific_name), sampleLink(row.sample_id));
    const downloads = element("p");
    if (m.aws_url && m.aws_url !== "NA") downloads.append(link("Assembly FASTA", m.aws_url), " · ");
    if (/^ERZ\d+$/.test(m.assembly_accession || "")) downloads.append(link("ENA " + m.assembly_accession, "https://www.ebi.ac.uk/ena/browser/view/" + m.assembly_accession), " · ");
    if (m.osf_tarball_url && m.osf_tarball_url !== "NA") downloads.append(link("Source archive", m.osf_tarball_url));
    detail.append(downloads);
    const values = element("dl");
    for (const [name, value] of [["Snapshot", row.release], ["Dataset", m.dataset],
      ["Assembly filter", m.asm_pipe_filter], ["HQ filter", m.hq_filter],
      ["Run accessions", m.run_accession], ["SeqKit sum (not MD5)", m.assembly_seqkit_sum],
      ["Archive filename", m.osf_tarball_filename], ["Sylph species", m.sylph_species]]) {
      values.append(element("dt", name), element("dd", value || "Not supplied"));
    }
    detail.append(values, element("h3", "Strains and source sample evidence"));
    const strains = element("ul");
    for (const strain of row.strains) {
      const item = element("li");
      item.append(link(strain.source_id, "https://bacdive.dsmz.de/strain/" + strain.source_id.replace(/^bacdive:/, "")),
        " · " + strain.strain_id + (strain.designation ? " · " + strain.designation : ""));
      item.append(element("p", strain.culture_collection_ids.join(" · ")));
      for (const taxon of strain.taxon_pages) item.append(link(taxon.label + " strain listing", taxon.page), " ");
      if (!strain.taxon_pages.length) item.append(element("p", "Not listed on a taxon page; the BacDive source and full inventory retain this strain."));
      item.append(sourceDetails("Inspect strain-to-BioSample evidence", strain.sample_evidence));
      if (strain.straininfo_context?.length) {
        const context = element("p", "StrainInfo context for this local strain: ");
        for (const entry of strain.straininfo_context) context.append(link(entry.straininfo_strain_id, entry.url), " ");
        item.append(context);
      }
      strains.append(item);
    }
    detail.append(strains, element("h3", "Genome crosslinks — shared BioSample"),
      element("p", "These source chains connect genome records to the same sample. They do not assert identical sequences or paired assemblies."));
    const genomes = element("ul");
    for (const genome of row.genome_links) {
      const item = element("li");
      item.append(link(genome.genome_id, genome.url), " · " + genome.strain_id + " · " + genome.relationship,
        sourceDetails("Inspect genome and sample source evidence", genome.source_evidence));
      genomes.append(item);
    }
    detail.append(genomes);
    if (!row.genome_links.length) detail.append(element("p", "No genome crosslink with a matching source chain was imported."));
    detail.append(sourceDetails("All original assembly metadata fields", m));
  }
  function render() {
    tbody.replaceChildren();
    const start = page * pageSize;
    for (const row of filtered.slice(start, start + pageSize)) {
      const tr = element("tr");
      const id = element("td");
      id.append(link(row.atb_id, "#" + row.atb_id), element("br"), sampleLink(row.sample_id));
      tr.append(id, element("td", row.metadata.scientific_name), element("td", String(row.strains.length)),
        element("td", String(new Set(row.genome_links.map(item => item.genome_id)).size)),
        element("td", row.metadata.asm_pipe_filter + " · " + row.metadata.hq_filter));
      tbody.append(tr);
    }
    status.textContent = filtered.length + " of " + rows.length + " linked assemblies match.";
    document.getElementById("atb-page").textContent = filtered.length ?
      (start + 1) + "–" + Math.min(start + pageSize, filtered.length) : "No results";
    previous.disabled = page === 0;
    next.disabled = start + pageSize >= filtered.length;
  }
  function search() {
    const terms = query.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    filtered = rows.filter(row => terms.every(term => row.searchText.includes(term)));
    page = 0;
    render();
  }
  function selectHash() {
    let identifier;
    try { identifier = decodeURIComponent(window.location.hash.slice(1)); }
    catch (_) { identifier = window.location.hash.slice(1); }
    showAssembly(identifier);
  }
  document.getElementById("atb-search").addEventListener("submit", event => { event.preventDefault(); search(); });
  query.addEventListener("input", search);
  previous.addEventListener("click", () => { page--; render(); });
  next.addEventListener("click", () => { page++; render(); });
  window.addEventListener("hashchange", selectHash);
  fetch("atb-index.json").then(response => {
    if (!response.ok) throw new Error("Index request failed");
    return response.json();
  }).then(data => {
    rows = data.assemblies.map(row => ({...row, searchText: [row.atb_id, row.sample_id,
      row.metadata.assembly_accession, row.metadata.scientific_name, row.metadata.sylph_species,
      ...row.strains.flatMap(strain => [strain.strain_id, strain.source_id, strain.designation, ...strain.culture_collection_ids]),
      ...row.genome_links.map(item => item.genome_id)].join(" ").toLowerCase()}));
    search();
    selectHash();
  }).catch(() => { status.textContent = "Could not load the assembly index. Reload this page or use the linked TSV inventories."; });
})();
