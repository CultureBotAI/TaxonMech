# YAML Record Review: Desulfovibrio inopinatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/desulfovibrio_inopinatus.yaml
- Started UTC: 2026-10-02T12:34:23Z
- Finished UTC: 2026-10-02T12:34:23Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102109` |
| Label | `Desulfovibrio inopinatus` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:872` |
| Parent label | `Desulfovibrio` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Nomenclature | `lpsn:775689` |
| Strains | 1 BacDive strain entry |
| Source attestations | `NCBITAXON`, `LPSN`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/desulfovibrio_inopinatus.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/uncultured_eubacterium_wjgrt_214.yaml data/taxa/bacteria/uncultured_eubacterium_wjgrt_217.yaml data/taxa/bacteria/desulfovibrio_inopinatus.yaml data/taxa/bacteria/delta_proteobacterium_s2551.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 506 lines, 9 lineage entries, 1 nomenclature entry, 1 synonym, 1 xref, 1 declared strain, and 5 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI, LPSN, BacDive, GOLD, MADIN, type-material, StrainInfo, genome, and related-record rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102099\|102100\|102109\|102110)([^0-9]\|$)' data curation` | Pass: found the generated species YAML plus expected descendant strain references; no competing `NCBITaxon:102109` identity record was present. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the multi-source species rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10509 maps `NCBITaxon:102109` to `desulfovibrio_inopinatus`.
- `curation/seed_scope.tsv` row 23612 keeps this taxon in scope with a four-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17805 names `NCBITaxon:102109` as `Desulfovibrio inopinatus`, with species rank, `Desulfovibrio` parent `NCBITaxon:872`, genetic code 11, and one NCBI synonym.
- The generated YAML line 1 preserves the exact NCBI identifier; lines 7-33 preserve the 9-row NCBI lineage ending at `NCBITaxon:872`.
- `data/raw/lpsn_names.tsv` row 16780 maps `lpsn:775689` to this species, flags it as validly published, legitimate, and the correct name, and links the LPSN name to `NCBITaxon:102109`.
- `data/raw/bacdive_strains.tsv` row 4030 maps `kgmicrobe.strain:bacdive_4134` / `bacdive:4134` to descendant `NCBITaxon:1121453` with `DSM-10711` and `HHQ%2020` culture identifiers.

## Evidence

- The NCBI row supports the YAML identifier, label, rank, parent, genetic code, and authority synonym.
- The LPSN row supports the nomenclature block, `lpsn:775689` xref, `kgmicrobe.strain:DSM-10711` type-strain designation, three publication identifiers, and `INSDC:AF177276`.
- The BacDive row accounts for the single top-level BacDive type-strain entry and keeps it safely scoped to descendant `NCBITaxon:1121453`.
- `data/raw/strain_assemblies.tsv` rows 124921-124928 and `data/raw/strain_genome_records.tsv` rows 100392-100397 account for the nested BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly genome entries under `kgmicrobe.strain:bacdive_4134`.
- `data/raw/strain_related_records.tsv` rows 360290-360307 account for the nested BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related records.
- `data/straininfo/assemblies.tsv` row 9261 and `data/straininfo/strain_links.tsv` row 88494 account for the StrainInfo assembly, deposit, and strain records linked to `DSM 10711`.
- The GOLD and MADIN source attestation counts match their exact aggregate rows: 1 GOLD organism and 3 MADIN trait assertions.

## Completeness

- The record is complete for the exact NCBI, LPSN, BacDive, GOLD, MADIN, type-material, genome, related-record, and StrainInfo inputs currently present for this species.
- BacDive, GOLD, GTDB, NCBI Assembly, BV-BRC, and StrainInfo nested rows stay scoped to `kgmicrobe.strain:bacdive_4134` and its descendant `NCBITaxon:1121453` classification.
- `taxonomy_mappings` is absent because no top-level GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102109`.
- This review did not infer additional strain entries, top-level genome records, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/desulfovibrio_inopinatus.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/desulfovibrio_inopinatus.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:102109`, `lpsn:775689`, and `kgmicrobe.strain:bacdive_4134` after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10509 |
| `curation/seed_scope.tsv` | 23612 |
| `data/raw/ncbitaxon_taxa.tsv` | 17805 |
| `data/raw/lpsn_names.tsv` | 16780 |
| `data/raw/bacdive_strains.tsv` | 4030 |
| `data/raw/gold_organisms.tsv` | 310 |
| `data/raw/madin_taxa.tsv` | 482 |
| `data/straininfo/assemblies.tsv` | 9261 |
| `data/straininfo/strain_links.tsv` | 88494 |
| `data/taxa/bacteria/desulfovibrio_inopinatus.yaml` | 1, 36, 56, 60, 64, and 469 |

- The exact-ID scan also found the generated `Desulfovibrio inopinatus DSM 10711` strain record under `NCBITaxon:102109`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/desulfovibrio_inopinatus.yaml` directly.
