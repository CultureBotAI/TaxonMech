# YAML Record Review: Acetobacter lovaniensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_lovaniensis.yaml`
- Reviewed UTC: 2026-09-26T07:46:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:104100` |
| label | `Acetobacter lovaniensis` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, Madin et al., and StrainInfo evidence. The YAML contains one LPSN nomenclature row, two GTDB `skos:broadMatch` mappings, one exact NCBI synonym, two related synonyms, two xrefs, one BacDive-derived type-strain entry, 14 culture collection IDs, 28 genome assemblies, 18 genome records, 117 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 16138 maps `NCBITaxon:104100` to `acetobacter_lovaniensis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_lovaniensis.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_lovaniensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_indonesiensis.yaml data/taxa/bacteria/acetobacter_indonesiensis_nric_0313.yaml data/taxa/bacteria/acetobacter_lambici.yaml data/taxa/bacteria/acetobacter_lovaniensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 18603 has `NCBITaxon:104100`, label `Acetobacter lovaniensis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, one exact NCBI synonym, one related NCBI synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 5898 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, exact and related synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 18603 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 16138 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 5898 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature, synonym, and type-strain identifiers | `data/raw/lpsn_names.tsv` line 14807 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 1567-1568 | Supported exactly by two pooled `skos:broadMatch` mappings covering 19 total GTDB genomes. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 9, `data/raw/bacdive_strains.tsv` line 10, and 14 `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 9 materializes the single local strain with 14 normalized culture IDs. |
| GOLD, MediaDive, Madin et al., StrainInfo, and NCBI type-material evidence | `data/raw/gold_organisms.tsv` line 574, `data/raw/mediadive_taxa.tsv` line 162, `data/raw/madin_taxa.tsv` line 777, and exact StrainInfo/type-material scans | Supported by `organism_count=3`, 3 MediaDive media IDs, 1 Madin et al. assertion, 2 StrainInfo assemblies, 33 StrainInfo related records, 4 direct StrainInfo records, 23 StrainInfo deposit hits, and 18 exact type-material rows. |
| Empty same-taxon BactoTraits and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:104100` | Supported; no committed BactoTraits or NCBI merged-ID row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, one exact synonym, one related synonym, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion, one related synonym, and xrefs.
- GTDB supplies two intentionally broad mappings; because each is a pooled `skos:broadMatch`, the mappings remain in `taxonomy_mappings` and do not become exact xrefs.
- BacDive supplies the single generated local strain, and culture-collection, GOLD, BV-BRC, GTDB, NCBI Assembly, AllTheBacteria, and StrainInfo rows provide nested genome and related-record evidence for that strain.
- MediaDive and Madin et al. supply aggregate source attestations.
- No exact BactoTraits, NCBI merged-ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The two GTDB mappings split this species across `GTDB:s__Acetobacter_fabarum_B` and `GTDB:s__Acetobacter_lovaniensis`, so the `skos:broadMatch` predicates are expected.
