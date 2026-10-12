# YAML Record Review: Stanieria cyanosphaera

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/stanieria_cyanosphaera.yaml
- Started UTC: 2026-10-02T12:36:46Z
- Finished UTC: 2026-10-02T12:36:46Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102116` |
| Label | `Stanieria cyanosphaera` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:102115` |
| Parent label | `Stanieria` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| NCBI synonyms | 3 |
| Source attestations | `NCBITAXON`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/stanieria_cyanosphaera.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/delta_proteobacterium_s2651.yaml data/taxa/bacteria/stanieria_cyanosphaera.yaml data/taxa/bacteria/oscillatoria_sancta.yaml data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 71 lines, 10 lineage entries, 3 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI, MADIN, and NCBI type-material rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102111\|102116\|102117\|102118)([^0-9]\|$)' data curation` | Pass: found the generated species YAML plus expected descendant strain references; no competing `NCBITaxon:102116` identity record was present. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the MADIN-backed species rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10512 maps `NCBITaxon:102116` to `stanieria_cyanosphaera`.
- `curation/seed_scope.tsv` row 53664 keeps this taxon in scope with a two-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17809 names `NCBITaxon:102116` as `Stanieria cyanosphaera`, with species rank, `Stanieria` parent `NCBITaxon:102115`, genetic code 11, and three NCBI synonyms.
- The generated YAML line 1 preserves the exact NCBI identifier; lines 7-36 preserve the 10-row NCBI lineage ending at `NCBITaxon:102115`.
- `data/raw/madin_taxa.tsv` row 483 reports three trait assertions filed directly under `NCBITaxon:102116`.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, exact synonym, and two related synonyms.
- The MADIN aggregate row supports the three-assertion MADIN source attestation.
- `data/raw/ncbi_type_material.tsv` rows 1235-1244 keep exact type-material strings for `NCBITaxon:102116`; they do not require a generated strain entry without a matching BacDive, StrainInfo, or culture-collection source row.
- No source external xrefs, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI, MADIN, and NCBI type-material inputs currently present for this species.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102116`.
- This review did not infer additional strain entries, top-level genome records, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/stanieria_cyanosphaera.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/stanieria_cyanosphaera.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:102116` after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10512 |
| `curation/seed_scope.tsv` | 53664 |
| `data/raw/ncbitaxon_taxa.tsv` | 17809 |
| `data/raw/madin_taxa.tsv` | 483 |
| `data/raw/ncbi_type_material.tsv` | 1235-1244 |
| `data/taxa/bacteria/stanieria_cyanosphaera.yaml` | 1, 39, 52, and 59 |

- The exact-ID scan also found generated Stanieria strain records under `NCBITaxon:102116`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/stanieria_cyanosphaera.yaml` directly.
