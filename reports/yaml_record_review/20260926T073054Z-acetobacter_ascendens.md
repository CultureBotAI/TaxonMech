# YAML Record Review: Acetobacter ascendens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_ascendens.yaml`
- Reviewed UTC: 2026-09-26T07:30:54Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:481146` |
| label | `Acetobacter ascendens` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, Madin et al., and StrainInfo evidence. The YAML contains two LPSN nomenclature rows, one GTDB `skos:closeMatch`, seven synonyms, one GTDB xref, one BacDive-derived type-strain entry, 2 culture collection IDs, 13 genome assemblies, 11 genome records, 32 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 515534 maps `NCBITaxon:481146` to `acetobacter_ascendens`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_ascendens.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_ascendens.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_ascendens.yaml data/taxa/bacteria/acetobacter_calcoaceticus.yaml data/taxa/bacteria/acetobacter_cerevisiae.yaml data/taxa/bacteria/acetobacter_cerevisiae_dsm_14362.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 107417 has `NCBITaxon:481146`, label `Acetobacter ascendens`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 10021 keeps the species in scope. `data/raw/ncbi_merged_ids.tsv` line 99543 redirects old ID `NCBITaxon:940260` into `NCBITaxon:481146`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, source set, old merged ID, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 107417 and `data/raw/ncbi_merged_ids.tsv` line 99543 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 515534 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 10021 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature | `data/raw/lpsn_names.tsv` lines 1569 and 2204 | Supported exactly by two deprecated species-name rows that both point at `lpsn:772511`. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 291989 | Supported exactly by one 6-genome `skos:closeMatch` to `GTDB:s__Acetobacter_ascendens`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 85537, `data/raw/bacdive_strains.tsv` line 85538, and two `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 163302 materializes the single local strain with JCM and LMG culture IDs. |
| GOLD and strain evidence | `data/raw/gold_organisms.tsv` line 36763 plus exact raw and StrainInfo scans | Supported; the GOLD aggregate has `organism_count=5`, and exact scans found 26 raw strain assemblies, 21 raw genome records, 50 raw related records, and 14 StrainInfo related records for this taxon. |
| NCBI type material and Madin et al. attestations | `data/raw/ncbi_type_material.tsv` and `data/raw/madin_taxa.tsv` line 25199 | Supported; 20 exact NCBI type-material rows and 1 Madin et al. assertion row name this taxon. |
| Empty same-taxon MediaDive and BactoTraits surfaces | Exact scans for `NCBITaxon:481146` | Supported; no committed MediaDive or BactoTraits row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, the direct `Acetobacter` parent, the merged old ID, and the exact 9-ancestor lineage.
- LPSN supplies the deprecated nomenclature rows represented in the YAML, and GTDB supplies the only taxonomy mapping.
- BacDive supplies the single generated local strain, while culture-collection, GOLD, BV-BRC, GTDB, NCBI Assembly, and StrainInfo rows provide nested genome and related-record evidence for that strain.
- No exact MediaDive, BactoTraits, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

NCBI type-material rows for this species include both excluded type-material strings and true `type strain` strings; the YAML correctly derives its generated local strain from BacDive rather than from every NCBI type-material string.
