# YAML Record Review: Acetobacter lovaniensis NRIC 0474

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_lovaniensis_nric_0474.yaml`
- Reviewed UTC: 2026-09-26T07:49:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307909` |
| label | `Acetobacter lovaniensis NRIC 0474` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:104100` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a compact generated strain record under `Acetobacter lovaniensis`. It has source attestations from NCBITAXON and GTDB; one exact GTDB synonym; one GTDB `skos:closeMatch`; one GTDB xref; and no generated local strains, genome assemblies, genome records, related records, LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107654 maps `NCBITaxon:1307909` to `acetobacter_lovaniensis_nric_0474`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_lovaniensis_nric_0474.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_lovaniensis_nric_0474.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_lovaniensis_nric_0474.yaml data/taxa/bacteria/acetobacter_malorum.yaml data/taxa/bacteria/acetobacter_malorum_dsm_14337.yaml data/taxa/bacteria/acetobacter_musti.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309513 has `NCBITaxon:1307909`, label `Acetobacter lovaniensis NRIC 0474`, rank `STRAIN`, parent `NCBITaxon:104100`, genetic code `11`, source set `ncbitaxon|gtdb`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 67315 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 309513 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107654 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 67315 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 17789 | Supported exactly by one 16-genome `skos:closeMatch` to `GTDB:s__Acetobacter_lovaniensis`. |
| Empty auxiliary evidence | Exact scans of BacDive, culture-collection, raw strain, StrainInfo, GOLD, LPSN, MediaDive, Madin et al., BactoTraits, NCBI type-material, and NCBI merged-ID surfaces for `NCBITaxon:1307909` | Supported; no committed auxiliary row names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter lovaniensis` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, exact synonym, xref, and non-NCBI source attestation.
- No exact same-taxon BacDive, culture collection, GOLD, LPSN, MediaDive, Madin et al., BactoTraits, StrainInfo, NCBI type-material, or NCBI merged-ID row exists in the committed source inventories.
- With `strain_count: 0`, no BacDive-derived or overlay strain rows, and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and product sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This record is distinct from the BacDive-backed `Acetobacter lovaniensis` species type-strain block; no processed source row links `NCBITaxon:1307909` to that local strain identity.
