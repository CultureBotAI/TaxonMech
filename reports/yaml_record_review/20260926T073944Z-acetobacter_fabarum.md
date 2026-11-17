# YAML Record Review: Acetobacter fabarum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_fabarum.yaml`
- Reviewed UTC: 2026-09-26T07:39:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:483199` |
| label | `Acetobacter fabarum` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, Madin et al., and StrainInfo evidence. The YAML contains one LPSN nomenclature row, three GTDB `skos:broadMatch` mappings, one related NCBI synonym, two xrefs, one BacDive-derived type-strain entry for the DSM 19596 child strain, 2 culture collection IDs, 16 genome assemblies, 11 genome records, 41 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 516022 maps `NCBITaxon:483199` to `acetobacter_fabarum`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_fabarum.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_fabarum.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_estunensis_nric_0472.yaml data/taxa/bacteria/acetobacter_fabarum.yaml data/taxa/bacteria/acetobacter_fabarum_dsm_19596.yaml data/taxa/bacteria/acetobacter_fallax.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 107904 has `NCBITaxon:483199`, label `Acetobacter fabarum`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, one related NCBI synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 21434 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 107904 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 516022 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 21434 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 24046 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 292047-292049 | Supported exactly by three pooled `skos:broadMatch` mappings covering 47 total GTDB genomes. |
| BacDive strain identity | `data/bacdive/records.jsonl.gz` line 23 and `data/raw/bacdive_strains.tsv` line 24 | Supported; BacDive record 23 names this species and its `NCBITaxon:1307906` strain, while the normalized BacDive row is keyed to the strain target. |
| GOLD and strain evidence | `data/raw/gold_organisms.tsv` line 36812 plus exact species and child-strain raw scans | Supported; the GOLD aggregate has `organism_count=6`, and exact scans found the species rows plus the DSM 19596 child-strain rows that generate the nested strain block. |
| Madin et al., StrainInfo, and NCBI type-material attestations | `data/raw/madin_taxa.tsv` line 25231 plus exact StrainInfo and NCBI type-material scans | Supported by 6 Madin et al. assertions, 1 StrainInfo assembly row, 10 StrainInfo related records, 8 direct StrainInfo records, 10 StrainInfo deposit hits, and 9 exact NCBI type-material rows. |
| Empty same-taxon MediaDive/BactoTraits surfaces | Exact scans for `NCBITaxon:483199` | Supported; no committed MediaDive or BactoTraits row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, one related synonym, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs.
- GTDB supplies three intentionally broad species mappings; because each is a pooled `skos:broadMatch`, the mappings remain in `taxonomy_mappings` and do not become exact xrefs.
- BacDive supplies the DSM 19596 child strain that is nested under this species, and StrainInfo contributes additional assembly and related-record overlays.
- GOLD, BV-BRC, GTDB, NCBI Assembly, AllTheBacteria, StrainInfo, and BacDive rows that resolve to this species or its canonical child strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact MediaDive, BactoTraits, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

BacDive record 23 is strain-level for `NCBITaxon:1307906` but also names this parent species; the generated species and strain YAMLs therefore share the same BacDive 23 culture identity.
