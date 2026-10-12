# YAML Record Review: Acetobacter peroxydans

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_peroxydans.yaml`
- Reviewed UTC: 2026-09-26T08:30:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:104098` |
| label | `Acetobacter peroxydans` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated species record under `Acetobacter`. It has source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS; one LPSN nomenclature row; one GTDB `skos:closeMatch`; two related synonyms; one BacDive type-strain row with 16 culture collection identifiers; 40 generated genome assemblies; 29 generated genome records; 145 generated related records; and no definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 16126 maps `NCBITaxon:104098` to `acetobacter_peroxydans`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_peroxydans.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_peroxydans.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_peroxydans.yaml data/taxa/bacteria/acetobacter_peroxydans_nbrc_13755.yaml data/taxa/bacteria/acetobacter_persici.yaml data/taxa/bacteria/acetobacter_persici_jcm_25330.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 18601 has `NCBITaxon:104098`, label `Acetobacter peroxydans`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, one NCBITaxon related synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 2035 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, species rank, parent, genetic code, source set, snapshot date, and related synonym | `data/raw/ncbitaxon_taxa.tsv` line 18601 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 16126 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 2035 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type strains | `data/raw/lpsn_names.tsv` line 14817 | Supported; LPSN preserves this name as a validly published legitimate synonym of the accepted pasteurianus concept, carries the GTDB mapping, lists ATCC-12874, DSM-2347, IFO-13755, LMG-1635, and NBRC-13755 as type-strain deposits, and supplies accession `INSDC:AB680509`. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 1555 | Supported exactly by one 18-genome `skos:closeMatch` to `GTDB:s__Acetobacter_peroxydans`. |
| BacDive strain, culture IDs, assemblies, genome records, and related crosslinks | `data/raw/bacdive_strains.tsv` line 25, culture-collection rows for BacDive 24, raw strain rows, and StrainInfo deposit rows | Supported; BacDive 24 supplies the direct type strain, and matched deposits account for the generated strain and related-record expansion. |
| GOLD, MediaDive, Madin et al., and BactoTraits source attestations | `data/raw/gold_organisms.tsv` line 571, `data/raw/mediadive_taxa.tsv` line 161, `data/raw/madin_taxa.tsv` line 765, `data/raw/bactotraits_taxa.tsv` line 120, and native GOLD organism/project rows | Supported; GOLD has three direct organism aggregates and two native direct projects, and the auxiliary trait/media rows are directly keyed to `NCBITaxon:104098`. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, the direct `Acetobacter` parent, the exact 9-ancestor lineage, and one related synonym.
- LPSN supplies the second related synonym through the accepted `Acetobacter pasteurianus` nomenclatural concept.
- GTDB supplies the only taxonomy mapping as `skos:closeMatch`.
- BacDive supplies one exact type-strain record and the 16 culture collection identifiers that fan out to the generated assemblies, genome records, and related records, including deposit-level crosslinks around `NCBITaxon:438` and child strain `NCBITaxon:1307915`.
- GOLD, MediaDive, Madin et al., and BactoTraits each have committed source rows keyed directly to this species.
- StrainInfo contributes deposit evidence but no exact direct target row for the species.
- No NCBI merged-ID row exists for this species, and no curator-added `causal_graphs` or definitions are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The generated related records intentionally include direct same-taxon evidence plus strain/deposit crosslinks from the BacDive culture IDs. Those crosslinks should be read as deposit expansion around BacDive 24, not as independent direct source attestations for every linked NCBITaxon identifier.
