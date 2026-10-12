# YAML Record Review: Acetobacter cerevisiae DSM 14362

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_cerevisiae_dsm_14362.yaml`
- Reviewed UTC: 2026-09-26T07:30:54Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307903` |
| label | `Acetobacter cerevisiae DSM 14362` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:178900` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record for DSM 14362 under `Acetobacter cerevisiae`. It has source attestations from NCBITAXON, GTDB, BACDIVE, MEDIADIVE, and BACTOTRAITS; one GTDB `skos:closeMatch`; one GTDB exact synonym and xref; one BacDive-derived local strain; 7 culture collection IDs; 19 genome assemblies; 14 genome records; 71 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107648 maps `NCBITaxon:1307903` to `acetobacter_cerevisiae_dsm_14362`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_cerevisiae_dsm_14362.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_cerevisiae_dsm_14362.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_ascendens.yaml data/taxa/bacteria/acetobacter_calcoaceticus.yaml data/taxa/bacteria/acetobacter_cerevisiae.yaml data/taxa/bacteria/acetobacter_cerevisiae_dsm_14362.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309507 has `NCBITaxon:1307903`, label `Acetobacter cerevisiae DSM 14362`, rank `STRAIN`, parent `NCBITaxon:178900`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive|bactotraits`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 15448 keeps the strain in scope. The exact same-taxon auxiliary rows are `data/raw/gtdb_mappings.tsv` line 17783, `data/raw/bactotraits_taxa.tsv` line 2338, and `data/raw/mediadive_taxa.tsv` line 2884.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 309507 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107648 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 15448 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 17783 | Supported exactly by one 10-genome `skos:closeMatch` to `GTDB:s__Acetobacter_cerevisiae`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 12, `data/raw/bacdive_strains.tsv` line 13, and seven `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 12 materializes the single local strain with seven normalized culture IDs. |
| Genome and related-record evidence | Exact scans of `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` for `NCBITaxon:1307903` | Supported by 9 raw assemblies, 7 raw genome records, and 20 raw related records keyed to this strain. |
| BactoTraits and MediaDive attestations | `data/raw/bactotraits_taxa.tsv` line 2338 and `data/raw/mediadive_taxa.tsv` line 2884 | Supported exactly with 8 BactoTraits assertions and 2 MediaDive media IDs. |
| Empty same-taxon LPSN, GOLD aggregate, Madin et al., StrainInfo, NCBI type-material, and NCBI merged-id surfaces | Exact scans for `NCBITaxon:1307903` | Supported; no committed row in those processed source tables names this strain as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter cerevisiae` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the seven normalized collection identifiers attached to that strain.
- BV-BRC, GTDB, NCBI Assembly, GOLD-linked, and BacDive raw rows that resolve to this canonical strain are represented as nested genome and related-record evidence.
- BactoTraits and MediaDive each supply one aggregate source attestation for the strain.
- No exact LPSN name, processed GOLD aggregate, Madin et al., StrainInfo overlay, NCBI type-material, NCBI merged-id evidence, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The native GOLD table has one DSM 14362 organism/project/analysis triplet, but this strain does not have its own `data/raw/gold_organisms.tsv` aggregate row; GOLD-derived nested rows are represented through the canonical BacDive strain where available.
