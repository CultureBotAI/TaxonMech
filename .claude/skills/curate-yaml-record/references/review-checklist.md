# TaxonRecord review checklist

Use this checklist for one taxon. It is not a requirement to populate every
optional slot or invent a causal graph.

## Evidence standard

- Every seeded value traces to a row in `data/raw/`; find the row before
  judging the value.
- Verify identifiers at their authority: NCBI Taxonomy browser, LPSN name
  page, GTDB taxon page, BacDive strain page.
- A count is a count of upstream records, not a biological claim.
- Preserve conflicts (NCBI vs LPSN on the current name) as findings, never by
  choosing one silently.

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | NCBI id, label, rank and domain agree with NCBI Taxonomy. | Homonyms and subspecies are explicitly distinguished. |
| Lineage | Root-first chain matches NCBI's; ranks are right. | Every ancestor has a label. |
| Synonyms | Each has a source; LPSN synonyms resolve to a real LPSN name. | No NCBI synonym is misfiled as exact. |
| Nomenclature | LPSN id maps to this taxon; status line is current; type strain designations are LPSN's. | Correct name vs synonym is stated, not implied. |
| Mappings | GTDB predicate is defensible; genome count matches GTDB. | broadMatch is not presented as equivalence. |
| Strains | Type strain flag traces to an LPSN designation; deposits are BacDive's. | Capped listing is stated with the true count. |
| Attestations | Each source, id, count and unit agree with the inventory. | Units are never summed across sources. |
| Causal graph | Scope, nodes, edges, direction and edge-level evidence agree. | Every edge is supported. |
| Status/audit | Mapping status and both history surfaces match the review performed. | Agent drafts stay PROPOSED; REVIEWED has human sign-off. |
