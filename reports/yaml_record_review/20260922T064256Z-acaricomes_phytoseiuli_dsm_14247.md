# YAML Record Review: Acaricomes phytoseiuli DSM 14247

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acaricomes_phytoseiuli_dsm_14247.yaml
- Started UTC: 2026-09-22T06:42:03Z
- Finished UTC: 2026-09-22T06:42:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1120917 |
| label | Acaricomes phytoseiuli DSM 14247 |
| rank | STRAIN |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:291968 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| strain_count | 1 |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial strain taxon at `data/taxa/bacteria/acaricomes_phytoseiuli_dsm_14247.yaml`. It carries one close GTDB mapping to `GTDB:s__Renibacterium_phytoseiuli`, one GTDB exact synonym, the `bacdive_7517` local strain surface, nine assembly rows, six genome rows, GOLD and StrainInfo related records that join through the same BacDive strain, and source attestations from NCBITAXON, GTDB, BACDIVE, MEDIADIVE, MADIN, and BACTOTRAITS. It has no LPSN nomenclature and no curator-added `causal_graphs`.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 35980 maps `NCBITaxon:1120917` to slug `acaricomes_phytoseiuli_dsm_14247`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -type f -name "????????T??????Z-acaricomes_phytoseiuli_dsm_14247.md" -print` returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acaricomes_phytoseiuli_dsm_14247.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaricomes_phytoseiuli.yaml data/taxa/bacteria/acaricomes_phytoseiuli_dsm_14247.yaml data/taxa/bacteria/acaricomes_sp.yaml data/taxa/bacteria/acaricomes_sp_rhf117.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 241896 has `NCBITaxon:1120917`, label `Acaricomes phytoseiuli DSM 14247`, rank `STRAIN`, direct parent `NCBITaxon:291968`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon|gtdb|bacdive|mediadive|madin_etal|bactotraits`, and snapshot date `2026-09-13`.

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
| `NCBITaxon:291968` Acaricomes phytoseiuli, `SPECIES` | line 59596 |

The GTDB mapping is supported by `data/raw/gtdb_mappings.tsv` line 4392 and `data/raw/gtdb_species.tsv` line 153194; both carry `GTDB:s__Renibacterium_phytoseiuli` with genome count 2. The lack of an LPSN `nomenclature` entry is correct for the strain record: `data/raw/lpsn_names.tsv` line 14789 maps `lpsn:772478` to the parent species `NCBITaxon:291968`, not to the strain taxon.

`curation/seed_scope.tsv` line 10941 keeps this strain taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, empty synonym slots, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 241896 | Supported exactly. |
| GTDB mapping, `Renibacterium phytoseiuli` exact synonym, and `GTDB:s__Renibacterium_phytoseiuli` xref | `data/raw/gtdb_mappings.tsv` line 4392 and `data/raw/gtdb_species.tsv` line 153194 | Supported exactly with `skos:closeMatch` and two GTDB genomes. |
| BacDive local strain `kgmicrobe.strain:bacdive_7517` | `data/raw/bacdive_strains.tsv` line 7392 and the native `data/bacdive/records.jsonl.gz` record for BacDive ID 7517 | Supported exactly for strain CSC, `bacdive:7517`, the strain taxon, `lpsn:772478`, and five culture IDs. |
| Culture-collection IDs | `data/raw/culture_collection_strains.tsv` lines 29991, 48903, 66030, 101146, and 133612 | Supported exactly for CCUG 49701, CIP 109141, DSM 14247, JCM 14300, and NBRC 107788 under `NCBITaxon:1120917`. |
| Assembly and genome links | `data/raw/strain_assemblies.tsv` lines 150561-150568, `data/raw/strain_genome_records.tsv` lines 120100-120105, and `data/straininfo/assemblies.tsv` line 11895 | Supported exactly for BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo rows linked through `bacdive_7517`. |
| GOLD and StrainInfo related records | `data/raw/strain_related_records.tsv` lines 430716-430737, exact native GOLD rows for `Go0013855`, `Go0625829`, `Go0625830`, `Gp0013855`, and `Ga0000001`, and `data/straininfo/related_records.tsv.gz` lines 252298-252306 | Supported exactly. |
| Source attestation counts | NCBITaxon, GTDB, BacDive, MediaDive, Madin et al., and BactoTraits raw inventories | Supported exactly by 1 NCBITAXON name, 2 GTDB genomes, 1 BACDIVE strain, 2 MEDIADIVE media, 5 MADIN trait assertions, and 18 BACTOTRAITS trait assertions for `NCBITaxon:1120917`. |
| Empty retired-ID and ATB surfaces | Exact gitignore-independent scans of `data/raw/ncbi_merged_ids.tsv`, `data/raw/dropped.tsv`, `data/atb/`, and `data/straininfo/exclusions.tsv` for `NCBITaxon:1120917` | Supported; no committed merged-ID, dropped-row, ATB, or StrainInfo exclusion evidence points at this strain taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the strain identity, direct parent species, root-first bacterial lineage, genetic code `11`, and NCBITAXON source attestation.
- GTDB supplies the two-genome `Renibacterium_phytoseiuli` mapping used by the strain-level `taxonomy_mappings` entry.
- BacDive supplies one local strain with five culture-collection IDs; those IDs join to BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo evidence exactly as represented.
- MediaDive, Madin et al., and BactoTraits provide direct strain-taxon aggregate counts, and the stored counts match the raw inventories.
- LPSN and NCBI type-material evidence belongs to the parent species record in the current committed inventories, and no committed retired-ID, dropped-row, ATB, or curator-added `causal_graphs` evidence needs to be represented at this strain taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local NCBITaxon, GTDB, BacDive, MediaDive, GOLD, BV-BRC, NCBI Assembly, and StrainInfo inventory rows are the committed snapshots that seeded the record.
