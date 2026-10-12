# YAML Record Review: Barnettozyma vustinii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/barnettozyma_vustinii.yaml
- Started UTC: 2026-09-21T23:51:01Z
- Finished UTC: 2026-09-21T23:52:15Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:682598 |
| label | Barnettozyma vustinii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:599802 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/barnettozyma_vustinii.yaml`. It carries seven related NCBI synonyms, no exact NCBI synonyms, one BacDive-derived local strain with one StrainInfo assembly and 19 related records, no LPSN nomenclature, no GTDB taxonomy mappings, no causal graphs, and source attestations from BacDive, NCBITAXON, and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*barnettozyma_vustinii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/barnettozyma_vustinii.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/barnettozyma_vustinii.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 160164 has `NCBITaxon:682598`, label `Barnettozyma vustinii`, rank `SPECIES`, direct parent `NCBITaxon:599802`, genetic code `1`, seven related synonyms, no exact synonyms, and sources `bacdive|gold`. `curation/seed_scope.tsv` line 30279 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Barnettozyma` under family `Phaffomycetaceae`.

`data/raw/ncbi_merged_ids.tsv` lines 90761, 92091, 92092, 92093, 92094, 92096, and 92097 map seven old identifiers to the current target. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` has `retired_into` pointing at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 160164 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 30279 | Supported exactly: `attested rule: Barnettozyma vustinii, 3 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| BacDive strain evidence | `data/raw/bacdive_strains.tsv` line 53163 and `data/bacdive/records.jsonl.gz` line 53162 | Supported exactly with one BacDive-derived strain, `kgmicrobe.strain:bacdive_130852`, three local culture collection IDs, and `medium_count: 2`. |
| Culture collection identifiers | Exact scan of `data/raw/culture_collection_strains.tsv` | Supported exactly with `CBS-11554`, `DSM-29255`, and `MUCL-52543`. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 41236 | Supported exactly with four aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:682598`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with four native organisms: `Go0618247`, `Go0618248`, `Go0618249`, and `Go0618250`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one project, `Gp0831022`, for `Go0618249`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to the exact organism or project IDs. |
| GOLD local-strain related records | Exact scan of `data/raw/strain_related_records.tsv` | Supported exactly with 11 GOLD-derived related rows on lines 50663-50673. |
| StrainInfo assembly | `data/straininfo/assemblies.tsv` line 1702 | Supported exactly with assembly `GCA_030569515` matched through deposit `CBS 11554`. |
| StrainInfo generated related records | Exact scan of `data/straininfo/related_records.tsv.gz` | Supported exactly with eight generated rows on lines 27178-27185. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two `culture from holotype` rows for CBS 11554 on lines 256002-256003. |
| NCBI merged IDs | Exact scan of `data/raw/ncbi_merged_ids.tsv` plus retained retired-row scan | Supported exactly; seven raw merges exist but do not produce `replaces` without retained retired taxon rows. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:682598`. |

The BacDive-derived strain has three culture collection IDs and receives one StrainInfo genome assembly, two StrainInfo nucleotide sequence related records, three StrainInfo deposit related records, and three StrainInfo strain related records from `straininfo.strain:368384`. GOLD contributes five `GOLD_ORGANISM` related rows, two `GOLD_PROJECT` rows, two BioProject rows, and two BioSample rows; the duplicate external identifiers are expected because the CBS 11554 organism and project matched both the culture-collection and strain fields.

The native StrainInfo snapshot has one exact direct row under `NCBITaxon:682598` with deposits for MUCL 52543, CBS 11554, and DSM 29255. All three deposits overlay onto BacDive-derived local culture collection IDs, so the generated assembly and related-record surfaces are populated for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Barnettozyma` parent, seven related synonyms, two type-material rows, and seven raw merged-ID rows.
- The raw NCBI merged-ID rows have no corresponding retained retired taxon rows, so no `replaces` values should be generated.
- BacDive supplies one exact local strain with three culture collection identifiers and two media.
- The aggregate GOLD transform supplies a taxon-level organism count of four.
- The local native GOLD snapshot supplies four exact organisms with one project and no joined analyses, and the GOLD local-strain overlay supplies 11 generated related records.
- The native StrainInfo snapshot supplies one genome assembly and eight generated related records.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Barnettozyma vustinii` as `SPECIES`, and the generated record follows the source rank exactly.
