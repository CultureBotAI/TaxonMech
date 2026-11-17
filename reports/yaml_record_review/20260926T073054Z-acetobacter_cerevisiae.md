# YAML Record Review: Acetobacter cerevisiae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_cerevisiae.yaml`
- Reviewed UTC: 2026-09-26T07:30:54Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:178900` |
| label | `Acetobacter cerevisiae` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, Madin et al., BactoTraits, and StrainInfo evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, one related NCBI synonym, two xrefs, three BacDive-derived local strains, 23 culture collection IDs, 19 genome assemblies, 14 genome records, 139 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 272022 maps `NCBITaxon:178900` to `acetobacter_cerevisiae`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_cerevisiae.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_cerevisiae.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_ascendens.yaml data/taxa/bacteria/acetobacter_calcoaceticus.yaml data/taxa/bacteria/acetobacter_cerevisiae.yaml data/taxa/bacteria/acetobacter_cerevisiae_dsm_14362.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 35858 has `NCBITaxon:178900`, label `Acetobacter cerevisiae`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, no exact NCBI synonyms, one related NCBI synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 1270 keeps the species in scope. `data/raw/lpsn_names.tsv` line 14799 carries the LPSN correct-name row with type-strain IDs for ATCC 23765, DSM 14362, and LMG 1625.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 35858 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 272022 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 1270 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 14799 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 56464 | Supported exactly by one 10-genome `skos:closeMatch` to `GTDB:s__Acetobacter_cerevisiae`. |
| BacDive-derived strains and culture IDs | `data/bacdive/records.jsonl.gz` lines 3, 12, and 58897 plus exact raw BacDive and culture-collection scans | Supported; 3 BacDive JSON records, 2 normalized species-level BacDive strain rows, and 16 raw culture rows contribute to the generated local strains. |
| GOLD and strain evidence | `data/raw/gold_organisms.tsv` line 15629 plus exact raw and StrainInfo scans | Supported; the GOLD aggregate has `organism_count=3`, and exact scans found 9 raw strain assemblies, 7 raw genome records, 20 raw related records, 1 StrainInfo assembly, and 42 StrainInfo related records for this taxon. |
| BactoTraits, MediaDive, Madin et al., and NCBI type-material attestations | `data/raw/bactotraits_taxa.tsv` line 4075, `data/raw/mediadive_taxa.tsv` line 5266, `data/raw/madin_taxa.tsv` line 18414, and `data/raw/ncbi_type_material.tsv` exact rows | Supported by 1 BactoTraits assertion, 2 MediaDive media IDs, 2 Madin et al. assertions, and 13 exact NCBI type-material rows. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, one related synonym, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive and StrainInfo contribute the three generated local strain blocks and their culture IDs, assemblies, genome records, and related records.
- GOLD, MediaDive, Madin et al., BactoTraits, BV-BRC, GTDB, NCBI Assembly, and BacDive source rows that resolve to this taxon are represented as aggregate attestations or nested strain evidence as appropriate.
- No generated definition or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

BacDive record 12 also names strain `NCBITaxon:1307903`, and the generated DSM 14362 strain record reuses that same BacDive 12 culture identity.
