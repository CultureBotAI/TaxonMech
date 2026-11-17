# YAML Record Review: Helicobacter pylori HP197

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp197.yaml`
- Started UTC: 2026-10-03T09:19:03Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:19:36Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103180` denotes
Helicobacter pylori HP197 beneath species 210. It declares `STRAIN`,
`BACTERIA`, `EXACT` grounding and `SEEDED` mapping status. It carries ten
ancestors, code 11, zero attached strains, one NCBI NAME attestation and
a seed event. There are no synonym, GTDB, nomenclature, genome or graph
assertions. The index entry is `data/taxa/PATHS.tsv:13140`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp197.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp197.yaml`:
  passed, one file and zero errors.
- Structured checks matched ID, label, stored rank, parent, code and all
  ten ancestor IDs, labels, ranks and parent links. The complete taxonomy
  inventory scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_hp197.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full catalog
  hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-inclusive target
  search found no separate history artifact. Strict validation covers
  the inspected embedded seed event.

## Identity and Grounding

The inspected [NCBI HP197 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103180&lvl=&mode=node)
supports the ID, label, genetic code and lineage beneath H. pylori. It
reports `no rank` rather than the inventory's `STRAIN`. Primary identity
and scope below species are supported; the rank discrepancy is unresolved.

A StrainInfo use of the shorthand HP197 belongs to Didymium iridis,
taxon 5793, not this target. Shared shorthand does not establish a deposit
or taxonomic match. No eukaryotic record was selected for review.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18347` supplies the target identity,
  stored rank, parent 210, code 11 and snapshot 2026-09-13. Every ancestor
  was checked against its separate inventory row.
- `data/catalog/ncbi_names-0000.jsonl.gz:38360` supplies the scientific
  name for taxon 103180.
- The source row lists only NCBI, matching one NAME assertion and its
  snapshot note, not a phenotype or genome count.
- `curation/seed_scope.tsv:144008` supports the one-source rationale
  retained by the seed event. SEEDED does not imply human review.

The record cites no literature, gene, regulator, phenotype or transcriptomic
claim. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive ID/name/slug and standalone HP197 searches covered
reports, history, curation, raw, ATB and StrainInfo uncompressed inventories.
Only the target taxonomy/scope rows matched. No prior target report,
separate history artifact or BacDive/culture candidate was found there.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo. The only target-specific match was
the native NCBI name. The additional match at
`data/straininfo/records.jsonl.gz:198366` identifies SI-ID256408, deposit
SI-DP602080 (ATCC 38954), as Didymium iridis and lists HP197 as a designation.
That inspected source identity excludes it as evidence for this Helicobacter
record; no sequence or deposit was transferred.

The ATB full TSV.XZ was not scanned. These bounded findings do not prove
that the target has never been deposited or sequenced. Empty optional slots
and zero attached strains remain consistent with the evidence inspected.

## Findings

- **Blocker:** None found in primary identity or structure.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The browser reports `no rank`,
  while the inventory/YAML store `STRAIN`. The importer in
  `src/taxonmech/ncbi_taxdump.py` directly normalizes source rank. The
  archive pinned by `conf/ncbi_taxdump.yaml` was not found by the
  ignored-inclusive checkout filename search in this review session.
  Source-version divergence versus import error remains unresolved;
  species parentage and scope are unaffected.

## Recommended Edits

No immediate generated-record edit is justified. Inspect the hash-verified
pinned source before changing rank inputs or importer behavior. Do not
create a StrainInfo deposit link from the reused HP197 designation.

## Follow-up Checks

- Inspect target 103180 in the archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- If a correction is supported and separately authorized, use the normal
  input refresh, `just seed-canary NCBITaxon:103180`, both target
  validators and full `just verify-corpus`.

## Additional Notes

The authority page was reached through its link on the previously inspected
parent-species page. The Didymium hit was inspected only to reject an
identity near miss, not to reopen eukaryotic review. External archive copies
were not checked. No paid research, outbound messages, GitHub mutation,
history addition or status promotion occurred.
