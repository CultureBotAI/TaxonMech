# YAML Record Review: Synechococcus sp. C9

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/synechococcus_sp_c9.yaml
- Started UTC: 2026-10-02T12:39:56Z
- Finished UTC: 2026-10-02T12:39:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102119` |
| Label | `Synechococcus sp. C9` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2626047` |
| Parent label | `unclassified Synechococcus` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| GTDB mapping | `GTDB:s__Gloeomargarita_sp022984075` |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/synechococcus_sp_c9.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/synechococcus_sp_c9.yaml data/taxa/bacteria/synechococcus_sp_p1.yaml data/taxa/bacteria/synechococcus_sp_p2.yaml data/taxa/bacteria/chlorogloeopsis_fritschii_pcc_6718.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 82 lines, 11 lineage entries, 3 synonyms, 1 xref, 0 declared strains, 1 taxonomy mapping, and 2 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI and GTDB rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102119\|102120\|102121\|102122)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to source rows, `PATHS.tsv`, `seed_scope.tsv`, and the generated YAMLs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the GTDB-backed species rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10515 maps `NCBITaxon:102119` to `synechococcus_sp_c9`.
- `curation/seed_scope.tsv` row 64047 keeps this taxon in scope with a two-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17812 names `NCBITaxon:102119` as `Synechococcus sp. C9`, with species rank, `unclassified Synechococcus` parent `NCBITaxon:2626047`, genetic code 11, and two NCBI synonyms.
- `data/raw/gtdb_mappings.tsv` row 1187 maps `GTDB:s__Gloeomargarita_sp022984075` to `NCBITaxon:102119` with `skos:closeMatch` and a two-genome count.
- The generated YAML line 1 preserves the exact NCBI identifier; lines 7-39 preserve the 11-row NCBI lineage ending at `NCBITaxon:2626047`.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, and two exact NCBI synonyms.
- The GTDB mapping row supports the `skos:closeMatch` taxonomy mapping, `GTDB:s__Gloeomargarita_sp022984075` xref, `Gloeomargarita sp022984075` exact synonym, and 2-genome GTDB source attestation.
- No source strain rows, genome assemblies, top-level genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI and GTDB mapping rows currently present for this species.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- This review did not infer additional strain entries, top-level genome records, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/synechococcus_sp_c9.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/synechococcus_sp_c9.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:102119` and `GTDB:s__Gloeomargarita_sp022984075` after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10515 |
| `curation/seed_scope.tsv` | 64047 |
| `data/raw/ncbitaxon_taxa.tsv` | 17812 |
| `data/raw/gtdb_mappings.tsv` | 1187 |
| `data/taxa/bacteria/synechococcus_sp_c9.yaml` | 1, 42, 48, 59, and 63 |

- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/synechococcus_sp_c9.yaml` directly.
