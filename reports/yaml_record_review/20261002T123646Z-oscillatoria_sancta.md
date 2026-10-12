# YAML Record Review: Oscillatoria sancta

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/oscillatoria_sancta.yaml
- Started UTC: 2026-10-02T12:36:46Z
- Finished UTC: 2026-10-02T12:36:46Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102117` |
| Label | `Oscillatoria sancta` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1158` |
| Parent label | `Oscillatoria` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| NCBI synonyms | 1 |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/oscillatoria_sancta.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/delta_proteobacterium_s2651.yaml data/taxa/bacteria/stanieria_cyanosphaera.yaml data/taxa/bacteria/oscillatoria_sancta.yaml data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 60 lines, 11 lineage entries, 1 synonym, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI and NCBI type-material rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102111\|102116\|102117\|102118)([^0-9]\|$)' data curation` | Pass: found the generated species YAML plus expected descendant strain references; no competing `NCBITaxon:102117` identity record was present. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `unexpected NCBI type-material rows`, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10513 maps `NCBITaxon:102117` to `oscillatoria_sancta`.
- `curation/seed_scope.tsv` row 143500 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17810 names `NCBITaxon:102117` as `Oscillatoria sancta`, with species rank, `Oscillatoria` parent `NCBITaxon:1158`, genetic code 11, and one NCBI synonym.
- The generated YAML line 1 preserves the exact NCBI identifier; lines 7-39 preserve the 11-row NCBI lineage ending at `NCBITaxon:1158`.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, and authority synonym.
- `data/raw/ncbi_type_material.tsv` rows 1245-1246 keep exact NCBI reference-strain strings for `NCBITaxon:102117`; they do not require a generated strain entry without a matching BacDive, StrainInfo, or culture-collection source row.
- No source external xrefs, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI and NCBI type-material inputs currently present for this species.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102117`.
- This review did not infer additional strain entries, top-level genome records, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/oscillatoria_sancta.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/oscillatoria_sancta.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:102117` after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10513 |
| `curation/seed_scope.tsv` | 143500 |
| `data/raw/ncbitaxon_taxa.tsv` | 17810 |
| `data/raw/ncbi_type_material.tsv` | 1245-1246 |
| `data/taxa/bacteria/oscillatoria_sancta.yaml` | 1, 42, and 48 |

- The exact-ID scan also found generated Oscillatoria strain records under `NCBITaxon:102117`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/oscillatoria_sancta.yaml` directly.
