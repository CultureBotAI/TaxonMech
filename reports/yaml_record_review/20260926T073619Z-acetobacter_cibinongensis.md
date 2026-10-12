# YAML Record Review: Acetobacter cibinongensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_cibinongensis.yaml`
- Reviewed UTC: 2026-09-26T07:36:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:146475` |
| label | `Acetobacter cibinongensis` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, Madin et al., and StrainInfo evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, two NCBI related synonyms, two xrefs, one BacDive-derived type-strain entry for the NRIC 0482 child strain, 6 culture collection IDs, 12 genome assemblies, 8 genome records, 38 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 174735 maps `NCBITaxon:146475` to `acetobacter_cibinongensis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_cibinongensis.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_cibinongensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_cibinongensis.yaml data/taxa/bacteria/acetobacter_cibinongensis_nric_0482.yaml data/taxa/bacteria/acetobacter_conturbans.yaml data/taxa/bacteria/acetobacter_estunensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 29732 has `NCBITaxon:146475`, label `Acetobacter cibinongensis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, two related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 21069 keeps the species in scope. `data/raw/ncbi_merged_ids.tsv` line 23760 redirects old ID `NCBITaxon:1670659` into `NCBITaxon:146475`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonyms, old merged ID, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 29732 and `data/raw/ncbi_merged_ids.tsv` line 23760 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 174735 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 21069 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 14800 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 31583 | Supported exactly by one 5-genome `skos:closeMatch` to `GTDB:s__Acetobacter_cibinongensis`. |
| BacDive strain identity | `data/bacdive/records.jsonl.gz` line 15 and `data/raw/bacdive_strains.tsv` line 16 | Supported; BacDive record 15 names this species and its `NCBITaxon:1307904` strain, while the normalized BacDive row is keyed to the strain target. |
| GOLD and strain evidence | `data/raw/gold_organisms.tsv` line 11247 plus exact species and child-strain raw scans | Supported; the GOLD aggregate has `organism_count=10`, and the exact scans found the species rows plus the NRIC 0482 child-strain rows that generate the nested strain block. |
| StrainInfo and NCBI type-material attestations | `data/straininfo/*.tsv`, `data/straininfo/records.jsonl.gz`, and `data/raw/ncbi_type_material.tsv` exact scans | Supported by 1 StrainInfo assembly row, 11 StrainInfo related records, 2 direct StrainInfo records, 8 StrainInfo deposit hits, and 17 exact NCBI type-material rows. |
| Madin et al. attestation and empty same-taxon MediaDive/BactoTraits surfaces | `data/raw/madin_taxa.tsv` line 16825 plus exact auxiliary scans | Supported; Madin et al. has 2 source assertions and no committed MediaDive or BactoTraits row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, two related synonyms, one merged old ID, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive supplies the NRIC 0482 child strain that is nested under this species, and StrainInfo contributes additional assembly and related-record overlays.
- GOLD, BV-BRC, GTDB, NCBI Assembly, StrainInfo, and BacDive rows that resolve to this species or its canonical child strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact MediaDive, BactoTraits, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

BacDive record 15 is strain-level for `NCBITaxon:1307904` but also names this parent species; the generated species and strain YAMLs therefore share the same BacDive 15 culture identity.
