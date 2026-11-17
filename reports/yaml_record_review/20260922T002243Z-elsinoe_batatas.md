# YAML Record Review: Elsinoe batatas

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/elsinoe_batatas.yaml
- Started UTC: 2026-09-22T00:21:15Z
- Finished UTC: 2026-09-22T00:22:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2601811 |
| label | Elsinoe batatas |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:40996 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/elsinoe_batatas.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*elsinoe_batatas.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/elsinoe_batatas.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/elsinoe_batatas.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 535723 has `NCBITaxon:2601811`, label `Elsinoe batatas`, rank `SPECIES`, direct parent `NCBITaxon:40996`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 62889 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Elsinoe` under family `Elsinoaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 535723 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62889 | Supported exactly: `attested rule: Elsinoe batatas, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 23906 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2601811`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0632174`, strain CRI-CJ2. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one project, `Gp0645998`, for `Go0632174`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row joining through project `Gp0645998`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no exact type-material row was filed under `NCBITaxon:2601811`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2601811`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2601811`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2601811`. |

The local native GOLD snapshot has one exact organism, CRI-CJ2, with one joined project and one joined analysis row. NCBI contributes no type-material rows, no raw merged-ID rows, and no retained retired rows for this taxon.

No exact native StrainInfo rows were filed under `NCBITaxon:2601811`, and the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Elsinoe` parent, and one related synonym.
- NCBI does not supply merged-ID or type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and one joined analysis.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Elsinoe batatas` as `SPECIES`, and the generated record follows the source rank exactly.
