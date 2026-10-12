# YAML Record Review: Acetobacter nitrogenifigens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_nitrogenifigens.yaml`
- Reviewed UTC: 2026-09-26T07:53:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:285268` |
| label | `Acetobacter nitrogenifigens` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, BacDive, StrainInfo, Madin et al., and NCBI type-material evidence. The YAML contains one LPSN nomenclature row, one NCBI related synonym, two xrefs, one BacDive-derived type-strain entry, 9 culture collection IDs, 23 genome assemblies, 17 genome records, 55 related records, and no GTDB taxonomy mappings, generated definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 384993 maps `NCBITaxon:285268` to `acetobacter_nitrogenifigens`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_nitrogenifigens.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_nitrogenifigens.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_nitrogenifigens.yaml data/taxa/bacteria/acetobacter_nitrogenifigens_dsm_23921_nbrc_105050.yaml data/taxa/bacteria/acetobacter_oeni.yaml data/taxa/bacteria/acetobacter_oeni_lmg_21952.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 58097 has `NCBITaxon:285268`, label `Acetobacter nitrogenifigens`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|lpsn|madin_etal`, one related NCBI synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 32184 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 58097 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 384993 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 32184 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 23283 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| BacDive type-strain evidence | `data/bacdive/records.jsonl.gz` line 20 | Supported; BacDive 20 names this species and the child strain `NCBITaxon:1120919`. |
| Madin et al., StrainInfo, and NCBI type-material evidence | `data/raw/madin_taxa.tsv` line 20758 and exact StrainInfo/type-material scans | Supported by 11 Madin et al. assertions, 1 direct StrainInfo record, 1 StrainInfo deposit hit, 7 StrainInfo related records, and 13 exact type-material rows. |
| Empty same-taxon GTDB, GOLD, MediaDive, BactoTraits, raw strain-table, and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:285268` | Supported; no committed row in those processed source tables names this species as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, one related synonym, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs.
- BacDive supplies the generated local type-strain block through BacDive 20, and that BacDive record also names the canonical `NCBITaxon:1120919` child strain.
- BV-BRC, GOLD, GTDB, NCBI Assembly, BacDive, and StrainInfo evidence that resolves through BacDive 20 is represented in the nested strain block as appropriate.
- No exact same-taxon GTDB mapping, processed GOLD aggregate, MediaDive row, BactoTraits row, NCBI merged ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The species has no direct GTDB mapping row, while its DSM 23921 / NBRC 105050 child strain carries the exact GTDB mapping for `GTDB:s__Acetobacter_nitrogenifigens`.
