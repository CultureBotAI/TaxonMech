# YAML Record Review: Desulfoscipio gibsoniae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/desulfoscipio_gibsoniae.yaml
- Started UTC: 2026-10-02T12:45:50Z
- Finished UTC: 2026-10-02T12:45:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102134` |
| Label | `Desulfoscipio gibsoniae` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2867376` |
| Parent label | `Desulfoscipio` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Nomenclature | `lpsn:17701` |
| Strains | 1 BacDive strain entry |
| Source attestations | `NCBITAXON`, `LPSN`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/desulfoscipio_gibsoniae.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/leptolyngbya_sp_pcc_73110.yaml data/taxa/bacteria/leptolyngbya_sp_pcc_7375.yaml data/taxa/bacteria/pseudanabaena_sp_pcc_7402.yaml data/taxa/bacteria/desulfoscipio_gibsoniae.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 782 lines, 9 lineage entries, 7 synonyms, 1 xref, 1 declared strain, and 5 source attestations. |
| Direct raw-source scans for this YAML | Pass: found the expected NCBI, LPSN, BacDive, GOLD, MADIN, type-material, merge, StrainInfo, AllTheBacteria, genome, and related-record rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102128\|102129\|102130\|102134)([^0-9]\|$)' data curation` | Pass: found the generated species YAML plus the expected descendant strain references; no competing `NCBITaxon:102134` identity record was present. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper exited with `NCBI source mismatch` on the multi-source species rollup, so direct source-table scans were used instead. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10526 maps `NCBITaxon:102134` to `desulfoscipio_gibsoniae`.
- `curation/seed_scope.tsv` row 23614 keeps this taxon in scope with a four-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17823 names `NCBITaxon:102134` as `Desulfoscipio gibsoniae`, with species rank, `Desulfoscipio` parent `NCBITaxon:2867376`, genetic code 11, three NCBI exact synonyms, and two NCBI related synonyms.
- `data/raw/lpsn_names.tsv` row 3270 maps `lpsn:17701` to this species, flags it as validly published, legitimate, and the correct name, links the LPSN name to `NCBITaxon:102134`, and records `DSM-7213` plus `NBRC-112754` as type-strain designations.
- `data/raw/bacdive_strains.tsv` row 11671 maps `kgmicrobe.strain:bacdive_11825` / `bacdive:11825` to descendant `NCBITaxon:767817` with `DSM-7213` and `NBRC-112754` culture identifiers.

## Evidence

- The NCBI and LPSN rows support the YAML identifier, label, rank, parent, genetic code, nomenclature block, seven generated synonyms, `lpsn:17701` xref, two publication identifiers, and `INSDC:AJ294431`.
- The BacDive row accounts for the single top-level BacDive type-strain entry and keeps it safely scoped to descendant `NCBITaxon:767817`.
- `data/raw/strain_assemblies.tsv` rows 8412-8420 and `data/raw/strain_genome_records.tsv` rows 6472-6478 account for the nested BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly genome entries under `kgmicrobe.strain:bacdive_11825`.
- `data/atb/assemblies.tsv` row 3094, `data/atb/strain_links.tsv` row 241, and `data/atb/genome_links.tsv` rows 957-961 account for the AllTheBacteria assembly linked through `biosample:SAMN02598540`.
- `data/raw/strain_related_records.tsv` rows 24986-25007 account for the nested BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related records.
- `data/straininfo/assemblies.tsv` row 816, `data/straininfo/strain_links.tsv` row 5857, and `data/straininfo/related_records.tsv.gz` rows 15335-15341 account for the StrainInfo assembly, nucleotide sequence, deposit, and strain records.
- The GOLD and MADIN source attestation counts match their exact aggregate rows: 3 GOLD organisms and 3 MADIN trait assertions.
- `data/raw/ncbi_merged_ids.tsv` row 13644 records the merge from `NCBITaxon:136621` into `NCBITaxon:102134`.

## Completeness

- The record is complete for the exact NCBI, LPSN, BacDive, GOLD, MADIN, NCBI type-material, AllTheBacteria, genome, related-record, and StrainInfo inputs currently present for this species.
- BacDive, GOLD, GTDB, NCBI Assembly, BV-BRC, StrainInfo, and AllTheBacteria nested rows stay scoped to `kgmicrobe.strain:bacdive_11825` and its descendant `NCBITaxon:767817` classification.
- `taxonomy_mappings` is absent because no top-level GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102134`.
- This review did not infer additional strain entries, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/desulfoscipio_gibsoniae.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/desulfoscipio_gibsoniae.yaml`.
- Re-run `just verify-corpus`.
- Re-run direct source scans for `NCBITaxon:102134`, `lpsn:17701`, `kgmicrobe.strain:bacdive_11825`, and `biosample:SAMN02598540` after any refresh of `data/raw/`, `data/atb/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10526 |
| `curation/seed_scope.tsv` | 23614 |
| `data/raw/ncbitaxon_taxa.tsv` | 17823 |
| `data/raw/lpsn_names.tsv` | 3270 |
| `data/raw/bacdive_strains.tsv` | 11671 |
| `data/raw/gold_organisms.tsv` | 313 |
| `data/raw/madin_taxa.tsv` | 487 |
| `data/atb/assemblies.tsv` | 3094 |
| `data/straininfo/related_records.tsv.gz` | 15335-15341 |
| `data/taxa/bacteria/desulfoscipio_gibsoniae.yaml` | 1, 36, 56, 80, 84, and 745 |

- The exact-ID scan also found the generated `Desulfoscipio gibsoniae DSM 7213` strain record under `NCBITaxon:102134`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/desulfoscipio_gibsoniae.yaml` directly.
