# YAML Record Review: Leptolyngbya sp. PCC 7375

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/leptolyngbya_sp_pcc_7375.yaml
- Started UTC: 2026-10-02T12:45:50Z
- Finished UTC: 2026-10-02T12:45:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102129` |
| Label | `Leptolyngbya sp. PCC 7375` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2650499` |
| Parent label | `unclassified Leptolyngbya` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| GTDB mapping | `GTDB:s__Leptothoe_sp000316115` |
| Source attestations | `NCBITAXON`, `GTDB`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/leptolyngbya_sp_pcc_7375.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/leptolyngbya_sp_pcc_73110.yaml data/taxa/bacteria/leptolyngbya_sp_pcc_7375.yaml data/taxa/bacteria/pseudanabaena_sp_pcc_7402.yaml data/taxa/bacteria/desulfoscipio_gibsoniae.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 98 lines, 12 lineage entries, 4 synonyms, 1 xref, 0 declared strains, 1 taxonomy mapping, and 4 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI, GTDB, GOLD, and MADIN rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102128\|102129\|102130\|102134)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to source rows, `PATHS.tsv`, `seed_scope.tsv`, and the generated YAMLs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the GTDB/GOLD/MADIN-backed species rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10524 maps `NCBITaxon:102129` to `leptolyngbya_sp_pcc_7375`.
- `curation/seed_scope.tsv` row 23613 keeps this taxon in scope with a four-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17821 names `NCBITaxon:102129` as `Leptolyngbya sp. PCC 7375`, with species rank, `unclassified Leptolyngbya` parent `NCBITaxon:2650499`, genetic code 11, and three NCBI synonyms.
- `data/raw/gtdb_mappings.tsv` row 1190 maps `GTDB:s__Leptothoe_sp000316115` to `NCBITaxon:102129` with `skos:closeMatch` and a one-genome count.
- `data/raw/gold_organisms.tsv` row 312 and `data/raw/madin_taxa.tsv` row 486 support the direct GOLD and MADIN source attestations.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, and three exact NCBI synonyms.
- The GTDB mapping row supports the `skos:closeMatch` taxonomy mapping, `GTDB:s__Leptothoe_sp000316115` xref, `Leptothoe sp000316115` exact synonym, and 1-genome GTDB source attestation.
- The GOLD and MADIN aggregate rows support the one-organism GOLD source attestation and seven-assertion MADIN source attestation.
- No source strain rows, genome assemblies, top-level genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI, GTDB mapping, GOLD, and MADIN rows currently present for this species.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- This review did not infer additional strain entries, top-level genome records, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/leptolyngbya_sp_pcc_7375.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/leptolyngbya_sp_pcc_7375.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:102129` and `GTDB:s__Leptothoe_sp000316115` after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10524 |
| `curation/seed_scope.tsv` | 23613 |
| `data/raw/ncbitaxon_taxa.tsv` | 17821 |
| `data/raw/gtdb_mappings.tsv` | 1190 |
| `data/raw/gold_organisms.tsv` | 312 |
| `data/raw/madin_taxa.tsv` | 486 |
| `data/taxa/bacteria/leptolyngbya_sp_pcc_7375.yaml` | 1, 45, 51, 65, and 69 |

- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/leptolyngbya_sp_pcc_7375.yaml` directly.
