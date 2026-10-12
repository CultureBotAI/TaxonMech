# YAML Record Review: Backusella dispersa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/backusella_dispersa.yaml
- Started UTC: 2026-09-21T23:34:34Z
- Finished UTC: 2026-09-21T23:36:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2583355 |
| label | Backusella dispersa |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:64649 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/backusella_dispersa.yaml`. It carries one NCBI exact synonym, three related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*backusella_dispersa.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/backusella_dispersa.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/backusella_dispersa.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 533767 has `NCBITaxon:2583355`, label `Backusella dispersa`, rank `SPECIES`, direct parent `NCBITaxon:64649`, genetic code `1`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 62856 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Backusella` under family `Backusellaceae`.

`data/raw/ncbi_merged_ids.tsv` line 44991 maps old identifier `NCBITaxon:2572691` to the current target. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` has `retired_into` pointing at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 533767 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62856 | Supported exactly: `attested rule: Backusella dispersa, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 23608 | Supported exactly with seven aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:2583355`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with seven native organisms: `Go0456225`, `Go0470963`, `Go0470964`, `Go0527626`, `Go0527627`, `Go0535949`, and `Go0535981`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with seven resequencing projects across the seven organism IDs above. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to these exact organism or project IDs. |
| NCBI merged IDs | `data/raw/ncbi_merged_ids.tsv` line 44991 plus retained retired-row scan | Supported exactly; the raw merge exists but does not produce `replaces` without a retained retired taxon row. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no exact type-material row was filed under `NCBITaxon:2583355`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2583355`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2583355`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2583355`. |

The local native GOLD snapshot has seven exact organisms and seven exact resequencing projects for strains NRRL 6038, NRRL 6039, NRRL 6045, NRRL 6046, NRRL 6047, NRRL 1402, and NRRL 3106. No native analysis row joins to those organism or project IDs in the committed snapshot.

The native StrainInfo snapshot has one exact direct row under `NCBITaxon:2583355` with one non-type deposit, CGMCC 3.0177. It does not overlay onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Backusella` parent, one exact synonym, three related synonyms, and one raw merged-ID row.
- The raw NCBI merged-ID row has no corresponding retained retired taxon row, so no `replaces` value should be generated.
- NCBI does not supply type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of seven.
- The local native GOLD snapshot supplies seven exact organisms with seven projects and no joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and the one exact native StrainInfo row correctly has no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Backusella dispersa` as `SPECIES`, and the generated record follows the source rank exactly.
