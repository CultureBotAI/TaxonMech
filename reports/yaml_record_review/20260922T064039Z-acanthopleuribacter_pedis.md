# YAML Record Review: Acanthopleuribacter pedis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acanthopleuribacter_pedis.yaml
- Started UTC: 2026-09-22T06:38:22Z
- Finished UTC: 2026-09-22T06:40:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:442870 |
| label | Acanthopleuribacter pedis |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:442869 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| strain_count | 1 |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/acanthopleuribacter_pedis.yaml`. It carries one LPSN nomenclature entry, one close GTDB species mapping, one NCBI related synonym, one BacDive-derived local strain with culture-collection IDs, NCBI/BV-BRC/GOLD/GTDB assembly and genome links, 23 related records, and source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS. It has no curator-added `causal_graphs`.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 506048 maps `NCBITaxon:442870` to slug `acanthopleuribacter_pedis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -type f -name "????????T??????Z-acanthopleuribacter_pedis.md" -print` returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acanthopleuribacter_pedis.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acalypha_indica_phytoplasma.yaml data/taxa/bacteria/acanthopleuribacter_pedis.yaml data/taxa/bacteria/acanthopleuribacter_sp.yaml data/taxa/bacteria/acanthopleuribacteraceae_bacterium.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 98281 has `NCBITaxon:442870`, label `Acanthopleuribacter pedis`, rank `SPECIES`, direct parent `NCBITaxon:442869`, NCBI related synonym `Acanthopleuribacter pedis Fukunaga et al. 2008`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:57723` Acidobacteriota, `PHYLUM` | line 7341 |
| `NCBITaxon:533205` Holophagae, `CLASS` | line 122075 |
| `NCBITaxon:533206` Acanthopleuribacterales, `ORDER` | line 122076 |
| `NCBITaxon:533207` Acanthopleuribacteraceae, `FAMILY` | line 122077 |
| `NCBITaxon:442869` Acanthopleuribacter, `GENUS` | line 98280 |

`data/raw/lpsn_names.tsv` line 24799 maps `lpsn:787601` to `Acanthopleuribacter pedis`, its LPSN parent `lpsn:517824`, `NCBITaxon:442870`, `GTDB:s__Acanthopleuribacter_pedis`, three LPSN type-strain designations, the two DOI references plus `PMID:18984699`, and `INSDC:AB303221`. `data/raw/gtdb_mappings.tsv` line 289682 maps `GTDB:s__Acanthopleuribacter_pedis` to this NCBI species with `skos:closeMatch` and `genome_count` 1; `data/raw/gtdb_species.tsv` line 2848 carries the same native GTDB species and count.

