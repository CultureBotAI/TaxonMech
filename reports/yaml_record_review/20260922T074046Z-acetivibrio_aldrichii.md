# YAML Record Review: Acetivibrio aldrichii

## Target

- File: `data/taxa/bacteria/acetivibrio_aldrichii.yaml`
- Identifier: `NCBITaxon:29353`
- PATHS.tsv row: 394726
- Label: `Acetivibrio aldrichii`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_aldrichii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetitomaculum_ruminis.yaml data/taxa/bacteria/acetitomaculum_ruminis_dsm_5522.yaml data/taxa/bacteria/acetitomaculum_sp.yaml data/taxa/bacteria/acetivibrio_aldrichii.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio aldrichii`.
- `data/raw/ncbitaxon_taxa.tsv` line 3078 pins `NCBITaxon:29353` to label `Acetivibrio aldrichii`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, exact synonyms `Clostridium aldrichii` and `Hungateiclostridium aldrichii`, related authority-bearing synonyms, source set `ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place `NCBITaxon:29353` under `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` lines 1111, 16224, and 33485 support the correct-name LPSN block for `lpsn:5941` and the `Clostridium aldrichii` and `Hungateiclostridium aldrichii` synonym rows retained in the YAML.

## Evidence

- An exact `find` probe under `reports/yaml_record_review` found no existing report for `acetivibrio_aldrichii`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 5604 keeps this taxon in scope as `attested rule: Acetivibrio aldrichii, 7 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 2665 ties `bacdive:2764` to `NCBITaxon:29353`, LPSN name `lpsn:5941`, designation `P-1`, and collection IDs ATCC 49358, DSM 6159, and OCM 112.
- `data/raw/ncbi_type_material.tsv` lines 144116-144125 list the NCBI type-material variants for ATCC 49358, DSM 6159, OCM 112, OGI 112, and strain P-1, consistent with the projected type-strain identity.
- `data/raw/strain_related_records.tsv` lines 340884-340889 support the three matched GOLD organism rows for DSM 6159, OCM 112, and ATCC 49358 under `kgmicrobe.strain:bacdive_2764`.
- `data/straininfo/strain_links.tsv` lines 84555-84556 and the bounded source-ID scan support the StrainInfo strain `straininfo.strain:42437`, ATCC 49358 deposit `straininfo.deposit:114180`, DSM 6159 deposit `straininfo.deposit:159788`, and sequence accessions `INSDC:AY691310` and `INSDC:X71846`.
- The gitignore-independent bounded exact-ID/source-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no GTDB, NCBI Assembly, or AllTheBacteria genome evidence for this NCBI taxon.

## Completeness

- NCBITAXON, LPSN, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and local counts.
- The single BacDive strain, three culture collection IDs, LPSN synonym history, GOLD organism related records, StrainInfo deposit rows, and StrainInfo nucleotide sequence rows are carried through.
- The empty assembly and genome surfaces are consistent with the absence of matched GTDB, NCBI Assembly, and ATB evidence in the scanned local inventories.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
