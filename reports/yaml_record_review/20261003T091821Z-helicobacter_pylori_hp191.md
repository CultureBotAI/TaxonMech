# YAML Record Review: Helicobacter pylori HP191

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp191.yaml`
- Started UTC: 2026-10-03T09:17:48Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:18:21Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:103179` denotes
Helicobacter pylori HP191 below species 210. It declares `STRAIN`,
`BACTERIA`, `EXACT` grounding and `SEEDED` mapping status, ten ancestors,
genetic code 11 and zero attached strains. Its sole attestation is one
NCBI NAME assertion, with one seed event. There are no synonym, GTDB,
nomenclature, genome or graph assertions. The index entry is
`data/taxa/PATHS.tsv:13139`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp191.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp191.yaml`:
  passed, one file and zero errors.
- Structured checks matched ID, label, stored rank, parent, genetic code
  and all ten ancestor IDs, labels, ranks and parent links. A complete
  taxonomy inventory scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_hp191.yaml`
  passed; no record or maintained input changed.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full catalog
  hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-inclusive target
  search found no separate history artifact. Strict validation covers
  the inspected embedded event.

## Identity and Grounding

The inspected [NCBI HP191 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103179&lvl=&mode=node)
supports ID, label, genetic code and lineage beneath H. pylori. It reports
`no rank`, not the pinned inventory's `STRAIN`. Primary identity and
eligibility below species are supported; the rank discrepancy is unresolved.
The target is not equated to its parent or a neighboring HP-numbered strain.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18346` supplies the target ID/name, rank,
  parent 210, code 11 and snapshot 2026-09-13. All ancestors were checked
  against their separate rows.
- `data/catalog/ncbi_names-0000.jsonl.gz:38359` supplies the scientific
  name for taxon 103179.
- The source row lists only NCBI, supporting one NAME attestation and
  the snapshot note, not a biological trait or genome count.
- `curation/seed_scope.tsv:144007` supports the one-source rationale
  retained by the seed event. SEEDED does not imply human review.

The record contains no literature citation, gene, regulatory, phenotype
or transcriptomic claim. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive ID/name/slug and standalone HP191 searches covered
reports, history, curation, raw, ATB and StrainInfo uncompressed inventories.
Only the target taxonomy/scope rows matched. No prior target report,
separate history artifact or BacDive/culture candidate was found there.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo using exact taxon fields, name, slug
and standalone HP191. The only match was the native NCBI name row.
The ATB full TSV.XZ was not scanned. These bounded findings do not prove
that HP191 has never been deposited or sequenced.

Empty optional fields and zero attached strains are consistent with the
inspected evidence. No species-level type strain, assembly or phenotype
was transferred to the target.

## Findings

- **Blocker:** None found in identity or structure.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The browser reports `no rank`,
  while the inventory/YAML store `STRAIN`. The importer in
  `src/taxonmech/ncbi_taxdump.py` directly normalizes source rank. The
  archive pinned by `conf/ncbi_taxdump.yaml` was not found in the
  ignored-inclusive checkout filename search during this review session.
  Source-version divergence versus import error remains unresolved;
  parentage and scope are unaffected.

## Recommended Edits

No immediate generated-record edit is justified. Inspect the hash-verified
pinned source before changing the rank inventory or importer. Preserve
empty optional fields until target-specific evidence supports additions.

## Follow-up Checks

- Inspect taxon 103179 in the archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- If a correction is supported and separately authorized, use the normal
  input refresh, `just seed-canary NCBITaxon:103179`, both target
  validators and full `just verify-corpus`.

## Additional Notes

The authority page was reached through its link on the previously inspected
parent-species page. External copies of the pinned archive were not checked.
No paid research, outbound messages, GitHub mutation, history entry or
review-status promotion occurred.
