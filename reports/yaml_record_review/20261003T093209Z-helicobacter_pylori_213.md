# YAML Record Review: Helicobacter pylori 213

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_213.yaml`
- Started UTC: 2026-10-03T09:31:23Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:32:09Z
- Verdict: pass with minor issues

## Target

The complete generated `TaxonRecord` was read. `NCBITaxon:103186` identifies
Helicobacter pylori 213 beneath species 210, stored as `STRAIN` in
`BACTERIA`. It has ten ancestors, code 11, `EXACT` grounding, `SEEDED`
mapping status, zero attached strains, one NCBI NAME attestation and one
seed event. No synonym, nomenclature, GTDB, genome or graph assertion is
present. Its index entry is `data/taxa/PATHS.tsv:13146`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_213.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_213.yaml`:
  passed, one file and zero errors.
- Structured checks matched the identity, stored rank, parent, code and
  all ten ancestor IDs, labels, ranks and parent links to source rows.
  A complete taxonomy parent-column scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_213.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was skipped: the available reproduction gate is
  full-corpus-only. Full source hashes and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-inclusive target
  search found no separate history artifact. The embedded event was
  inspected and included in strict validation.

## Identity and Grounding

The inspected [NCBI 213 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103186&lvl=&mode=node)
supports the exact ID, name, genetic code and lineage beneath H. pylori.
Its rank is `no rank`, not the inventory's `STRAIN`. This is an unresolved
source conflict, not a change to the supported identity or species parent.

The bare numeric designation 213 recurs across unrelated source taxa.
It cannot establish a culture or genome identity on its own.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18353` supports the stored identity,
  rank, parent, code and snapshot 2026-09-13. Every ancestor was checked
  against its separate inventory row.
- `data/catalog/ncbi_names-0000.jsonl.gz:38366` supplies the target's
  scientific name under taxon 103186.
- `curation/seed_scope.tsv:144014` supports the one-source rationale in
  the seed event. The single NAME attestation agrees with NCBI identity
  evidence; it asserts no phenotype or genome count.
- The record has no gene, regulator, pathway, expression-module or
  literature assertion. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive target ID/full-name/slug searches covered reports,
history, curation, raw, ATB and StrainInfo uncompressed inventories. Only
the target taxonomy and scope rows matched. No prior target report,
separate history artifact or culture candidate was found by those keys.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo. Alongside the target keys, exact 213
values were searched in `strain`, `ncbi_strain_identifiers` and
`infraspecific_name` (including `strain=213`). All 74 matching JSON rows
were parsed for source names and taxon IDs. One was the native target name;
73 belonged to other taxa, with no additional Helicobacter match. These
included Campylobacter jejuni taxon 197, Pseudomonas aeruginosa taxon 287,
Klebsiella pneumoniae taxon 573 and Rouxiella silvae taxon 1646373. No
deposit or genome was transferred from those identity near misses.

Arbitrary numeric substrings and every possible alias field were not searched;
the ATB full TSV.XZ was not scanned. The bounded result is not proof that
the target has never been deposited or sequenced. Empty optional slots
and zero attached strains remain consistent with the inspected evidence.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The live page gives `no rank`,
  while the inventory/YAML give `STRAIN`. The inspected importer in
  `src/taxonmech/ncbi_taxdump.py` directly normalizes native ranks. The
  ignored-inclusive checkout filename search did not locate the archive
  pinned by `conf/ncbi_taxdump.yaml`. Source-version divergence versus
  import error remains unresolved.

## Recommended Edits

No generated-record edit is justified. Compare the rank to the hash-verified
pinned source before changing the configured snapshot or importer. Do not
join numeric strain names without explicit matching taxon and deposit
evidence. A demonstrated importer defect belongs in
`src/taxonmech/ncbi_taxdump.py` with a regression test, followed by normal
extraction and seeding.

## Follow-up Checks

- Inspect taxon 103186 in the configured source archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- Following a separately authorized correction, refresh inputs, run
  `just seed-canary NCBITaxon:103186`, both target validators and full
  `just verify-corpus`.

## Additional Notes

The authority page was inspected through the parent-species page's link.
Source-search matches were parsed into identity projections to avoid
truncated output; target identity evidence was inspected in full. No
external archive copy was checked. No paid research, outbound messages,
GitHub mutation, history addition or review-status promotion occurred.
