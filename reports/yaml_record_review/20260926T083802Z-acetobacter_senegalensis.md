# YAML Record Review: Acetobacter senegalensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_senegalensis.yaml`
- Reviewed UTC: 2026-09-26T08:38:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:446692` |
| label | `Acetobacter senegalensis` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated species record under `Acetobacter`. It has source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN; one LPSN nomenclature row; one GTDB `skos:closeMatch`; one NCBITaxon related synonym; one BacDive type-strain row classified at descendant `NCBITaxon:1307918`; two culture collection identifiers; 18 generated genome assemblies; 14 generated genome records; 48 generated related records; and no definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 507199 maps `NCBITaxon:446692` to `acetobacter_senegalensis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_senegalensis.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_senegalensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_senegalensis.yaml data/taxa/bacteria/acetobacter_senegalensis_dsm_18889.yaml data/taxa/bacteria/acetobacter_sicerae.yaml data/taxa/bacteria/acetobacter_sp.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 99417 has `NCBITaxon:446692`, label `Acetobacter senegalensis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, one related synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 21407 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, species rank, parent, genetic code, source set, snapshot date, and related synonym | `data/raw/ncbitaxon_taxa.tsv` line 99417 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 507199 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 21407 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type strains | `data/raw/lpsn_names.tsv` line 23561 | Supported; LPSN carries this as the correct name, links `GTDB:s__Acetobacter_senegalensis`, lists DSM-120446 and LMG-23690 as type-strain deposits, and supplies accession `INSDC:AY883036`. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 290046 | Supported exactly by one 17-genome `skos:closeMatch` to `GTDB:s__Acetobacter_senegalensis`. |
| BacDive descendant strain | Native BacDive taxon assignments plus `data/raw/bacdive_strains.tsv` line 22 and direct strain-genome rows | Supported; BacDive 21 links both the species and child strain `NCBITaxon:1307918`, and the generated species row preserves the child placement with `classified_as: NCBITaxon:1307918`. |
| GOLD and Madin et al. source attestations | `data/raw/gold_organisms.tsv` line 35747, `data/raw/madin_taxa.tsv` line 24410, and native GOLD organism/project/analysis rows | Supported; GOLD has four direct organisms and three direct native projects, and Madin et al. has seven assertions keyed to this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, direct `Acetobacter` parent, exact 9-ancestor lineage, and one related synonym.
- LPSN supplies the correct-name nomenclature row and the `GTDB:s__Acetobacter_senegalensis` xref.
- GTDB supplies the only taxonomy mapping as `skos:closeMatch`.
- BacDive supplies one type-strain cluster around LMG 23690 and DSM 18889; the species record keeps exact species rows, child DSM 18889 rows, and StrainInfo deposit expansion from BacDive 21 with explicit per-row `taxon_id` values.
- GOLD supplies four direct organism aggregates and Madin et al. supplies seven direct assertions.
- NCBI type-material and StrainInfo rows exist for this species; the generated record uses them as deposit and related-record context rather than direct top-level source attestations.
- No exact same-taxon MediaDive, BactoTraits, or NCBI merged-ID row exists in the committed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The BacDive 21 cluster is also represented directly on `Acetobacter senegalensis DSM 18889`; the parent species retains it as the LPSN-supported type-strain cluster while preserving the strain taxon on the child-specific rows.