`curation/seed_scope.tsv` line 3103 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, related synonym, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 98281 | Supported exactly. |
| LPSN nomenclature and `lpsn:787601` xref | `data/raw/lpsn_names.tsv` line 24799 | Supported exactly, including species rank, authority, status flags, URL, type-strain designations, publications, `INSDC:AB303221`, and the linked GTDB species. |
| GTDB taxonomy mapping and `GTDB:s__Acanthopleuribacter_pedis` xref | `data/raw/gtdb_mappings.tsv` line 289682 and `data/raw/gtdb_species.tsv` line 2848 | Supported exactly with `skos:closeMatch` and one GTDB genome. |
| BacDive local strain `kgmicrobe.strain:bacdive_24718` | `data/raw/bacdive_strains.tsv` line 24275 and the native `data/bacdive/records.jsonl.gz` record for BacDive ID 24718 | Supported exactly: strain FYK2218, `bacdive:24718`, taxon `NCBITaxon:442870`, LPSN `lpsn:787601`, culture IDs DSM 28897/KCTC 12899/NBRC 101209, and type-strain flag `yes`. |
| Culture-collection IDs | `data/raw/culture_collection_strains.tsv` lines 75646, 115914, and 132517 | Supported exactly for `DSM-28897`, `KCTC-12899`, and `NBRC-101209` under `NCBITaxon:442870`. |
| NCBI type-material rows | `data/raw/ncbi_type_material.tsv` lines 212342-212347 | Supported exactly for KCTC 12899, KCTC:12899, NBRC 101209, NBRC:101209, `personal::FYK2218`, and `strain FYK2218`. |
| Assembly and genome links | `data/raw/strain_assemblies.tsv` lines 115606-115614 and `data/raw/strain_genome_records.tsv` lines 92861-92868 | Supported exactly for BacDive, GTDB, GOLD, BV-BRC, and NCBI Assembly rows attached through `bacdive_24718`. |
| BV-BRC `patric:193.22` related links | `data/raw/strain_assemblies.tsv` line 115612, `data/raw/strain_genome_records.tsv` line 92864, and `data/raw/strain_related_records.tsv` lines 333098 and 333109 | Source-backed as a BV-BRC row matched on the exact `KCTC 12899` strain token; the source row itself names `Azospirillum lipoferum KCTC 12899` and `NCBITaxon:193`, so the cross-taxon value in the record preserves source provenance rather than silently reclassifying it. |
| GOLD organism, project, and analysis related records | `data/raw/strain_related_records.tsv` lines 333110-333116 and exact native GOLD rows for `Go0030476`, `Go0618056`, `Go0618057`, `Gp0592896`, and `Ga0504896` | Supported exactly. |
| StrainInfo overlay related records | `data/straininfo/strain_links.tsv` line 83245 and `data/straininfo/related_records.tsv.gz` lines 199917-199918 | Supported exactly for the DSM 28897 deposit and `straininfo.strain:399724` matched to `bacdive:24718` through the culture identifier. |
| Source attestation counts | `data/raw/ncbitaxon_taxa.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `bacdive_strains.tsv`, `mediadive_taxa.tsv`, `gold_organisms.tsv`, `madin_taxa.tsv`, and `bactotraits_taxa.tsv` | Supported exactly by the 1 NCBITAXON name, 1 LPSN name, 1 GTDB genome, 1 BACDIVE strain, 1 MEDIADIVE medium, 3 GOLD organisms, 8 MADIN trait assertions, and 18 BACTOTRAITS trait assertions for `NCBITaxon:442870`. |
| Empty retired-ID and ATB surfaces | Exact gitignore-independent scans of `data/raw/ncbi_merged_ids.tsv`, `data/raw/dropped.tsv`, and `data/atb/` for `NCBITaxon:442870` | Supported; no committed merged-ID, dropped-row, or AllTheBacteria overlay evidence points at this taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct genus parent, root-first bacterial lineage, one related synonym, genetic code `11`, and six type-material rows.
- LPSN supplies the correct-name nomenclature block, type-strain designations, publication identifiers, and `INSDC:AB303221`.
- GTDB supplies the same one-genome species count used by the `taxonomy_mappings` entry and the GTDB source attestation.
- BacDive supplies one local type strain, and the three culture-collection identifiers join to NCBI Assembly, GTDB, BV-BRC, GOLD, and StrainInfo evidence exactly as represented in `genome_assemblies`, `genome_records`, and `related_records`.
- MediaDive, GOLD, Madin et al., and BactoTraits provide aggregate source-attestation counts only in this record shape, and the stored counts match the raw inventories.
- No committed retired-ID, dropped-row, ATB, or curator-added `causal_graphs` evidence needs to be represented.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The local `data/raw/ncbitaxon_taxa.tsv`, LPSN, GTDB, BacDive, GOLD, BV-BRC, NCBI Assembly, and StrainInfo inventory rows are the committed snapshots that seeded the record.
- The `patric:193.22` entries are deliberately retained with their source taxon `NCBITaxon:193`; they trace to BV-BRC rows that match the record's `KCTC 12899` culture ID even though BV-BRC's genome name and taxonomy point to `Azospirillum lipoferum`.
