# YAML Record Review: Botrytis cinerea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/botrytis_cinerea.yaml
- Started UTC: 2026-09-22T02:59:03Z
- Finished UTC: 2026-09-22T02:59:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:40559 |
| label | Botrytis cinerea |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:33196 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/botrytis_cinerea.yaml`. It carries four NCBI exact synonyms, seven NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*botrytis_cinerea.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/botrytis_cinerea.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/botrytis_cinerea.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4642 has `NCBITaxon:40559`, label `Botrytis cinerea`, rank `SPECIES`, direct parent `NCBITaxon:33196`, genetic code `1`, four exact synonyms, seven related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52444 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Botrytis` under family `Sclerotiniaceae`.

The side merged-ID inventory maps `NCBITaxon:1138823`, `NCBITaxon:1138824`, and `NCBITaxon:1671128` into this taxon, but no committed retained retired-row evidence points at it, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4642 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52444 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34596 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:40559`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two unstrained native organisms, `Go0002498` and `Go0002576`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one joined project, `Gp0002498`, under `Go0002498`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis joins to this taxon by exact organism ID or project ID. |
| NCBI merged-ID side inventory | Exact `data/raw/ncbi_merged_ids.tsv` scan | Supported; old IDs `NCBITaxon:1138823`, `NCBITaxon:1138824`, and `NCBITaxon:1671128` merge into `NCBITaxon:40559`, but they are not retained retired rows and therefore do not generate `replaces`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material designation is filed for `NCBITaxon:40559`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `40559`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 856 deposit-taxonomy hits and 768 direct records under `40559`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:40559`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:40559`. |

The local native GOLD snapshot has two exact unstrained organism rows and one joined project, but no joined analysis.

The NCBI merged-ID side inventory has three old IDs for this taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Botrytis` parent, four exact synonyms, and seven related synonyms.
- NCBI supplies three side-inventory old IDs in `data/raw/ncbi_merged_ids.tsv`, but no retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies two exact organisms, one joined project, and no joined analyses.
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

- Botrytis cinerea has exact native StrainInfo taxon hits at high volume, but this generated TaxonMech record stays strain-count zero because those exact rows did not join to BacDive-derived local strain entries.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Botrytis cinerea` as `SPECIES`, and the generated record follows the source rank exactly.
