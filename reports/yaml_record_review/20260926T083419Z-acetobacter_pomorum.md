# YAML Record Review: Acetobacter pomorum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pomorum.yaml`
- Reviewed UTC: 2026-09-26T08:34:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:65959` |
| label | `Acetobacter pomorum` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated species record under `Acetobacter`. It has source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN; one LPSN nomenclature row; two GTDB `skos:broadMatch` mappings; one NCBITaxon related synonym; one BacDive type-strain row classified at descendant `NCBITaxon:1307917`; three culture collection identifiers; 8 generated genome assemblies; 13 generated genome records; 35 generated related records; and no definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 562443 maps `NCBITaxon:65959` to `acetobacter_pomorum`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pomorum.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pomorum.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pomorum.yaml data/taxa/bacteria/acetobacter_pomorum_dm001.yaml data/taxa/bacteria/acetobacter_pomorum_dsm_11825.yaml data/taxa/bacteria/acetobacter_sacchari.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 8570 has `NCBITaxon:65959`, label `Acetobacter pomorum`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, one related synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 20943 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, species rank, parent, genetic code, source set, snapshot date, and related synonym | `data/raw/ncbitaxon_taxa.tsv` line 8570 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 562443 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 20943 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type strains | `data/raw/lpsn_names.tsv` line 14818 | Supported; LPSN carries this as the correct name, links `GTDB:s__Acetobacter_pomorum`, lists CIP-105762, DSM-11825, and LMG-18848 as type-strain deposits, and supplies accession `INSDC:AJ001632`. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 301427-301428 | Supported exactly by broad matches to `GTDB:s__Acetobacter_oryzifermentans` and `GTDB:s__Acetobacter_pomorum`; the YAML preserves their pooled `skos:broadMatch` scope. |
| BacDive descendant strain | Native BacDive taxon assignments plus `data/raw/bacdive_strains.tsv` line 12 and culture-collection rows for BacDive 11 | Supported; BacDive 11 is anchored at child strain `NCBITaxon:1307917`, and the parent species keeps it with `classified_as: NCBITaxon:1307917`. |
| GOLD and Madin et al. source attestations | `data/raw/gold_organisms.tsv` line 40650, `data/raw/madin_taxa.tsv` line 28578, and native GOLD organism/project/analysis rows | Supported; GOLD has eight direct organisms and seven direct native projects, and Madin et al. has five assertions keyed to the species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, the direct `Acetobacter` parent, the exact 9-ancestor lineage, and one related synonym.
- LPSN supplies the correct-name nomenclature row, three type-strain deposits, and the `GTDB:s__Acetobacter_pomorum` xref.
- GTDB supplies two broad mappings because GTDB species pools overlap this NCBI taxon.
- BacDive supplies one descendant type-strain row for DSM 11825, and deposit matches account for the generated genome records and StrainInfo related-record expansion.
- GOLD supplies eight direct organism rows and Madin et al. supplies five trait assertions.
- NCBI type-material and StrainInfo rows exist for this species; the generated record keeps those as support context and deposit crosslinks rather than direct `source_attestations`.
- No exact same-taxon MediaDive, BactoTraits, or NCBI merged-ID row exists in the committed inventories, and no curator-added `causal_graphs` or definitions are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The species record intentionally mixes direct species evidence with DSM 11825 evidence retained from child strain `NCBITaxon:1307917`. The YAML keeps that boundary explicit with `classified_as` on BacDive 11 and with per-row `taxon_id` values on genome and related records.
