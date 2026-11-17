# YAML Record Review: Acetobacter musti

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_musti.yaml`
- Reviewed UTC: 2026-09-26T07:49:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:864732` |
| label | `Acetobacter musti` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, and BactoTraits evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, two NCBI related synonyms, two xrefs, one BacDive-derived type-strain entry, 2 culture collection IDs, 6 related records, and no genome assemblies, genome records, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 595905 maps `NCBITaxon:864732` to `acetobacter_musti`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_musti.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_musti.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_lovaniensis_nric_0474.yaml data/taxa/bacteria/acetobacter_malorum.yaml data/taxa/bacteria/acetobacter_malorum_dsm_14337.yaml data/taxa/bacteria/acetobacter_musti.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 182015 has `NCBITaxon:864732`, label `Acetobacter musti`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|bactotraits`, two related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 7004 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 182015 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 595905 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 7004 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifier | `data/raw/lpsn_names.tsv` line 30456 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 315550 | Supported exactly by one 2-genome `skos:closeMatch` to `GTDB:s__Acetobacter_musti`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 54723, `data/raw/bacdive_strains.tsv` line 54724, and two `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 132413 materializes the single local strain with CECT and DSM culture IDs. |
| GOLD, MediaDive, BactoTraits, StrainInfo, and NCBI type-material evidence | `data/raw/gold_organisms.tsv` line 43469, `data/raw/mediadive_taxa.tsv` line 13526, `data/raw/bactotraits_taxa.tsv` line 9120, and exact StrainInfo/type-material scans | Supported by `organism_count=4`, 1 MediaDive medium, 5 BactoTraits assertions, 2 StrainInfo related records, 2 direct StrainInfo records, 3 StrainInfo deposit hits, and 6 exact type-material rows. |
| Empty same-taxon Madin et al. and raw genome surfaces | Exact scans for `NCBITaxon:864732` | Supported; no committed Madin et al., raw assembly, or raw genome row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, two related synonyms, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive supplies the single generated local strain, and culture-collection plus StrainInfo rows provide the generated culture IDs and related records.
- GOLD, MediaDive, and BactoTraits supply aggregate source attestations.
- No exact Madin et al., raw genome, NCBI merged-ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This species has committed strain identity and related-record evidence, but no processed raw assembly or genome rows; the zero `genome_assembly_count` and `genome_record_count` are therefore expected.
