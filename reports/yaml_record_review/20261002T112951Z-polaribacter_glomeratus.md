# YAML Record Review: Polaribacter glomeratus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/polaribacter_glomeratus.yaml
- Started UTC: 2026-10-02T11:29:51Z
- Finished UTC: 2026-10-02T11:29:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102` |
| Label | `Polaribacter glomeratus` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:52959` |
| Parent label | `Polaribacter` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Nomenclature | `lpsn:784649` |
| GTDB mapping | `GTDB:s__Polaribacter_glomeratus` |
| Strains | 1 BacDive strain entry |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/polaribacter_glomeratus.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/ehrlichia_sp_cate.yaml data/taxa/bacteria/polaribacter_glomeratus.yaml data/taxa/bacteria/uncultured_eubacterium_wjgrt_1.yaml data/taxa/bacteria/uncultured_eubacterium_wjgrt_2.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 671 lines, 11 lineage entries, 4 synonyms, 2 xrefs, 1 declared strain, 1 taxonomy mapping, and 6 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI, LPSN, GTDB, BacDive, GOLD, MADIN, type-material, and StrainInfo rows. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*polaribacter_glomeratus.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(101949\|102\|102005\|102006)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to source rows, `PATHS.tsv`, `seed_scope.tsv`, and the generated YAMLs. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the multi-source species rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10412 maps `NCBITaxon:102` to `polaribacter_glomeratus`.
- `curation/seed_scope.tsv` row 9138 keeps this taxon in scope with a six-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 76 names `NCBITaxon:102` as `Polaribacter glomeratus`, with species rank, `Polaribacter` parent `NCBITaxon:52959`, genetic code 11, and three NCBI synonyms.
- The generated YAML line 1 preserves the exact NCBI identifier; lines 7-39 preserve the 11-row NCBI lineage ending at `NCBITaxon:52959`.
- `data/raw/lpsn_names.tsv` row 22676 maps `lpsn:784649` to this species, flags it as validly published, legitimate, and the correct name, and links the LPSN name to `NCBITaxon:102`.
- `data/raw/gtdb_mappings.tsv` row 1186 maps `GTDB:s__Polaribacter_glomeratus` to `NCBITaxon:102` with `skos:closeMatch`, and `data/raw/gtdb_species.tsv` row 141923 reports 2 genomes for that GTDB species.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, exact synonym, and two related synonyms.
- The LPSN rows support the nomenclature block, `lpsn:784649` xref, `Flectobacillus glomeratus` LPSN synonym, three listed type-strain designations, three publication identifiers, and `INSDC:M58775`.
- The GTDB rows support the `skos:closeMatch` taxonomy mapping and the 2-genome source attestation.
- The `data/raw/bacdive_strains.tsv` row for `bacdive_136694` accounts for the single top-level BacDive type-strain entry, including `ACAM 171`, `ATCC 43844`, and `CIP 103112` culture-collection IDs.
- The GOLD and MADIN source attestation counts match their exact aggregate rows: 2 GOLD organisms and 3 MADIN trait assertions.

## Completeness

- The record is complete for the exact NCBI, LPSN, GTDB, BacDive, GOLD, MADIN, type-material, and StrainInfo inputs currently present for this species.
- The BacDive, GOLD, GTDB, NCBI Assembly, BV-BRC, and StrainInfo nested rows stay scoped to the `bacdive_136694` type strain and its ATCC/CIP culture identifiers.
- This review did not infer additional strain entries, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/polaribacter_glomeratus.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/polaribacter_glomeratus.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:102`, `lpsn:784649`, and `GTDB:s__Polaribacter_glomeratus` after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10412 |
| `curation/seed_scope.tsv` | 9138 |
| `data/raw/ncbitaxon_taxa.tsv` | 76 |
| `data/raw/lpsn_names.tsv` | 22676 |
| `data/raw/gtdb_mappings.tsv` | 1186 |
| `data/raw/gtdb_species.tsv` | 141923 |
| `data/raw/bacdive_strains.tsv` | 58999 |
| `data/raw/gold_organisms.tsv` | 307 |
| `data/raw/madin_taxa.tsv` | 481 |
| `data/taxa/bacteria/polaribacter_glomeratus.yaml` | 1, 42, 64, 71, 90, and 631 |

- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/polaribacter_glomeratus.yaml` directly.
