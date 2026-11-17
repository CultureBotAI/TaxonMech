# YAML Record Review: Botryosphaeria kuwatsukai

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/botryosphaeria_kuwatsukai.yaml
- Started UTC: 2026-09-22T02:47:53Z
- Finished UTC: 2026-09-22T02:47:53Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2021124 |
| label | Botryosphaeria kuwatsukai |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:45132 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/botryosphaeria_kuwatsukai.yaml`. It carries two NCBI exact synonyms, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*botryosphaeria_kuwatsukai.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/botryosphaeria_kuwatsukai.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/botryosphaeria_kuwatsukai.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 511209 has `NCBITaxon:2021124`, label `Botryosphaeria kuwatsukai`, rank `SPECIES`, direct parent `NCBITaxon:45132`, genetic code `1`, two exact synonyms, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61950 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Botryosphaeria` under family `Botryosphaeriaceae`.

The side merged-ID inventory maps `NCBITaxon:1480134` and `NCBITaxon:760146` into this taxon, but no committed retained retired-row evidence points at it, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 511209 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61950 | Supported exactly: `attested rule: Botryosphaeria kuwatsukai, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 18833 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2021124`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0677899`, for strain KE8637. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one joined project, `Gp0779740`, for strain KE8637. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis, `Botryosphaeria kuwatsukai KE8637`, joined through `Gp0779740`. |
| NCBI merged-ID side inventory | Exact `data/raw/ncbi_merged_ids.tsv` scan | Supported; old IDs `NCBITaxon:1480134` and `NCBITaxon:760146` merge into `NCBITaxon:2021124`, but they are not retained retired rows and therefore do not generate `replaces`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with three epitype designations for `Macrophoma kuwatsukai`: `HMAS 245112`, `HMAS:245112`, and `PG 2`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2021124`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `2021124`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2021124`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2021124`. |

The local native GOLD snapshot has one exact KE8637 organism, one joined project, and one analysis joined through the project ID.

The NCBI type-material inventory contributes three epitype rows for this taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Botryosphaeria` parent, two exact synonyms, four related synonyms, and three epitype rows.
- NCBI supplies two side-inventory old IDs in `data/raw/ncbi_merged_ids.tsv`, but no retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one joined project, and one project-joined analysis.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- Native GOLD analysis rows can join by project ID as well as organism ID; the KE8637 analysis is recovered through `AP PROJECT GOLD IDS`, so it does not require a direct `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Botryosphaeria kuwatsukai` as `SPECIES`, and the generated record follows the source rank exactly.
