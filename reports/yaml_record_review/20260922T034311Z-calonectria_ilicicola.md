# YAML Record Review: Calonectria ilicicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/calonectria_ilicicola.yaml
- Started UTC: 2026-09-22T03:43:11Z
- Finished UTC: 2026-09-22T03:43:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:182845 |
| label | Calonectria ilicicola |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2779503 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/calonectria_ilicicola.yaml`. It carries one NCBI exact synonym, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*calonectria_ilicicola.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/calonectria_ilicicola.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/calonectria_ilicicola.yaml` exited successfully and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 36555 has `NCBITaxon:182845`, label `Calonectria ilicicola`, rank `SPECIES`, direct parent `NCBITaxon:2779503`, genetic code `1`, exact synonym `Cylindrocladium parasiticum`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 54370 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Calonectria kyotensis species complex` under genus `Calonectria`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:182845`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 36555 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54370 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 16211 | Supported exactly with 32 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:182845`. |
| Native GOLD organism evidence | Complete exact native GOLD organism scan | Supported exactly by 32 native GOLD organism rows for `Calonectria ilicicola`. |
| Native GOLD project evidence | Complete exact native GOLD project scan joined from exact organism IDs | Supported exactly by 32 native GOLD project rows for the exact organism IDs. |
| Native GOLD analysis evidence | Complete exact native GOLD analysis scan by project IDs | Supported exactly by 32 native GOLD analysis rows joined through the exact project IDs. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:182845`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 22 type-material rows for `Calonectria ilicicola`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `182845`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 18 deposit-taxonomy hits and 13 direct records under `182845`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:182845`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:182845`. |

The committed aggregate GOLD row is mirrored by 32 exact native GOLD organisms, 32 native project rows, and 32 native analysis rows.

Native StrainInfo has exact taxon rows under `182845`, but the generated StrainInfo overlay correctly remains empty because no BacDive-derived local strain inventory entry joins those rows.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Calonectria kyotensis species complex` parent, one exact synonym, one related synonym, and 22 type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of 32.
- The local native GOLD snapshot supplies 32 exact organisms, 32 project rows, and 32 joined analysis rows.
- Native StrainInfo has exact rows under this taxon, but no BacDive-derived local strain inventory entry turns them into generated `data/straininfo/` overlay rows.
- BacDive does not supply exact local strain evidence for this taxon.
- NCBI merged-ID, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The native GOLD organism, project, and analysis counts exceeded the bounded scan samples, so this review also scanned all three native GOLD gzip JSONL snapshots exactly to recover all 32 rows on each surface.
- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:182845\t' data/raw/ncbi_type_material.tsv` scan to recover all 22 rows.
- The first attempted complete GOLD analysis scan had an over-broad `jq` predicate and was discarded; the second pass used the exact 32 project IDs and recovered the expected 32 rows.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Calonectria ilicicola` as `SPECIES`, and the generated record follows the source rank exactly.
