# YAML Record Review: Helicobacter pylori JK269

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_jk269.yaml`
- Started UTC: 2026-10-03T09:28:21Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:28:56Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. Taxon `NCBITaxon:103184` is
Helicobacter pylori JK269, stored as `STRAIN` beneath species 210 in
`BACTERIA`. It has `EXACT` grounding, `SEEDED` mapping status, ten ancestors,
code 11, zero attached strains, one NCBI NAME attestation and one seed
event. It contains no other synonym, nomenclature, GTDB, genome or graph
assertion. The index entry is `data/taxa/PATHS.tsv:13144`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_jk269.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_jk269.yaml`:
  passed, one file and zero errors.
- Structured checks matched ID, label, stored rank, parent, code and all
  ten ancestor IDs, labels, ranks and parent links to inventory rows.
  The complete taxonomy parent-column scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_jk269.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was skipped: it has no documented target-only mode.
  Full source hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-inclusive target
  search found no separate history artifact. The embedded event was
  inspected and included in strict validation.

## Identity and Grounding

The inspected [NCBI JK269 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103184&lvl=&mode=node)
confirms the target ID, full name, code and lineage beneath H. pylori.
It gives `no rank` instead of the stored `STRAIN`; identity and eligibility
below species are unaffected.

StrainInfo also uses JK269 for Saccharomyces cerevisiae, taxon 4932. That
source identity excludes the yeast deposit as a match to this Helicobacter.
The near miss was examined only to prevent an incorrect join; no eukaryotic
record was selected for review.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18351` supports target identity, stored
  rank, parent, code and snapshot date 2026-09-13. Each ancestor was
  checked against its separate inventory row.
- `data/catalog/ncbi_names-0000.jsonl.gz:38364` supplies the scientific
  name for the exact target taxon.
- `curation/seed_scope.tsv:144012` supports the rationale preserved in
  the seed event. One NCBI NAME assertion is supported, not a genome or
  phenotype count.
- No gene, regulator, pathway, phenotype, literature or expression claim
  is present. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive searches for the ID, full name, slug and whole JK269
covered reports, history, curation, raw, ATB and StrainInfo uncompressed
inventories. Only target taxonomy and scope rows matched. No prior target
report, separate history artifact or culture candidate was found there.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo. The native NCBI name was the only
target-specific match. The other result,
`data/straininfo/records.jsonl.gz:72554`, identifies SI-ID106756,
DOI 10.60712/SI-ID106756.1, and deposit SI-DP317933 (KCTC 7309) as
Saccharomyces cerevisiae and lists JK269 as a designation. No deposit or
sequence was transferred from that unrelated source record.

The ATB full TSV.XZ was not scanned. These bounded searches do not prove
that the target has never been deposited or sequenced. Empty optional
fields and zero attached strains remain consistent with the inspected
target-specific evidence.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The browser's `no rank` conflicts
  with inventory/YAML `STRAIN`. The inspected importer in
  `src/taxonmech/ncbi_taxdump.py` directly normalizes native ranks. An
  ignored-inclusive checkout filename search did not locate the archive
  pinned in `conf/ncbi_taxdump.yaml`. Source-version divergence versus
  import error remains unresolved.

## Recommended Edits

No generated-record edit is justified. Resolve the rank conflict from the
hash-verified pinned source before changing the configured snapshot or
importer. Do not add a StrainInfo deposit from the reused JK269 shorthand.
Any supported rank correction must flow through maintained inputs or the
importer with a regression test, then normal extraction and seeding.

## Follow-up Checks

- Inspect taxon 103184 in the configured archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- Following a separately authorized correction, refresh inputs, run
  `just seed-canary NCBITaxon:103184`, both target validators and full
  `just verify-corpus`.

## Additional Notes

The authority page was inspected through the parent-species page's link.
External archive copies were not checked. The yeast record was used only
to reject a false identity match. No paid research, outbound messages,
GitHub mutation, curation-history addition or review-status promotion occurred.
