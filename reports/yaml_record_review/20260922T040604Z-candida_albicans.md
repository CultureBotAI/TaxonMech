# YAML Record Review: Candida albicans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candida_albicans.yaml
- Started UTC: 2026-09-22T04:06:04Z
- Finished UTC: 2026-09-22T04:06:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5476 |
| label | Candida albicans |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5475 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/candida_albicans.yaml`. It carries 14 NCBI exact synonyms, 16 NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*candida_albicans.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candida_albicans.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candida_albicans.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2426 has `NCBITaxon:5476`, label `Candida albicans`, rank `SPECIES`, direct parent `NCBITaxon:5475`, genetic code `12`, 14 exact synonyms, 16 related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52003 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent genus `Candida` under family `Debaryomycetaceae`.

The NCBI merged-ID side inventory maps old IDs `NCBITaxon:226999`, `NCBITaxon:300021`, and `NCBITaxon:39399` to `NCBITaxon:5476`, but the retained retired-row inventory is empty for this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2426 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52003 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 38482 | Supported exactly with 46 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5476`. |
| Native GOLD organism evidence | Complete exact native GOLD organism scan | Supported exactly by 53 native GOLD organism rows for `Candida albicans`. |
| Native GOLD project evidence | Complete exact native GOLD project scan joined from exact organism IDs | Supported exactly by 53 native GOLD project rows for the exact organism IDs. |
| Native GOLD analysis evidence | Complete exact native GOLD analysis scan by project IDs | Supported exactly by 35 native GOLD analysis rows joined through exact project IDs. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with three old IDs pointing at `NCBITaxon:5476`. |
| Empty retained retired-row inventory | Exact retained retired-row scan | Supported; no retained retired row points at `NCBITaxon:5476`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 37 type-material rows for `Candida albicans`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5476`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 1,461 deposit-taxonomy hits and 1,225 direct records under `5476`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5476`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5476`. |

The committed aggregate GOLD row contributes 46 organism assertions, while the local native GOLD snapshot currently has 53 exact organism rows, 53 project rows, and 35 joined analysis rows under `5476`.

Native StrainInfo has exact taxon rows under `5476`, but the generated StrainInfo overlay correctly remains empty because no BacDive-derived local strain inventory entry joins those rows.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Candida` genus parent, 14 exact synonyms, 16 related synonyms, and 37 type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of 46.
- The local native GOLD snapshot supplies 53 exact organisms, 53 project rows, and 35 joined analysis rows.
- Native StrainInfo has exact rows under this taxon, but no BacDive-derived local strain inventory entry turns them into generated `data/straininfo/` overlay rows.
- BacDive does not supply exact local strain evidence for this taxon.
- The NCBI merged-ID side inventory has three old IDs, but no retained retired row contributes a generated `replaces` value.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The native GOLD organism, project, and analysis counts exceeded the bounded scan samples, so this review also scanned all three native GOLD gzip JSONL snapshots exactly to recover all 53 organism rows, 53 project rows, and 35 analysis rows.
- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:5476\t' data/raw/ncbi_type_material.tsv` scan to recover all 37 rows.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Candida albicans` as `SPECIES`, and the generated record follows the source rank exactly.
