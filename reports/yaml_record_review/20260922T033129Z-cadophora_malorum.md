# YAML Record Review: Cadophora malorum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cadophora_malorum.yaml
- Started UTC: 2026-09-22T03:31:29Z
- Finished UTC: 2026-09-22T03:31:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:108018 |
| label | Cadophora malorum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:210567 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cadophora_malorum.yaml`. It carries two NCBI exact synonyms, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*cadophora_malorum.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cadophora_malorum.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cadophora_malorum.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 19514 has `NCBITaxon:108018`, label `Cadophora malorum`, rank `SPECIES`, direct parent `NCBITaxon:210567`, genetic code `1`, exact synonyms `Phialophora malorum` and `Sporotrichum malorum`, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53727 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cadophora` under family `Ploettnerulaceae`.

`data/raw/ncbi_merged_ids.tsv` lines 72855 and 92181 record side-inventory old IDs `NCBITaxon:364364` and `NCBITaxon:685540` merged into `NCBITaxon:108018`, but the retained NCBI row for this generated record is current and has no `retired_into` value. The record correctly omits `replaces`, which is generated only from retained retired rows.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 19514 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53727 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 1488 | Supported exactly with four aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:108018`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0384301`, `Go0631248`, `Go0641303`, and `Go0641304` for four `Cadophora malorum` strains. |
| Native GOLD project evidence | Complete exact native GOLD project scan joined from exact organism IDs | Supported exactly by 26 project rows for the four exact organism IDs. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by two analysis rows joined through projects `Gp0235393` and `Gp0644557`. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with old IDs `NCBITaxon:364364` and `NCBITaxon:685540` pointing to the current taxon. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material row mentions `NCBITaxon:108018`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `108018`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 73 deposit-taxonomy hits and 55 direct records under `108018`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:108018`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:108018`. |

The committed aggregate GOLD row is mirrored by four exact native GOLD organism rows, 26 native project rows, and two analysis rows joined through those projects.

Native StrainInfo has exact taxon rows under `108018`, but the generated StrainInfo overlay correctly remains empty because no BacDive-derived local strain inventory entry joins those rows.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cadophora` parent, two exact synonyms, and four related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of four.
- The local native GOLD snapshot supplies four exact organisms, 26 project rows, and two joined analysis rows.
- Native StrainInfo has exact rows under this taxon, but no BacDive-derived local strain inventory entry turns them into generated `data/straininfo/` overlay rows.
- BacDive does not supply exact local strain evidence for this taxon.
- NCBI type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The native GOLD project count exceeded the bounded scan sample, so this review also scanned `data/gold/projects.jsonl.gz` exactly for `Go0384301`, `Go0631248`, `Go0641303`, and `Go0641304` to recover all 26 rows.
- The side-inventory NCBI merge rows for `NCBITaxon:364364` and `NCBITaxon:685540` do not require YAML `replaces` entries without retained retired source rows.
- Exact local native GOLD scans recovered four organism rows, 26 project rows, and two analysis rows for `NCBITaxon:108018`.
- GOLD analysis rows for strains `Mo12` and `M34` join through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Cadophora malorum` as `SPECIES`, and the generated record follows the source rank exactly.
