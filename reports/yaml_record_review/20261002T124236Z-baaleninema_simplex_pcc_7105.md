# YAML Record Review: Baaleninema simplex PCC 7105

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/baaleninema_simplex_pcc_7105.yaml
- Started UTC: 2026-10-02T12:42:36Z
- Finished UTC: 2026-10-02T12:42:36Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102127` |
| Label | `Baaleninema simplex PCC 7105` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2862350` |
| Parent label | `Baaleninema simplex` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| GTDB mapping | `GTDB:s__Baaleninema_simplex` |
| Source attestations | `NCBITAXON`, `GTDB`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/baaleninema_simplex_pcc_7105.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/gloeobacter_violaceus_pcc_8105.yaml data/taxa/bacteria/xenococcus_sp_pcc_7305.yaml data/taxa/bacteria/pseudanabaena_sp_pcc_6903.yaml data/taxa/bacteria/baaleninema_simplex_pcc_7105.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 96 lines, 12 lineage entries, 5 synonyms, 1 xref, 0 declared strains, 1 taxonomy mapping, and 3 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI, GTDB, and MADIN rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102124\|102125\|102126\|102127)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to source rows, `PATHS.tsv`, `seed_scope.tsv`, and the generated YAMLs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the GTDB/MADIN-backed strain rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10522 maps `NCBITaxon:102127` to `baaleninema_simplex_pcc_7105`.
- `curation/seed_scope.tsv` row 31668 keeps this taxon in scope with a three-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17819 names `NCBITaxon:102127` as `Baaleninema simplex PCC 7105`, with strain rank, `Baaleninema simplex` parent `NCBITaxon:2862350`, genetic code 11, and four NCBI synonyms.
- `data/raw/gtdb_mappings.tsv` row 1189 maps `GTDB:s__Baaleninema_simplex` to `NCBITaxon:102127` with `skos:closeMatch` and a two-genome count.
- `data/raw/madin_taxa.tsv` row 485 reports one trait assertion filed directly under `NCBITaxon:102127`.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, and four exact NCBI synonyms.
- The GTDB mapping row supports the `skos:closeMatch` taxonomy mapping, `GTDB:s__Baaleninema_simplex` xref, `Baaleninema simplex` exact synonym, and 2-genome GTDB source attestation.
- The MADIN aggregate row supports the one-assertion MADIN source attestation.
- No source strain rows, genome assemblies, top-level genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI, GTDB mapping, and MADIN rows currently present for this strain.
- Nested `strains` are absent because the record itself is the strain-rank taxon and no BacDive, culture-collection, StrainInfo, ATB, or exact strain-related rows are present.
- This review did not infer additional genome records, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/baaleninema_simplex_pcc_7105.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/baaleninema_simplex_pcc_7105.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:102127` and `GTDB:s__Baaleninema_simplex` after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10522 |
| `curation/seed_scope.tsv` | 31668 |
| `data/raw/ncbitaxon_taxa.tsv` | 17819 |
| `data/raw/gtdb_mappings.tsv` | 1189 |
| `data/raw/madin_taxa.tsv` | 485 |
| `data/taxa/bacteria/baaleninema_simplex_pcc_7105.yaml` | 1, 45, 51, 68, and 72 |

- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/baaleninema_simplex_pcc_7105.yaml` directly.
