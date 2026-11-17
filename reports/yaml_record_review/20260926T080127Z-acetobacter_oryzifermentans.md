# YAML Record Review: Acetobacter oryzifermentans

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_oryzifermentans.yaml`
- Reviewed UTC: 2026-09-26T08:01:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1633874` |
| label | `Acetobacter oryzifermentans` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, StrainInfo, and NCBI type-material evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, three NCBI related synonyms, two xrefs, one BacDive-derived type-strain entry, 3 culture collection IDs, 1 BacDive-derived genome assembly, 2 related records, and no generated definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 230493 maps `NCBITaxon:1633874` to `acetobacter_oryzifermentans`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_oryzifermentans.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_oryzifermentans.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_orleanensis.yaml data/taxa/bacteria/acetobacter_orleanensis_jcm_7639.yaml data/taxa/bacteria/acetobacter_orleanensis_nric_0473.yaml data/taxa/bacteria/acetobacter_oryzifermentans.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 425055 has `NCBITaxon:1633874`, label `Acetobacter oryzifermentans`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, three related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 16040 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 425055 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 230493 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 16040 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifier | `data/raw/lpsn_names.tsv` line 34070 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 41919 | Supported exactly by one 28-genome `skos:closeMatch` to `GTDB:s__Acetobacter_oryzifermentans`. |
| BacDive, GOLD, StrainInfo, and NCBI type-material evidence | `data/bacdive/records.jsonl.gz` line 86182, `data/raw/bacdive_strains.tsv` line 86183, `data/raw/gold_organisms.tsv` line 13992, exact StrainInfo scans, and exact NCBI type-material scans | Supported by BacDive record 163947, `organism_count=1`, one direct StrainInfo record, one StrainInfo deposit hit, two StrainInfo related records, and six exact type-material rows. |
| Empty same-taxon MediaDive, BactoTraits, Madin et al., and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:1633874` | Supported; no committed row in those processed source tables names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, three related synonyms, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive supplies the single generated local type-strain block, and the culture-collection table contributes the three normalized collection identifiers attached to that strain.
- BacDive, GOLD, and StrainInfo rows that resolve to this species or its local strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact MediaDive, BactoTraits, Madin et al., NCBI merged ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The only exact raw genome assembly row is BacDive-derived, so the empty `genome_records` list is expected even though one BacDive assembly is present.
