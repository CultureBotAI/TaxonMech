# YAML Record Review: Acetobacter pasteurianus NBRC 3279

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3279.yaml`
- Reviewed UTC: 2026-09-26T08:20:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1226659` |
| label | `Acetobacter pasteurianus NBRC 3279` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:438` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a compact generated strain record under `Acetobacter pasteurianus`. It has source attestations from NCBITAXON and GTDB; one exact GTDB synonym; one GTDB `skos:closeMatch`; one GTDB xref; and no generated local strains, genome assemblies, genome records, related records, LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 76104 maps `NCBITaxon:1226659` to `acetobacter_pasteurianus_nbrc_3279`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pasteurianus_nbrc_3279.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3279.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3277.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3278.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3279.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3280.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 279633 has `NCBITaxon:1226659`, label `Acetobacter pasteurianus NBRC 3279`, rank `STRAIN`, parent `NCBITaxon:438`, genetic code `11`, source set `ncbitaxon|gtdb`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 66401 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 279633 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 76104 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 66401 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 12860 | Supported exactly by one 31-genome `skos:closeMatch` to `GTDB:s__Acetobacter_pasteurianus`. |
| Native GOLD snapshot and processed aggregate | `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, `data/gold/analyses.jsonl.gz`, and exact `data/raw/gold_organisms.tsv` scan | Native GOLD has one exact organism row for `NCBITaxon:1226659` and two attached project/analysis rows; no processed GOLD aggregate row names this strain, so no GOLD source attestation is generated. |
| Empty auxiliary evidence | Exact scans of BacDive, culture-collection, raw strain, StrainInfo, LPSN, MediaDive, Madin et al., BactoTraits, NCBI type-material, and NCBI merged-ID surfaces for `NCBITaxon:1226659` | Supported; no committed auxiliary row names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter pasteurianus` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, exact synonym, xref, and GENOME source attestation.
- Native GOLD contains organism `Go0174790` and project `Gp0494895`, plus a second project row whose name does not match this strain; no processed GOLD aggregate row names this taxon.
- No exact same-taxon BacDive, culture collection, processed GOLD aggregate, LPSN, MediaDive, Madin et al., BactoTraits, StrainInfo, NCBI type-material, raw strain, or NCBI merged-ID row exists in the committed processed inventories.
- With `strain_count: 0`, no BacDive-derived or overlay strain rows, and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and product sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The native GOLD workbook links `Go0174790` both to `Gp0494895` for NBRC 3279 and to `Gp0495803`, whose project and analysis name is `New Jersey aster yellows phytoplasma NJAY`; neither row is promoted into the processed taxon-level GOLD aggregate.
