# YAML Record Review: Acetobacter estunensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_estunensis.yaml`
- Reviewed UTC: 2026-09-26T07:36:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:104097` |
| label | `Acetobacter estunensis` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, Madin et al., and StrainInfo evidence. The YAML contains one LPSN nomenclature row, two GTDB `skos:broadMatch` mappings, five synonyms, two xrefs, one BacDive-derived type-strain entry, 11 culture collection IDs, 9 genome assemblies, 7 genome records, 71 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 16115 maps `NCBITaxon:104097` to `acetobacter_estunensis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_estunensis.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_estunensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_cibinongensis.yaml data/taxa/bacteria/acetobacter_cibinongensis_nric_0482.yaml data/taxa/bacteria/acetobacter_conturbans.yaml data/taxa/bacteria/acetobacter_estunensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 18600 has `NCBITaxon:104097`, label `Acetobacter estunensis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, one exact NCBI synonym, three related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 5897 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 18600 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 16115 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 5897 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature, synonym, and type-strain identifiers | `data/raw/lpsn_names.tsv` line 14802 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 1551-1552 | Supported exactly by two pooled `skos:broadMatch` mappings covering 3 total GTDB genomes. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 10, `data/raw/bacdive_strains.tsv` line 11, and 11 `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 10 materializes the single local strain with 11 normalized culture IDs. |
| GOLD, MediaDive, Madin et al., and strain evidence | `data/raw/gold_organisms.tsv` line 568, `data/raw/mediadive_taxa.tsv` line 160, `data/raw/madin_taxa.tsv` line 762, and exact raw/StrainInfo scans | Supported; the GOLD aggregate has `organism_count=3`, MediaDive reports 3 media IDs, Madin et al. reports 1 assertion, and strain scans found 8 raw assemblies, 6 raw genome records, 20 raw related records, 1 StrainInfo assembly, and 29 StrainInfo related records. |
| NCBI type-material evidence and empty same-taxon BactoTraits/NCBI merged-id surfaces | Exact scans for `NCBITaxon:104097` | Supported; 15 NCBI type-material rows name this taxon, and no committed BactoTraits or NCBI merged-ID row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, four synonym strings, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion, one related synonym, and xrefs.
- GTDB supplies two intentionally broad species mappings; because each is a pooled `skos:broadMatch`, the mappings remain in `taxonomy_mappings` and do not become exact xrefs.
- BacDive supplies the single generated local strain, and culture-collection, GOLD, BV-BRC, GTDB, NCBI Assembly, AllTheBacteria, and StrainInfo rows provide nested genome and related-record evidence for that strain.
- MediaDive and Madin et al. supply aggregate source attestations for the species.
- No exact BactoTraits, NCBI merged-ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The two GTDB mappings split `Acetobacter estunensis` into GTDB species `Acetobacter_estunensis` and `Acetobacter_estunensis_A`, so their `skos:broadMatch` predicates are expected.
