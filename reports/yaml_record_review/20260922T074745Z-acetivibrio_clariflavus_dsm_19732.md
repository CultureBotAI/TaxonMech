# YAML Record Review: Acetivibrio clariflavus DSM 19732

## Target

- File: `data/taxa/bacteria/acetivibrio_clariflavus_dsm_19732.yaml`
- Identifier: `NCBITaxon:720554`
- PATHS.tsv row: 580583
- Label: `Acetivibrio clariflavus DSM 19732`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:288965` (`Acetivibrio clariflavus`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_clariflavus_dsm_19732.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_clariflavus.yaml data/taxa/bacteria/acetivibrio_clariflavus_4_2a.yaml data/taxa/bacteria/acetivibrio_clariflavus_dsm_19732.yaml data/taxa/bacteria/acetivibrio_ethanolgignens.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon under `Acetivibrio clariflavus`.
- `data/raw/ncbitaxon_taxa.tsv` line 169536 pins `NCBITaxon:720554` to label `Acetivibrio clariflavus DSM 19732`, rank `STRAIN`, parent `NCBITaxon:288965`, genetic code 11, exact NCBI strain synonyms for the older `Clostridium` and `Hungateiclostridium` combinations, source set `ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio clariflavus`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/gtdb_species.tsv` line 3277 and `data/raw/gtdb_mappings.tsv` line 305132 support the six-genome `GTDB:s__Acetivibrio_clariflavus` `skos:closeMatch` mapping to `NCBITaxon:720554`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_clariflavus_dsm_19732`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 6929 keeps this taxon in scope as `attested rule: Acetivibrio clariflavus DSM 19732, 7 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 2753 ties `bacdive:2853` directly to `NCBITaxon:720554`, LPSN name `lpsn:5949`, designation `EBR-02E-0045`, and collection IDs DSM 19732, EBR 45, and NBRC 101661.
- `data/raw/ncbi_type_material.tsv` lines 136816-136823 list the DSM 19732, NBRC 101661, EBR-02E-0045, and EBR45 type-material variants.
- `data/raw/strain_assemblies.tsv` lines 118859-118866, `data/raw/strain_genome_records.tsv` lines 95553-95558, and `data/atb/assemblies.tsv` line 2574 support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, StrainInfo, and AllTheBacteria genome evidence.
- `data/atb/strain_links.tsv` line 4037 and `data/atb/genome_links.tsv` lines 17626-17630 support the AllTheBacteria BioSample `SAMN02261428`, run `SRR3927407`, and ENA analysis `ERZ4066522` links.
- `data/raw/strain_related_records.tsv` lines 343146-343165 support the BioProject, BioSample, GOLD, INSDC, and StrainInfo related records carried by the BacDive strain.
- `data/straininfo/strain_links.tsv` lines 84799-84800 support the NBRC 101661 and DSM 19732 StrainInfo deposits projected under `straininfo.strain:308309`.

## Completeness

- NCBITAXON, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The `GTDB:s__Acetivibrio_clariflavus` mapping and older NCBI strain synonyms are present, and the parent species carries the corresponding LPSN nomenclatural rows.
- The DSM 19732 BacDive strain is represented with its culture-collection IDs, local genome assemblies, local genome records, AllTheBacteria metadata, GOLD/INSDC/NCBI project records, and StrainInfo deposits.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
