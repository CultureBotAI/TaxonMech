# YAML Record Review: Acetobacter lambici

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_lambici.yaml`
- Reviewed UTC: 2026-09-26T07:46:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1332824` |
| label | `Acetobacter lambici` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, BactoTraits, and StrainInfo evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, five NCBI related synonyms, two xrefs, one BacDive-derived type-strain entry, 2 culture collection IDs, 9 genome assemblies, 7 genome records, 32 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 118377 maps `NCBITaxon:1332824` to `acetobacter_lambici`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_lambici.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_lambici.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_indonesiensis.yaml data/taxa/bacteria/acetobacter_indonesiensis_nric_0313.yaml data/taxa/bacteria/acetobacter_lambici.yaml data/taxa/bacteria/acetobacter_lovaniensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 319450 has `NCBITaxon:1332824`, label `Acetobacter lambici`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|bactotraits`, five related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 7728 keeps the species in scope. `data/raw/ncbi_merged_ids.tsv` lines 13936-13938 redirect old IDs `NCBITaxon:1379703`, `NCBITaxon:1379704`, and `NCBITaxon:1379705` into `NCBITaxon:1332824`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonyms, old merged IDs, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 319450 and `data/raw/ncbi_merged_ids.tsv` lines 13936-13938 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 118377 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 7728 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 28519 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 19406 | Supported exactly by one 3-genome `skos:closeMatch` to `GTDB:s__Acetobacter_lambici`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 23262, `data/raw/bacdive_strains.tsv` line 23263, and two `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 23489 materializes the single local strain with DSM and LMG culture IDs. |
| GOLD, MediaDive, BactoTraits, StrainInfo, and NCBI type-material evidence | `data/raw/gold_organisms.tsv` line 8073, `data/raw/mediadive_taxa.tsv` line 3030, `data/raw/bactotraits_taxa.tsv` line 2457, and exact StrainInfo/type-material scans | Supported by `organism_count=3`, 1 MediaDive medium, 1 BactoTraits assertion, 1 StrainInfo assembly, 8 StrainInfo related records, 2 direct StrainInfo records, 3 StrainInfo deposit hits, and 5 exact type-material rows. |
| Empty same-taxon Madin et al. surface | Exact scan for `NCBITaxon:1332824` | Supported; no committed Madin et al. row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, five related synonyms, three merged old IDs, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive supplies the single generated local strain, and culture-collection, GOLD, BV-BRC, GTDB, NCBI Assembly, AllTheBacteria, and StrainInfo rows provide nested genome and related-record evidence for that strain.
- MediaDive and BactoTraits supply aggregate source attestations.
- No exact Madin et al., generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The three NCBI merged IDs are preserved as equivalent identifiers on the generated record.
