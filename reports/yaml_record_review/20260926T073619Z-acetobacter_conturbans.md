# YAML Record Review: Acetobacter conturbans

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_conturbans.yaml`
- Reviewed UTC: 2026-09-26T07:36:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1737472` |
| label | `Acetobacter conturbans` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, and StrainInfo evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, two NCBI related synonyms, two xrefs, one BacDive-derived type-strain entry, 2 culture collection IDs, 9 genome assemblies, 7 genome records, 24 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 260258 maps `NCBITaxon:1737472` to `acetobacter_conturbans`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_conturbans.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_conturbans.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_cibinongensis.yaml data/taxa/bacteria/acetobacter_cibinongensis_nric_0482.yaml data/taxa/bacteria/acetobacter_conturbans.yaml data/taxa/bacteria/acetobacter_estunensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 453832 has `NCBITaxon:1737472`, label `Acetobacter conturbans`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, two related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 16249 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 453832 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 260258 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 16249 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifier | `data/raw/lpsn_names.tsv` line 2753 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 54244 | Supported exactly by one 1-genome `skos:closeMatch` to `GTDB:s__Acetobacter_conturbans`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 89365, `data/raw/bacdive_strains.tsv` line 89366, and two `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 167133 materializes the single local strain with LMG and NCIMB culture IDs. |
| GOLD and strain evidence | `data/raw/gold_organisms.tsv` line 15082 plus exact raw and StrainInfo scans | Supported; the GOLD aggregate has `organism_count=1`, and exact scans found 8 raw strain assemblies, 6 raw genome records, 18 raw related records, 1 StrainInfo assembly, and 2 StrainInfo related records. |
| NCBI type-material evidence and empty same-taxon MediaDive/Madin/BactoTraits surfaces | `data/raw/ncbi_type_material.tsv` plus exact auxiliary scans | Supported; 5 NCBI type-material rows name this taxon, and no committed MediaDive, Madin et al., or BactoTraits row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, two related synonyms, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive supplies the single generated local strain, and culture-collection, GOLD, BV-BRC, GTDB, NCBI Assembly, AllTheBacteria, and StrainInfo rows provide nested genome and related-record evidence for that strain.
- No exact MediaDive, Madin et al., BactoTraits, NCBI merged-ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The single GTDB mapping is close rather than broad, so it is represented both as a taxonomy mapping and through the generated GTDB xref.
