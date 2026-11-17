# YAML Record Review: Acetitomaculum ruminis

## Target

- File: `data/taxa/bacteria/acetitomaculum_ruminis.yaml`
- Identifier: `NCBITaxon:2382`
- PATHS.tsv row: 340334
- Label: `Acetitomaculum ruminis`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:31980` (`Acetitomaculum`)

## Validation

- `just validate data/taxa/bacteria/acetitomaculum_ruminis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetitomaculum_ruminis.yaml data/taxa/bacteria/acetitomaculum_ruminis_dsm_5522.yaml data/taxa/bacteria/acetitomaculum_sp.yaml data/taxa/bacteria/acetivibrio_aldrichii.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the NCBI taxon `Acetitomaculum ruminis`.
- `data/raw/ncbitaxon_taxa.tsv` line 1879 pins `NCBITaxon:2382` to label `Acetitomaculum ruminis`, rank `SPECIES`, parent `NCBITaxon:31980`, genetic code 11, the NCBI related synonym `Acetitomaculum ruminis Greening and Leedle 1995`, source set `ncbitaxon|lpsn|gold|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place `NCBITaxon:31980` under Lachnospiraceae, Lachnospirales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` line 14790 supports the LPSN nomenclature block, the legitimate and validly published correct-name status, the `lpsn:772479` xref, the `GTDB:s__Acetitomaculum_ruminis` cross-reference, ATCC 43876 and DSM 5522 type-strain designations, and the `INSDC:M59083` sequence accession.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetitomaculum_ruminis`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 23341 keeps this taxon in scope as `attested rule: Acetitomaculum ruminis, 4 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 6222 ties BacDive strain `bacdive:6338` to child strain taxon `NCBITaxon:1120918`, LPSN name `lpsn:772479`, and collection IDs ATCC 43876 and DSM 5522; the YAML preserves the child filing through `classified_as: NCBITaxon:1120918`.
- The local genome and strain links for `bacdive:6338`, `patric:1120918.3`, `gold:Ga0104376`, `gold:Go0013856`, `gold:Gp0127372`, `gtdb.genome:RS_GCF_900112085.1`, and `SAMN05216249` support the assembly, genome, AllTheBacteria, BioProject, BioSample, and GOLD related records for DSM 5522.
- `data/raw/strain_related_records.tsv` lines 401013-401014 support the direct `gold:Go0622856` GOLD organism rows filed at `NCBITaxon:2382` for ATCC 43876.
- `data/raw/ncbi_type_material.tsv` lines 93938-93943 list the NCBI type-material variants for ATCC 43876, DSM 5522, and strain 139B, all consistent with the BacDive/LPSN type-strain identity.
- The StrainInfo strain `straininfo.strain:46854` and deposits `straininfo.deposit:113253` and `straininfo.deposit:113254` support the ATCC 43876 and DSM 5522 deposit related records, the `INSDC:HM043967` and `INSDC:M59083` sequence rows, and the StrainInfo assembly for `GCA_900112085`.

## Completeness

- NCBITAXON, LPSN, BACDIVE, GOLD, and MADIN attestations are represented with their local counts and with explicit notes where descendant BacDive rows are rolled up or direct GOLD/MADIN rows are counted.
- The sole BacDive strain, known collection IDs, local genome records, related projects/samples, ATB assembly `atb.assembly:202505.SAMN05216249`, and same-strain StrainInfo records are carried through.
- The GTDB species is present as the LPSN cross-reference `GTDB:s__Acetitomaculum_ruminis`; the separate GTDB mapping inventory maps that species to the child strain `NCBITaxon:1120918`, so the species-level record appropriately does not assert a direct `taxonomy_mappings` row.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
