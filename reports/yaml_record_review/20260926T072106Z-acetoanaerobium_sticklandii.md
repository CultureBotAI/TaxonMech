# YAML Record Review: Acetoanaerobium sticklandii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetoanaerobium_sticklandii.yaml`
- Reviewed UTC: 2026-09-26T07:21:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1511` |
| label | `Acetoanaerobium sticklandii` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:186831` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, Madin et al., and canonical strain evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, four synonyms, two xrefs, one BacDive-derived type-strain entry, 6 culture collection IDs, 10 genome assemblies, 7 genome records, 43 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 192428 maps `NCBITaxon:1511` to `acetoanaerobium_sticklandii`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetoanaerobium_sticklandii.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetoanaerobium_sticklandii.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetoanaerobium_sp_wjdl_y2.yaml data/taxa/bacteria/acetoanaerobium_sticklandii.yaml data/taxa/bacteria/acetoanaerobium_sticklandii_dsm_519.yaml data/taxa/bacteria/acetobacter_aceti.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 1179 has `NCBITaxon:1511`, label `Acetoanaerobium sticklandii`, rank `SPECIES`, parent `NCBITaxon:186831`, genetic code `11`, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, exact synonym `Clostridium sticklandii`, two NCBI related synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 20768 keeps the taxon in scope. `data/raw/gtdb_mappings.tsv` line 33112 maps `GTDB:s__Acetoanaerobium_sticklandii` to `NCBITaxon:1511` with `skos:closeMatch` and 2 genomes, and `data/raw/lpsn_names.tsv` line 31382 carries the LPSN correct-name row with the same NCBI taxon and the same GTDB species ID.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, exact and related synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 1179 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 192428 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 20768 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature, LPSN synonym, type-strain identifiers, and nomenclatural publication accessions | `data/raw/lpsn_names.tsv` line 31382 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 33112 | Supported exactly by one 2-genome `skos:closeMatch`. |
| GOLD organism count and GOLD project evidence | `data/raw/gold_organisms.tsv` line 11917 plus exact native GOLD scans | Supported; the aggregate has `organism_count=2`, and the native GOLD tables contain 2 matching organism rows, 1 project row, and 1 analysis row for this taxon. |
| BacDive type-strain evidence | `data/bacdive/records.jsonl.gz` line 2617 and `data/raw/ncbi_type_material.tsv` exact rows | Supported; BacDive record 2717 names this species and strain `NCBITaxon:499177`, and 16 NCBI type-material rows for `NCBITaxon:1511` are all `type strain` rows. |
| Canonical strain and genome evidence | Exact scans of `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/*.tsv` for `NCBITaxon:1511` | Supported; 7 raw strain assemblies, 5 raw genome records, 16 raw related records, 1 StrainInfo assembly, and 15 StrainInfo related records contribute to the single generated BacDive strain block. |
| Madin et al. trait attestation | `data/raw/madin_taxa.tsv` line 17056 | Supported exactly with 6 source assertions. |
| Empty MediaDive, BactoTraits, and NCBI merged-id surfaces | Exact scans for `NCBITaxon:1511` | Supported; there are no exact same-taxon MediaDive, BactoTraits, or merged-old-ID rows for this species. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the primary identity, the direct parent, two synonym strings, and the exact 9-ancestor bacterial lineage.
- LPSN supplies the nomenclature assertion, one related synonym, two xrefs, a sequence accession, publication accessions, and a type-strain identifier set for the species.
- GTDB supplies the only taxonomy mapping, a 2-genome `skos:closeMatch` to `GTDB:s__Acetoanaerobium_sticklandii`.
- GOLD, BV-BRC, GTDB, NCBI Assembly, StrainInfo, and BacDive records all resolve onto the single canonical BacDive 2717 DSM 519 type-strain block represented in YAML.
- No same-taxon MediaDive, BactoTraits, ATB, or NCBI merged-id evidence is present, and the record correctly has no generated definitions or curator-added causal graphs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The generated species record and the generated `NCBITaxon:499177` strain record both aggregate evidence for the DSM 519 culture through the same BacDive 2717 strain identity; the difference is in the target NCBI taxon that seeded each YAML file.
