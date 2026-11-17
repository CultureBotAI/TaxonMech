# YAML Record Review: Acetobacter papayae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_papayae.yaml`
- Reviewed UTC: 2026-09-26T08:05:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1076592` |
| label | `Acetobacter papayae` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, StrainInfo, and NCBI type-material evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, two NCBI related synonyms, two xrefs, two BacDive-derived local strains, 7 culture collection IDs, 10 genome assemblies, 8 genome records, 28 related records, and no generated definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 24157 maps `NCBITaxon:1076592` to `acetobacter_papayae`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_papayae.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_papayae.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_oryzoeni.yaml data/taxa/bacteria/acetobacter_papayae.yaml data/taxa/bacteria/acetobacter_papayae_jcm_25143.yaml data/taxa/bacteria/acetobacter_pasteurianus.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 230854 has `NCBITaxon:1076592`, label `Acetobacter papayae`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, two related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 14870 keeps the species in scope. `data/raw/ncbi_merged_ids.tsv` line 2564 redirects old ID `NCBITaxon:1076593` into `NCBITaxon:1076592`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonyms, old merged ID, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 230854 and `data/raw/ncbi_merged_ids.tsv` line 2564 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 24157 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 14870 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 27329 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 2867 | Supported exactly by one 7-genome `skos:closeMatch` to `GTDB:s__Acetobacter_papayae`. |
| BacDive, GOLD, StrainInfo, and NCBI type-material evidence | Exact BacDive, GOLD, raw strain-table, StrainInfo, and type-material scans | Supported by two BacDive records, `organism_count=1`, one StrainInfo assembly row, 6 StrainInfo related records, 3 direct StrainInfo records, 4 StrainInfo deposit hits, and 7 exact type-material rows. |
| Empty same-taxon MediaDive, BactoTraits, and Madin et al. surfaces | Exact scans for `NCBITaxon:1076592` | Supported; no committed row in those processed source tables names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, two related synonyms, one merged old ID, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive supplies two generated local strain blocks, including one BacDive record that also names the canonical child strain `NCBITaxon:1234671`.
- GOLD, BV-BRC, GTDB, NCBI Assembly, BacDive, and StrainInfo rows that resolve to this species or to the JCM 25143 / LMG 26456 child strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact MediaDive, BactoTraits, Madin et al., generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The generated species record correctly carries both the child-strain BacDive block and the additional species-keyed BacDive block for the JCM 25144 / NRIC 0656 local strain.
