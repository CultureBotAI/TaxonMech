# YAML Record Review: Acetobacter pomorum DM001

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pomorum_dm001.yaml`
- Reviewed UTC: 2026-09-26T08:34:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:945681` |
| label | `Acetobacter pomorum DM001` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:65959` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a compact generated strain record under `Acetobacter pomorum`. It has source attestations from NCBITAXON, GTDB, and MADIN; one GTDB `skos:closeMatch`; three exact synonyms from NCBI and GTDB; one GTDB xref; and no generated local strains, genome assemblies, genome records, related records, LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 618266 maps `NCBITaxon:945681` to `acetobacter_pomorum_dm001`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pomorum_dm001.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pomorum_dm001.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pomorum.yaml data/taxa/bacteria/acetobacter_pomorum_dm001.yaml data/taxa/bacteria/acetobacter_pomorum_dsm_11825.yaml data/taxa/bacteria/acetobacter_sacchari.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 202403 has `NCBITaxon:945681`, label `Acetobacter pomorum DM001`, rank `STRAIN`, parent `NCBITaxon:65959`, genetic code `11`, source set `ncbitaxon|gtdb|madin_etal`, two NCBITaxon exact synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 35386 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, snapshot date, and exact synonyms | `data/raw/ncbitaxon_taxa.tsv` line 202403 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 618266 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 35386 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping and synonym | `data/raw/gtdb_mappings.tsv` line 321161 | Supported exactly by one 28-genome `skos:closeMatch` to `GTDB:s__Acetobacter_oryzifermentans`. |
| Madin et al. source attestation | `data/raw/madin_taxa.tsv` line 33271 | Supported exactly by one direct assertion keyed to this strain. |
| Native GOLD context | `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, `data/gold/analyses.jsonl.gz`, and exact `data/raw/gold_organisms.tsv` scan | Native GOLD has one exact organism/project/analysis chain through `Go0008488` and `Gp0008488`; no processed GOLD aggregate row names this strain, so no GOLD source attestation is generated. |
| Empty auxiliary evidence | Exact scans of BacDive, culture-collection, raw strain, StrainInfo, LPSN, MediaDive, BactoTraits, NCBI type-material, NCBI merged-ID, and processed GOLD aggregate surfaces for `NCBITaxon:945681` | Supported; no committed auxiliary row names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter pomorum` parent, the exact 10-ancestor lineage, and two exact synonyms.
- GTDB supplies the taxonomy mapping, one exact synonym, one xref, and the GENOME source attestation.
- Madin et al. supplies the one direct trait assertion that keeps the compact strain in scope.
- Native GOLD contains one exact organism/project/analysis chain, but no processed GOLD aggregate row is keyed to this taxon.
- No exact same-taxon BacDive, culture collection, processed GOLD aggregate, LPSN, MediaDive, BactoTraits, StrainInfo, NCBI type-material, raw strain, or NCBI merged-ID row exists in the committed processed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This record is generated from NCBI, GTDB, and Madin rows only, so its empty strain and genome sections are expected even though a native GOLD organism exists outside the processed aggregate.
