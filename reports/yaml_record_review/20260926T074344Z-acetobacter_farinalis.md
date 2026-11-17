# YAML Record Review: Acetobacter farinalis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_farinalis.yaml`
- Reviewed UTC: 2026-09-26T07:43:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1260984` |
| label | `Acetobacter farinalis` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, and StrainInfo evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, one NCBI related synonym, two xrefs, one BacDive-derived type-strain entry, 2 culture collection IDs, 6 related records, and no genome assemblies, genome records, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 88957 maps `NCBITaxon:1260984` to `acetobacter_farinalis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_farinalis.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_farinalis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_farinalis.yaml data/taxa/bacteria/acetobacter_garciniae.yaml data/taxa/bacteria/acetobacter_ghanensis.yaml data/taxa/bacteria/acetobacter_ghanensis_dsm_18895.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 291707 has `NCBITaxon:1260984`, label `Acetobacter farinalis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, one related NCBI synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 15340 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 291707 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 88957 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 15340 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifier | `data/raw/lpsn_names.tsv` line 26516 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 14467 | Supported exactly by one 3-genome `skos:closeMatch` to `GTDB:s__Acetobacter_farinalis`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 89915, `data/raw/bacdive_strains.tsv` line 89916, and two `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 167683 materializes the single local strain with BCC and NBRC culture IDs. |
| GOLD, StrainInfo, and NCBI type-material evidence | `data/raw/gold_organisms.tsv` line 6154 plus exact StrainInfo and NCBI type-material scans | Supported; the GOLD aggregate has `organism_count=2`, and exact scans found 5 StrainInfo related records, 3 direct StrainInfo records, 8 StrainInfo deposit hits, and 11 exact NCBI type-material rows. |
| Empty same-taxon MediaDive, Madin et al., BactoTraits, and raw genome surfaces | Exact scans for `NCBITaxon:1260984` | Supported; no committed MediaDive, Madin et al., BactoTraits, raw strain assembly, raw strain genome, or raw related-record row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, one related synonym, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive supplies the single generated local strain, and culture-collection plus StrainInfo rows provide the generated culture IDs and related records.
- GOLD supplies the aggregate organism attestation for this species.
- No exact MediaDive, Madin et al., BactoTraits, NCBI merged-ID, raw genome, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This species has committed strain identity and related-record evidence, but no processed raw assembly or genome rows; the zero `genome_assembly_count` and `genome_record_count` are therefore expected.
