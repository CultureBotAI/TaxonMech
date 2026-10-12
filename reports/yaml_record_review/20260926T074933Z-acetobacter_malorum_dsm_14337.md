# YAML Record Review: Acetobacter malorum DSM 14337

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_malorum_dsm_14337.yaml`
- Reviewed UTC: 2026-09-26T07:49:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307910` |
| label | `Acetobacter malorum DSM 14337` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:178901` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record for DSM 14337 under `Acetobacter malorum`. It has source attestations from NCBITAXON, GTDB, BACDIVE, MEDIADIVE, and BACTOTRAITS; one GTDB exact synonym and xref; one GTDB `skos:closeMatch`; one BacDive-derived local strain; 7 culture collection IDs; 19 genome assemblies; 14 genome records; 66 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107656 maps `NCBITaxon:1307910` to `acetobacter_malorum_dsm_14337`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_malorum_dsm_14337.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_malorum_dsm_14337.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_lovaniensis_nric_0474.yaml data/taxa/bacteria/acetobacter_malorum.yaml data/taxa/bacteria/acetobacter_malorum_dsm_14337.yaml data/taxa/bacteria/acetobacter_musti.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309514 has `NCBITaxon:1307910`, label `Acetobacter malorum DSM 14337`, rank `STRAIN`, parent `NCBITaxon:178901`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive|bactotraits`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 15451 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 309514 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107656 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 15451 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 17790 | Supported exactly by one 13-genome `skos:closeMatch` to `GTDB:s__Acetobacter_malorum`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 13, `data/raw/bacdive_strains.tsv` line 14, and seven `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 13 materializes the single local strain with seven normalized culture IDs. |
| Genome and related-record evidence | Exact scans of raw strain tables for `NCBITaxon:1307910` | Supported by 9 raw assembly rows, 7 raw genome rows, and 20 raw related records keyed to this strain. |
| BactoTraits and MediaDive attestations | `data/raw/bactotraits_taxa.tsv` line 2341 and `data/raw/mediadive_taxa.tsv` line 2889 | Supported exactly with 7 BactoTraits assertions and 2 MediaDive media IDs. |
| Empty same-taxon LPSN, GOLD aggregate, Madin et al., StrainInfo, NCBI type-material, and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:1307910` | Supported; no committed row in those processed source tables names this strain as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter malorum` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the seven normalized collection identifiers attached to that strain.
- BV-BRC, GOLD, GTDB, NCBI Assembly, StrainInfo, and BacDive evidence that resolves through BacDive 13 is represented in the nested strain block.
- BactoTraits and MediaDive each supply one aggregate source attestation for the strain.
- No exact LPSN name, processed GOLD aggregate, Madin et al., StrainInfo overlay, NCBI type-material, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This generated strain shares BacDive record 13 with its parent `NCBITaxon:178901` species record.
