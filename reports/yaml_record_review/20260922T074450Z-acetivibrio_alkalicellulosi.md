# YAML Record Review: Acetivibrio alkalicellulosi

## Target

- File: `data/taxa/bacteria/acetivibrio_alkalicellulosi.yaml`
- Identifier: `NCBITaxon:320502`
- PATHS.tsv row: 436048
- Label: `Acetivibrio alkalicellulosi`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:35829` (`Acetivibrio`)

## Validation

- `just validate data/taxa/bacteria/acetivibrio_alkalicellulosi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/bacteria/acetivibrio_alkalicellulosi.yaml data/taxa/bacteria/acetivibrio_alkalicellulosi_dsm_17461.yaml data/taxa/bacteria/acetivibrio_cellulolyticus.yaml data/taxa/bacteria/acetivibrio_cellulolyticus_cd2.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows.
- `just validate-history` was skipped because this review is read-only and does not add a `history/` entry.
- `just verify-corpus` was skipped because a neighboring YAML review already recorded a clean full-corpus verification over 625,960 records.
- `just validate-products` is not applicable because this record has no `causal_graphs`.

## Identity and Grounding

- The record is an `EXACT` / `SEEDED` bacterial species for the validly published correct name `Acetivibrio alkalicellulosi`.
- `data/raw/ncbitaxon_taxa.tsv` line 65565 pins `NCBITaxon:320502` to label `Acetivibrio alkalicellulosi`, rank `SPECIES`, parent `NCBITaxon:35829`, genetic code 11, exact synonyms `Clostridium alkalicellulosi corrig. Zhilina et al. 2006` and `Hungateiclostridium alkalicellulosi`, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, and NCBI snapshot `2026-09-13`.
- The raw parent rows place `NCBITaxon:320502` under `Acetivibrio`, Acetivibrionaceae, Acetivibrionales, Clostridia, Bacillota, Bacillati, and Bacteria, matching the YAML lineage.
- `data/raw/lpsn_names.tsv` lines 1113, 16228, and 33486 support the correct-name LPSN block for `lpsn:5943` and the LPSN synonym rows for `Clostridium alkalicellulosi` and `Hungateiclostridium alkalicellulosi`.

## Evidence

- Exact `find` probes under `reports/yaml_record_review` found no existing report for `acetivibrio_alkalicellulosi`; `find` includes ignored report files.
- `curation/seed_scope.tsv` line 21288 keeps this taxon in scope as `attested rule: Acetivibrio alkalicellulosi, 5 sources incl. NCBI`.
- `data/raw/gtdb_species.tsv` line 73940 and `data/raw/gtdb_mappings.tsv` line 267744 support the one-genome `GTDB:s__Herbivorax_alkalicellulosi` `skos:closeMatch` mapping to `NCBITaxon:320502` and the GTDB-sourced exact synonym `Herbivorax alkalicellulosi`.
- `data/raw/bacdive_strains.tsv` line 2738 ties BacDive strain `bacdive:2838` to child strain taxon `NCBITaxon:1002220`, LPSN name `lpsn:5943`, and DSM 17461 / VKM B-2349 collection IDs; the YAML preserves the child filing through `classified_as: NCBITaxon:1002220`.
- `data/raw/strain_assemblies.tsv` lines 118739-118746 and `data/raw/strain_genome_records.tsv` lines 95454-95460 support the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo assembly/genome rows for DSM 17461.
- `data/raw/strain_related_records.tsv` lines 342818-342837 support the BV-BRC, GOLD, GTDB, NCBI Assembly, GOLD organism, and GOLD project related records for DSM 17461 and VKM B-2349.
- `data/straininfo/assemblies.tsv` line 8674 and `data/straininfo/strain_links.tsv` lines 84758-84759 support the StrainInfo assembly and deposit links for DSM 17461 and VKM B-2349.

## Completeness

- NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN attestations are represented with the expected local counts.
- The only BacDive strain found for this LPSN species is represented, and its local BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo genome/related-record trail is carried through.
- The gitignore-independent bounded exact-ID/source-ID scan across `data/raw`, `data/atb`, and `data/straininfo` found no same-strain AllTheBacteria rows for `bacdive:2838`, `GCA_008125075`, or `SAMN01163580`, so the empty ATB surface is consistent with the source evidence.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source used for this review because live NCBI lookup was unavailable in this environment.
- `data/taxa/` is generated; future changes, if any, should be made in source extraction or seeding logic rather than by editing this YAML directly.
