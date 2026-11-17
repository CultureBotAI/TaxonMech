# YAML Record Review: Blumeria graminis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/blumeria_graminis.yaml
- Started UTC: 2026-09-22T02:28:31Z
- Finished UTC: 2026-09-22T02:28:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:34373 |
| label | Blumeria graminis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:34372 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/blumeria_graminis.yaml`. It carries one NCBI exact synonym, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*blumeria_graminis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/blumeria_graminis.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/blumeria_graminis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 3837 has `NCBITaxon:34373`, label `Blumeria graminis`, rank `SPECIES`, direct parent `NCBITaxon:34372`, genetic code `1`, one exact synonym, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52273 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Blumeria` under family `Erysiphaceae`.

The side merged-ID inventory maps `NCBITaxon:1961886` and `NCBITaxon:5122` into this taxon, but no committed retained retired-row evidence points at it, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 3837 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52273 | Supported exactly: `attested rule: Blumeria graminis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 32854 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:34373`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms: `Go0002497`, and `Go0373437` for strain 5874. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with two joined projects: `Gp0002497`, and `Gp0220538` for strain 5874. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins through exact `NCBITaxon:34373` organism or project IDs. |
| NCBI merged-ID side inventory | Exact `data/raw/ncbi_merged_ids.tsv` scan | Supported; old IDs `NCBITaxon:1961886` and `NCBITaxon:5122` merge into `NCBITaxon:34373`, but they are not retained retired rows and therefore do not generate `replaces`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six neotype designations for `Erysiphe graminis`: `MUMH 1707`, `MUMH:1707`, `MUMH<JPN> 1707`, `MUMH<JPN>-1707`, `MUMH<JPN>1707`, and `MUMH<JPN>:1707`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `34373`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `34373`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:34373`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:34373`. |

The local native GOLD snapshot has two exact organisms and two joined projects, while the aggregate GOLD transform contributes one source assertion for this taxon-level record.

The NCBI type-material inventory contributes six neotype rows for this taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Blumeria` parent, one exact synonym, four related synonyms, and six neotype rows.
- NCBI supplies two side-inventory old IDs in `data/raw/ncbi_merged_ids.tsv`, but no retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies two exact organisms and two joined projects, with no joined analyses.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the generated aggregate count can differ from local native GOLD rows joined by exact `ORGANISM NCBI TAX ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Blumeria graminis` as `SPECIES`, and the generated record follows the source rank exactly.
