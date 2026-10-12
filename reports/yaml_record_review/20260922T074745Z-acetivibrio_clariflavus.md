# YAML Record Review: Acetivibrio clariflavus

## Target

- File: `data/taxa/bacteria/acetivibrio_clariflavus.yaml`
- Identifier: `NCBITaxon:288965`
- PATHS.tsv row: 388990
- Label: `Acetivibrio clariflavus`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_clariflavus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_clariflavus.yaml data/taxa/bacteria/acetivibrio_clariflavus_4_2a.yaml data/taxa/bacteria/acetivibrio_clariflavus_dsm_19732.yaml data/taxa/bacteria/acetivibrio_ethanolgignens.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio clariflavus`.
- `data/raw/ncbitaxon_taxa.tsv` line 58955 pins `NCBITaxon:288965` to label `Acetivibrio clariflavus`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, NCBI exact synonyms for `Clostridium clariflavum` and `Hungateiclostridium clariflavum`, related synonyms including the NCBI authority strings, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the species below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` lines 1119, 25159, and 33491 support the LPSN correct name `lpsn:5949`, the `Clostridium clariflavum` and `Hungateiclostridium clariflavum` synonym rows, type-strain designations DSM 19732 and NBRC 101661, sequence accession `INSDC:AB186359`, and the `GTDB:s__Acetivibrio_clariflavus` xref.
- `data/raw/gtdb_species.tsv` line 3277 and `data/raw/gtdb_mappings.tsv` line 229246 support the six-genome `GTDB:s__Acetivibrio_clariflavus` `skos:closeMatch` mapping to `NCBITaxon:288965`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_clariflavus`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 21257 keeps this taxon in scope as `attested rule: Acetivibrio clariflavus, 5 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 2753 ties `bacdive:2853` to LPSN name `lpsn:5949`, child taxon `NCBITaxon:720554`, designation `EBR-02E-0045`, collection IDs DSM 19732, EBR 45, and NBRC 101661, and the YAML records this as a type strain classified as the DSM 19732 child.
- `data/raw/ncbi_type_material.tsv` lines 136816-136823 list the DSM 19732, NBRC 101661, EBR-02E-0045, and EBR45 type-material variants.
- `data/raw/strain_assemblies.tsv` lines 118859-118866, `data/raw/strain_genome_records.tsv` lines 95553-95558, and `data/atb/assemblies.tsv` line 2574 support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, StrainInfo, and AllTheBacteria genome evidence projected from the DSM 19732 strain.
- `data/atb/strain_links.tsv` line 4037 and `data/atb/genome_links.tsv` lines 17626-17630 support the AllTheBacteria BioSample `SAMN02261428`, run `SRR3927407`, and ENA analysis `ERZ4066522` links.
- `data/raw/strain_related_records.tsv` lines 343146-343165 support the BioProject, BioSample, GOLD, INSDC, and StrainInfo related records carried by the DSM 19732 BacDive strain.
- `data/straininfo/strain_links.tsv` lines 84799-84800 support the NBRC 101661 and DSM 19732 StrainInfo deposits projected under `straininfo.strain:308309`.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN attestations are represented with the expected assertion units and counts, including direct-only notes for GOLD and MADIN and a descendant note for the BacDive type strain.
- The correct LPSN name, LPSN synonym rows, GTDB species xref, GTDB taxonomy mapping, and NCBI exact/related synonyms are all present.
- The DSM 19732 type-strain child evidence is represented with BacDive, culture-collection IDs, local genome assemblies, local genome records, AllTheBacteria metadata, GOLD/INSDC/NCBI project records, and StrainInfo deposits.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
