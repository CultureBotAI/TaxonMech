# YAML Record Review: Acetivibrio mesophilus

## Target

- File: `data/taxa/bacteria/acetivibrio_mesophilus.yaml`
- Identifier: `NCBITaxon:2487273`
- PATHS.tsv row: 343381
- Label: `Acetivibrio mesophilus`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_mesophilus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_mesophilus.yaml data/taxa/bacteria/acetivibrio_saccincola.yaml data/taxa/bacteria/acetivibrio_sp.yaml data/taxa/bacteria/acetivibrio_sp_6_13.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio mesophilus`.
- `data/raw/ncbitaxon_taxa.tsv` line 526345 pins `NCBITaxon:2487273` to label `Acetivibrio mesophilus`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, exact synonym `Hungateiclostridium mesophilum`, related synonyms for the Acetivibrio and Hungateiclostridium authority strings plus strain N2K1, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the species below `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` lines 764-765 support the LPSN correct name `lpsn:5587`, the `Hungateiclostridium mesophilum` synonym row, type-strain designation DSM 107956, sequence accession `INSDC:MK138666`, and the synonym-side `GTDB:s__Hungateiclostridium_mesophilum` xref.
- `data/raw/gtdb_species.tsv` line 74471 and `data/raw/gtdb_mappings.tsv` line 193481 support the five-genome `GTDB:s__Hungateiclostridium_mesophilum` `skos:closeMatch` mapping to `NCBITaxon:2487273`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_mesophilus`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 13117 keeps this taxon in scope as `attested rule: Acetivibrio mesophilus, 6 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 80211 ties `bacdive:157972` directly to `NCBITaxon:2487273`, LPSN name `lpsn:5587`, designation N2K1, and collection IDs CECT 9704 and DSM 107956.
- `data/raw/ncbi_type_material.tsv` lines 96517-96522 list the CECT 9704, DSM 107956, and N2K1 type-material variants.
- `data/raw/strain_assemblies.tsv` lines 64972-64974 and `data/raw/strain_genome_records.tsv` lines 50126-50129 support the BacDive, BV-BRC, and GOLD assembly and genome rows for N2K1 / DSM 107956.
- `data/atb/assemblies.tsv` line 6314, `data/atb/strain_links.tsv` line 2285, and `data/atb/genome_links.tsv` lines 9699-9701 support `atb.assembly:202505.SAMN10395150`, run `SRR8752195`, ENA analysis `ERZ25504871`, and the BV-BRC/GOLD sample links.
- `data/raw/strain_related_records.tsv` lines 205171-205181 support the BioProject `PRJNA504010`, BioSample `SAMN10395150`, GOLD analysis `Ga0442409`, GOLD organisms `Go0146500`, `Go0621948`, `Go0621949`, GOLD project `Gp0495217`, and StrainInfo related records.
- `data/straininfo/strain_links.tsv` line 56842 supports the DSM 107956 StrainInfo deposit projected under `straininfo.strain:402063`.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, and GOLD attestations are represented with the expected assertion units and counts.
- The LPSN correct/synonym names, NCBI exact/related synonyms, and GTDB `Hungateiclostridium` species mapping are present.
- The BacDive type strain is represented with its CECT/DSM collection identifiers, BacDive/BV-BRC/GOLD genome evidence, AllTheBacteria metadata, GOLD project/sample/analysis/organism records, and StrainInfo deposit rows.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
