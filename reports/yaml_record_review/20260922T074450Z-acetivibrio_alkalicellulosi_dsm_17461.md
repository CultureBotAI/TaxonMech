# YAML Record Review: Acetivibrio alkalicellulosi DSM 17461

## Target

- File: `data/taxa/bacteria/acetivibrio_alkalicellulosi_dsm_17461.yaml`
- Identifier: `NCBITaxon:1002220`
- PATHS.tsv row: 678
- Label: `Acetivibrio alkalicellulosi DSM 17461`
- Rank/domain: `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:320502` (`Acetivibrio alkalicellulosi`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_alkalicellulosi_dsm_17461.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_alkalicellulosi.yaml data/taxa/bacteria/acetivibrio_alkalicellulosi_dsm_17461.yaml data/taxa/bacteria/acetivibrio_cellulolyticus.yaml data/taxa/bacteria/acetivibrio_cellulolyticus_cd2.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial strain taxon for `Acetivibrio alkalicellulosi DSM 17461`.
- `data/raw/ncbitaxon_taxa.tsv` line 209384 pins `NCBITaxon:1002220` to label `Acetivibrio alkalicellulosi DSM 17461`, rank `STRAIN`, parent `NCBITaxon:320502`, genetic code 11, exact strain synonyms from NCBI, source set `ncbitaxon|bacdive|mediadive|bactotraits`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place the strain below `Acetivibrio alkalicellulosi`, `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_alkalicellulosi_dsm_17461`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 22126 keeps this taxon in scope as `attested rule: Acetivibrio alkalicellulosi DSM 17461, 4 sources incl. NCBI`.
- `data/raw/bacdive_strains.tsv` line 2738 ties `bacdive:2838` directly to `NCBITaxon:1002220`, `lpsn:5943`, designation `Z-7026`, and collection IDs DSM 17461 and VKM B-2349.
- `data/raw/strain_assemblies.tsv` lines 118739-118746 and `data/raw/strain_genome_records.tsv` lines 95454-95460 support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo assembly/genome rows retained under this strain record by DSM 17461 identity.
- `data/raw/strain_related_records.tsv` lines 342818-342837 support the BioProject `PRJNA65293`, BioSample `SAMN01163580`, GOLD analysis `Ga0025046`, GOLD organisms `Go0003903` and `Go0628911`, and GOLD project `Gp0003903`.
- `data/straininfo/strain_links.tsv` lines 84758-84759 support both projected StrainInfo deposits under `straininfo.strain:291125`, including the DSM 17461 deposit filed at `NCBITaxon:320502` and the VKM B-2349 deposit linked by the same BacDive strain.

## Completeness

- NCBITAXON, BACDIVE, MEDIADIVE, and BACTOTRAITS attestations are represented with the expected assertion units and counts.
- The strain synonyms, BacDive strain, collection IDs, genome assemblies, genome IDs, GOLD/BV-BRC/GTDB/NCBI Assembly related records, and StrainInfo deposit rows all trace to `bacdive:2838` or to a DSM 17461 culture-identifier match.
- The GTDB genome evidence is present as genome support for DSM 17461, while the one local GTDB species mapping targets the parent species `NCBITaxon:320502`; the strain record therefore appropriately omits a `taxonomy_mappings` block.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
