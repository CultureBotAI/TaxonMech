# YAML Record Review: Acetivibrio saccincola

## Target

- File: `data/taxa/bacteria/acetivibrio_saccincola.yaml`
- Identifier: `NCBITaxon:1677857`
- PATHS.tsv row: 243492
- Label: `Acetivibrio saccincola`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_saccincola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_mesophilus.yaml data/taxa/bacteria/acetivibrio_saccincola.yaml data/taxa/bacteria/acetivibrio_sp.yaml data/taxa/bacteria/acetivibrio_sp_6_13.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio saccincola`.
- `data/raw/ncbitaxon_taxa.tsv` line 437748 pins `NCBITaxon:1677857` to label `Acetivibrio saccincola`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, NCBI exact synonyms for `Herbivorax saccincola` and `Hungateiclostridium saccincola`, related synonyms for authority strings and strains GGR1/A7, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the species below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` lines 1159, 31289, and 33877 support the LPSN correct name `lpsn:5991`, the `Herbivorax saccincola` and `Hungateiclostridium saccincola` synonym rows, type-strain designation DSM 101079, sequence accession `INSDC:LN868252`, and the synonym-side `GTDB:s__Herbivorax_saccincola` xref.
- `data/raw/gtdb_species.tsv` line 73941 and `data/raw/gtdb_mappings.tsv` line 48658 support the eight-genome `GTDB:s__Herbivorax_saccincola` `skos:closeMatch` mapping to `NCBITaxon:1677857`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_saccincola`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 1586 keeps this taxon in scope as `attested rule: Acetivibrio saccincola, 8 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` lines 54990 and 86368 support the GGR1 / DSM 101079 type strain and the JCM 31827 / DSM 104321 strain.
- `data/raw/ncbi_type_material.tsv` lines 51495-51500 list the CECT 9155, DSM 101079, and GGR1 type-material variants.
- `data/raw/strain_assemblies.tsv` lines 25881-25883 and 77747-77748 support the BacDive, BV-BRC, and GOLD assembly rows for GGR1 plus the BacDive and BV-BRC assembly rows for A7.
- `data/raw/strain_genome_records.tsv` lines 20659-20662 and 60379-60380 support the BacDive, GOLD, and BV-BRC genome rows for both local BacDive strains.
- `data/raw/strain_related_records.tsv` lines 71819-71829 support the GGR1 BioProject, BioSample, GOLD analysis, GOLD organisms, GOLD project, and StrainInfo related records; lines 238817-238818 support the A7 BioProject and BioSample rows.
- `data/straininfo/strain_links.tsv` line 13789 supports the DSM 101079 StrainInfo deposit projected under `straininfo.strain:396620`.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The LPSN correct/synonym names, NCBI exact/related synonyms, and GTDB `Herbivorax` species mapping are present.
- Both BacDive strains are represented: GGR1 carries the type-strain genome, GOLD, and StrainInfo evidence, and A7 carries its BacDive/BV-BRC genome and project/sample evidence.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
