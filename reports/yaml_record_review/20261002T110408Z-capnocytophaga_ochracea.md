# YAML Record Review: Capnocytophaga ochracea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/capnocytophaga_ochracea.yaml
- Started UTC: 2026-10-02T11:04:08Z
- Finished UTC: 2026-10-02T11:04:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1018` |
| Label | `Capnocytophaga ochracea` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1016` |
| Parent label | `Capnocytophaga` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Nomenclature | `lpsn:774469` |
| GTDB mapping | `GTDB:s__Capnocytophaga_ochracea` |
| Strains | 14 BacDive strain entries |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `MEDIADIVE`, `GOLD`, `MADIN`, `BACTOTRAITS` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/capnocytophaga_ochracea.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/amazonian_soil_bacterium_m52.yaml data/taxa/bacteria/amazonian_soil_bacterium_m54.yaml data/taxa/bacteria/amazonian_soil_bacterium_m55.yaml data/taxa/bacteria/capnocytophaga_ochracea.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 2,920 lines, 11 lineage entries, 9 synonyms, 2 xrefs, 14 declared strains, 1 taxonomy mapping, and 8 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, ATB, and StrainInfo rows. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*capnocytophaga_ochracea.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1018)([^0-9]\|$)' data curation` | Pass: found the generated species YAML plus expected descendant and related-record references; no competing `NCBITaxon:1018` identity record was present. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the multi-source species rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10374 maps `NCBITaxon:1018` to `capnocytophaga_ochracea`.
- `curation/seed_scope.tsv` row 246 keeps this taxon in scope with an eight-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 791 names `NCBITaxon:1018` as `Capnocytophaga ochracea`, with species rank, `Capnocytophaga` parent `NCBITaxon:1016`, and genetic code 11.
- The generated YAML line 1 preserves the exact NCBI identifier; lines 7-39 preserve the 11-row NCBI lineage ending at `NCBITaxon:1016`.
- `data/raw/lpsn_names.tsv` row 16024 maps `lpsn:774469` to this species, flags it as validly published, legitimate, and the correct name, and links the LPSN name to `NCBITaxon:1018`.
- `data/raw/gtdb_mappings.tsv` row 1184 maps `GTDB:s__Capnocytophaga_ochracea` to `NCBITaxon:1018` with `skos:closeMatch`, and `data/raw/gtdb_species.tsv` row 40627 reports 38 genomes for that GTDB species.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, exact synonyms, and related synonyms.
- The LPSN row supports the nomenclature block, `lpsn:774469` xref, LPSN synonym `lpsn:773964`, six listed type-strain designations, three publication identifiers, and `INSDC:AB671761`.
- The GTDB rows support the `skos:closeMatch` taxonomy mapping and the 38-genome source attestation.
- The 14 `data/raw/bacdive_strains.tsv` rows for `bacdive_5488`, `bacdive_5489`, `bacdive_135187`, `bacdive_137555`, `bacdive_138017`, `bacdive_138050`, `bacdive_138195`, `bacdive_138645`, `bacdive_138740`, `bacdive_142019`, `bacdive_142323`, `bacdive_142628`, `bacdive_142759`, and `bacdive_145365` account for the 14 top-level strain entries.
- The descendant `bacdive_5488` row is filed under `NCBITaxon:521097` and remains safely scoped by `classified_as: NCBITaxon:521097` in the generated strain entry.
- The MediaDive, GOLD, MADIN, and BactoTraits source attestation counts match their exact source-count rows.

## Completeness

- The record is complete for the exact NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, ATB, and StrainInfo inputs currently present for this species.
- The seed count intentionally aggregates 13 BacDive rows filed directly under `NCBITaxon:1018` with one type-strain BacDive row filed under descendant `NCBITaxon:521097`.
- Exact `history/` searches for `NCBITaxon:1018`, `capnocytophaga_ochracea`, and `Capnocytophaga ochracea` found no append-only history record for this generated YAML.
- This review did not infer additional type strains, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/capnocytophaga_ochracea.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/capnocytophaga_ochracea.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:1018`, `lpsn:774469`, and `GTDB:s__Capnocytophaga_ochracea` after any refresh of `data/raw/`, `data/atb/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10374 |
| `curation/seed_scope.tsv` | 246 |
| `data/raw/ncbitaxon_taxa.tsv` | 791 |
| `data/raw/lpsn_names.tsv` | 16024 |
| `data/raw/gtdb_mappings.tsv` | 1184 |
| `data/raw/gtdb_species.tsv` | 40627 |
| `data/raw/gold_organisms.tsv` | 303 |
| `data/taxa/bacteria/capnocytophaga_ochracea.yaml` | 1, 42, 67, 74, 109, and 2865 |

- The exact-ID scan also found `Capnocytophaga ochracea DSM 7271`, `Capnocytophaga ochracea F0287`, `Capnocytophaga ochracea str. Holt 25`, and `Capnocytophaga ochracea HMP_JCVI_SC0240` generated as descendant strain records under `NCBITaxon:1018`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/capnocytophaga_ochracea.yaml` directly.
