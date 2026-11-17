# YAML Record Review: Acaricomes phytoseiuli

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acaricomes_phytoseiuli.yaml
- Started UTC: 2026-09-22T06:42:03Z
- Finished UTC: 2026-09-22T06:42:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:291968 |
| label | Acaricomes phytoseiuli |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:291967 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| strain_count | 1 |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species at `data/taxa/bacteria/acaricomes_phytoseiuli.yaml`. It carries one LPSN nomenclature entry, one close GTDB mapping to `GTDB:s__Renibacterium_phytoseiuli`, one NCBI related synonym, one GTDB exact synonym, a descendant BacDive strain classified as `NCBITaxon:1120917`, nine assembly rows, six genome rows, StrainInfo and GOLD related records, and source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN. It has no curator-added `causal_graphs`.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 392364 maps `NCBITaxon:291968` to slug `acaricomes_phytoseiuli`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -type f -name "????????T??????Z-acaricomes_phytoseiuli.md" -print` returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acaricomes_phytoseiuli.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaricomes_phytoseiuli.yaml data/taxa/bacteria/acaricomes_phytoseiuli_dsm_14247.yaml data/taxa/bacteria/acaricomes_sp.yaml data/taxa/bacteria/acaricomes_sp_rhf117.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 59596 has `NCBITaxon:291968`, label `Acaricomes phytoseiuli`, rank `SPECIES`, direct parent `NCBITaxon:291967`, NCBI related synonym `Acaricomes phytoseiuli Pukall et al. 2006 emend. Nouioui et al. 2018`, genetic code `11`, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:201174` Actinomycetota, `PHYLUM` | line 39769 |
| `NCBITaxon:1760` Actinomycetes, `CLASS` | line 1378 |
| `NCBITaxon:85006` Micrococcales, `ORDER` | line 13092 |
| `NCBITaxon:1268` Micrococcaceae, `FAMILY` | line 978 |
| `NCBITaxon:291967` Acaricomes, `GENUS` | line 59595 |

The LPSN nomenclature block is species-scoped and supported by `data/raw/lpsn_names.tsv` line 14789, which maps `lpsn:772478` to `NCBITaxon:291968` with the correct-name status, type-strain designations `CCUG-49701`, `DSM-14247`, and `JCM-14300`, the Pukall et al. references, and `INSDC:AJ812213`. The GTDB entry is supported by `data/raw/gtdb_mappings.tsv` line 234204 and `data/raw/gtdb_species.tsv` line 153194; both carry `GTDB:s__Renibacterium_phytoseiuli` with genome count 2.

`curation/seed_scope.tsv` line 21261 keeps this species in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, related synonym, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 59596 | Supported exactly. |
| LPSN nomenclature and `lpsn:772478` xref | `data/raw/lpsn_names.tsv` line 14789 | Supported exactly for the species-level name, status flags, type-strain designations, publications, and sequence accession. |
| GTDB mapping, `Renibacterium phytoseiuli` exact synonym, and `GTDB:s__Renibacterium_phytoseiuli` xref | `data/raw/gtdb_mappings.tsv` line 234204 and `data/raw/gtdb_species.tsv` line 153194 | Supported exactly with `skos:closeMatch` and two GTDB genomes. |
| Descendant BacDive strain `kgmicrobe.strain:bacdive_7517` | `data/raw/bacdive_strains.tsv` line 7392 and the native `data/bacdive/records.jsonl.gz` record for BacDive ID 7517 | Supported; BacDive files strain CSC under `NCBITaxon:1120917`, and the generated species record preserves that narrower identity in `classified_as`. |
| Culture-collection IDs | `data/raw/culture_collection_strains.tsv` lines 29991, 48903, 66030, 101146, and 133612 | Supported exactly for CCUG 49701, CIP 109141, DSM 14247, JCM 14300, and NBRC 107788 under the strain taxon. |
| NCBI type-material rows | `data/raw/ncbi_type_material.tsv` lines 141223-141230 | Supported exactly for the CCUG, DSM, JCM, and CSC spelling variants attached to `NCBITaxon:291968`. |
| Assembly and genome links | `data/raw/strain_assemblies.tsv` lines 150561-150568, `data/raw/strain_genome_records.tsv` lines 120100-120105, and `data/straininfo/assemblies.tsv` line 11895 | Supported exactly for BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo rows linked through `bacdive_7517`. |
| GOLD and StrainInfo related records | `data/raw/strain_related_records.tsv` lines 430716-430737, exact native GOLD rows for `Go0013855`, `Go0625829`, `Go0625830`, `Gp0013855`, and `Ga0000001`, and `data/straininfo/related_records.tsv.gz` lines 252298-252306 | Supported exactly. |
| Source attestation counts | NCBITaxon, LPSN, GTDB, BacDive, GOLD, and Madin et al. raw inventories | Supported exactly by 1 NCBITAXON name, 1 LPSN name, 2 GTDB genomes, 1 descendant BACDIVE strain, 2 direct GOLD organisms, and 11 MADIN trait assertions for `NCBITaxon:291968`. |
| Empty retired-ID and ATB surfaces | Exact gitignore-independent scans of `data/raw/ncbi_merged_ids.tsv`, `data/raw/dropped.tsv`, `data/atb/`, and `data/straininfo/exclusions.tsv` for `NCBITaxon:291968` | Supported; no committed merged-ID, dropped-row, ATB, or StrainInfo exclusion evidence points at this species. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct genus parent, root-first bacterial lineage, one related synonym, genetic code `11`, and eight type-material rows.
- LPSN supplies the correct-name nomenclature block for the species; the strain taxon correctly does not duplicate that LPSN name as a separate nomenclature entry.
- GTDB supplies the two-genome `Renibacterium_phytoseiuli` mapping used by the species-level `taxonomy_mappings` entry.
- BacDive supplies one descendant local strain with five culture-collection IDs, and the raw row's `NCBITaxon:1120917` target is preserved in the strain's `classified_as` field.
- GOLD direct organism assertions remain counted separately from descendant strain-taxonomy GOLD rows, while strain-related GOLD evidence is retained under the local BacDive strain.
- No committed retired-ID, dropped-row, ATB, MediaDive, BactoTraits, or curator-added `causal_graphs` evidence needs to be represented at the parent species level.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local NCBITaxon, LPSN, GTDB, BacDive, GOLD, BV-BRC, NCBI Assembly, and StrainInfo inventory rows are the committed snapshots that seeded the record.
