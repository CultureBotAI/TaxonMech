# YAML Record Review: Acetobacter malorum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_malorum.yaml`
- Reviewed UTC: 2026-09-26T07:49:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:178901` |
| label | `Acetobacter malorum` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, Madin et al., and StrainInfo evidence. The YAML contains one LPSN nomenclature row, two GTDB `skos:broadMatch` mappings, two NCBI related synonyms, two xrefs, two BacDive-derived local strains, 8 culture collection IDs, 19 genome assemblies, 14 genome records, 66 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 272026 maps `NCBITaxon:178901` to `acetobacter_malorum`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_malorum.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_malorum.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_lovaniensis_nric_0474.yaml data/taxa/bacteria/acetobacter_malorum.yaml data/taxa/bacteria/acetobacter_malorum_dsm_14337.yaml data/taxa/bacteria/acetobacter_musti.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 35859 has `NCBITaxon:178901`, label `Acetobacter malorum`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, two related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 21112 keeps the species in scope. `data/raw/ncbi_merged_ids.tsv` line 80882 redirects old ID `NCBITaxon:479937` into `NCBITaxon:178901`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonyms, old merged ID, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 35859 and `data/raw/ncbi_merged_ids.tsv` line 80882 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 272026 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 21112 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 14808 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 56465-56466 | Supported exactly by two pooled `skos:broadMatch` mappings covering 15 total GTDB genomes. |
| BacDive strain identities | `data/bacdive/records.jsonl.gz` lines 13 and 99043 plus exact raw BacDive scans | Supported; BacDive 13 names the DSM 14337 child strain, while BacDive 176819 is keyed directly to this species. |
| GOLD, Madin et al., StrainInfo, and NCBI type-material evidence | `data/raw/gold_organisms.tsv` line 15630, `data/raw/madin_taxa.tsv` line 18415, and exact StrainInfo/type-material scans | Supported by `organism_count=8`, 3 Madin et al. assertions, 1 StrainInfo assembly, 28 StrainInfo related records, 6 direct StrainInfo records, 22 StrainInfo deposit hits, and 7 exact type-material rows. |
| Empty same-taxon MediaDive and BactoTraits surfaces | Exact scans for `NCBITaxon:178901` | Supported; no committed MediaDive or BactoTraits row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, two related synonyms, one merged old ID, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs.
- GTDB supplies two intentionally broad mappings; because each is a pooled `skos:broadMatch`, the mappings remain in `taxonomy_mappings` and do not become exact xrefs.
- BacDive supplies two generated local strains, including the DSM 14337 child strain also represented as `NCBITaxon:1307910`.
- GOLD, BV-BRC, GTDB, NCBI Assembly, StrainInfo, BacDive, and Madin et al. rows that resolve to this species or its canonical child strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact MediaDive, BactoTraits, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

BacDive record 13 is strain-level for `NCBITaxon:1307910` but also names this parent species; the generated species and strain YAMLs therefore share the same BacDive 13 culture identity.
