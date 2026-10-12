# YAML Record Review: Capnocytophaga sputigena

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/capnocytophaga_sputigena.yaml
- Started UTC: 2026-10-02T11:26:42Z
- Finished UTC: 2026-10-02T11:26:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1019` |
| Label | `Capnocytophaga sputigena` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1016` |
| Parent label | `Capnocytophaga` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Nomenclature | `lpsn:774470` |
| GTDB mapping | `GTDB:s__Capnocytophaga_sputigena` |
| Strains | 34 BacDive strain entries |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/capnocytophaga_sputigena.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/capnocytophaga_sputigena.yaml data/taxa/bacteria/ehrlichia_sp_casc.yaml` | Pass: the strict two-file batch scanned 2 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 3,480 lines, 11 lineage entries, 2 synonyms, 2 xrefs, 34 declared strains, 1 taxonomy mapping, and 6 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI, LPSN, GTDB, BacDive, GOLD, MADIN, type-material, and StrainInfo rows. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*capnocytophaga_sputigena.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1019)([^0-9]\|$)' data curation` | Pass: found the generated species YAML plus expected descendant and related-record references; no competing `NCBITaxon:1019` identity record was present. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the multi-source species rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10408 maps `NCBITaxon:1019` to `capnocytophaga_sputigena`.
- `curation/seed_scope.tsv` row 8430 keeps this taxon in scope with a six-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 792 names `NCBITaxon:1019` as `Capnocytophaga sputigena`, with species rank, `Capnocytophaga` parent `NCBITaxon:1016`, genetic code 11, and two NCBI synonyms.
- The generated YAML line 1 preserves the exact NCBI identifier; lines 7-39 preserve the 11-row NCBI lineage ending at `NCBITaxon:1016`.
- `data/raw/lpsn_names.tsv` row 16025 maps `lpsn:774470` to this species, flags it as validly published, legitimate, and the correct name, and links the LPSN name to `NCBITaxon:1019`.
- `data/raw/gtdb_mappings.tsv` row 1185 maps `GTDB:s__Capnocytophaga_sputigena` to `NCBITaxon:1019` with `skos:closeMatch`, and `data/raw/gtdb_species.tsv` row 40646 reports 45 genomes for that GTDB species.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, and two related synonyms.
- The LPSN row supports the nomenclature block, `lpsn:774470` xref, eight listed type-strain designations, three publication identifiers, and `INSDC:X67609`.
- The GTDB rows support the `skos:closeMatch` taxonomy mapping and the 45-genome source attestation.
- The `bacdive_5490` type-strain row is filed under descendant `NCBITaxon:553177` and remains safely scoped by `classified_as: NCBITaxon:553177` in the generated strain entry.
- The other 33 `data/raw/bacdive_strains.tsv` rows for `NCBITaxon:1019` account for the remaining BacDive strain entries, from `bacdive_137791` through the CRBIP-only `bacdive_174172` and `bacdive_174173` rows.
- The GOLD and MADIN source attestation counts match their exact aggregate rows: 74 GOLD organisms and 4 MADIN trait assertions.

## Completeness

- The record is complete for the exact NCBI, LPSN, GTDB, BacDive, GOLD, MADIN, type-material, and StrainInfo inputs currently present for this species.
- The seed count intentionally aggregates 33 BacDive rows filed directly under `NCBITaxon:1019` with one type-strain BacDive row filed under descendant `NCBITaxon:553177`.
- Exact `history/` searches for `NCBITaxon:1019`, `capnocytophaga_sputigena`, and `Capnocytophaga sputigena` found no append-only history record for this generated YAML.
- This review did not infer additional type strains, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/capnocytophaga_sputigena.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/capnocytophaga_sputigena.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:1019`, `lpsn:774470`, and `GTDB:s__Capnocytophaga_sputigena` after any refresh of `data/raw/`, `data/atb/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10408 |
| `curation/seed_scope.tsv` | 8430 |
| `data/raw/ncbitaxon_taxa.tsv` | 792 |
| `data/raw/lpsn_names.tsv` | 16025 |
| `data/raw/gtdb_mappings.tsv` | 1185 |
| `data/raw/gtdb_species.tsv` | 40646 |
| `data/raw/gold_organisms.tsv` | 305 |
| `data/raw/madin_taxa.tsv` | 480 |
| `data/taxa/bacteria/capnocytophaga_sputigena.yaml` | 1, 42, 69, 76, 89, and 3437 |

- The exact-ID scan also found `Capnocytophaga sputigena ATCC 33612` and `Capnocytophaga sputigena CC21_001D` generated as descendant strain records under `NCBITaxon:1019`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/capnocytophaga_sputigena.yaml` directly.
