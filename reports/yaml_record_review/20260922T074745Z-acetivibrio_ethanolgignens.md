# YAML Record Review: Acetivibrio ethanolgignens

## Target

- File: `data/taxa/bacteria/acetivibrio_ethanolgignens.yaml`
- Identifier: `NCBITaxon:290052`
- PATHS.tsv row: 389830
- Label: `Acetivibrio ethanolgignens`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_ethanolgignens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_clariflavus.yaml data/taxa/bacteria/acetivibrio_clariflavus_4_2a.yaml data/taxa/bacteria/acetivibrio_clariflavus_dsm_19732.yaml data/taxa/bacteria/acetivibrio_ethanolgignens.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio ethanolgignens`.
- `data/raw/ncbitaxon_taxa.tsv` line 59074 pins `NCBITaxon:290052` to label `Acetivibrio ethanolgignens`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, NCBI exact synonyms for `Acetanaerobacter ethanolgignens` and `Acetivibrio ethanoligignens`, related synonyms for the Acetanaerobacter and Acetivibrio authority strings, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the species below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` line 14792 supports the LPSN correct name `lpsn:772482`, type-strain designations ATCC 33324, DSM 3005, and LMG 7055, sequence accession `INSDC:FR749897`, and the ICNP nomenclatural status.
- `data/raw/gtdb_species.tsv` line 195392 and `data/raw/gtdb_mappings.tsv` line 229928 support the seven-genome `GTDB:s__Velocimicrobium_ethanolgignens` `skos:closeMatch` mapping to `NCBITaxon:290052`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_ethanolgignens`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 2565 keeps this taxon in scope as `attested rule: Acetivibrio ethanolgignens, 8 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 17486 ties `bacdive:17675` directly to `NCBITaxon:290052`, LPSN name `lpsn:772482`, designation `77-6`, and collection IDs ATCC 33324 and DSM 3005.
- `data/raw/ncbi_type_material.tsv` lines 138293-138301 list the ATCC 33324, DSM 3005, LMG 7055, and 77-6 type-material variants.
- `data/raw/strain_related_records.tsv` lines 289825-289831 support the GOLD analysis, GOLD organisms, GOLD project, INSDC 16S sequence, and StrainInfo deposit/strain records for the ATCC 33324 / DSM 3005 type strain.
- `data/straininfo/strain_links.tsv` lines 76879-76880 support the ATCC 33324 and DSM 3005 StrainInfo deposits projected under `straininfo.strain:14535`.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The LPSN correct name, NCBI exact/related synonyms, and GTDB `Velocimicrobium` species mapping are present.
- The BacDive type strain is represented with its ATCC/DSM collection identifiers, GOLD analysis/organism/project related records, the StrainInfo 16S sequence, and both StrainInfo deposits.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
