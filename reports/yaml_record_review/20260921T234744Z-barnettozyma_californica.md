# YAML Record Review: Barnettozyma californica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/barnettozyma_californica.yaml
- Started UTC: 2026-09-21T23:46:41Z
- Finished UTC: 2026-09-21T23:47:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:36038 |
| label | Barnettozyma californica |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:599802 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/barnettozyma_californica.yaml`. It carries eight NCBI exact synonyms, six related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*barnettozyma_californica.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/barnettozyma_californica.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/barnettozyma_californica.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4047 has `NCBITaxon:36038`, label `Barnettozyma californica`, rank `SPECIES`, direct parent `NCBITaxon:599802`, genetic code `1`, eight exact synonyms, six related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52315 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Barnettozyma` under family `Phaffomycetaceae`.

`data/raw/ncbi_merged_ids.tsv` line 75253 maps old identifier `NCBITaxon:392965` to the current target. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` has `retired_into` pointing at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4047 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52315 | Supported exactly: `attested rule: Barnettozyma californica, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 33259 | Supported exactly with six aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:36038`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with six native organisms: `Go0517089`, `Go0519935`, `Go0519947`, `Go0615499`, `Go0615500`, and `Go0657814`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with four projects across four of the six organism IDs above. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with four analysis rows joining through the four project IDs above. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with seven rows on lines 193787-193793. |
| NCBI merged IDs | `data/raw/ncbi_merged_ids.tsv` line 75253 plus retained retired-row scan | Supported exactly; the raw merge exists but does not produce `replaces` without a retained retired taxon row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `36038`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:36038`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:36038`. |

The NCBI type-material inventory contributes seven `type material` rows under the synonym `Zygohansenula californica` for CBS 252, NCYC 2590, and NRRL Y-17395 designation variants. The local native GOLD snapshot has six exact organisms, with projects and analysis rows for NRRL Y-17395, UCD89, UCD09, and PB4207; strains DSM 3455 and CBS 252 lack matching project rows in the local snapshot.

The native StrainInfo snapshot has 75 exact direct rows and 119 exact deposit rows under `NCBITaxon:36038`, including a type deposit for IFO 0800. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Barnettozyma` parent, eight exact synonyms, six related synonyms, seven type-material rows, and one raw merged-ID row.
- The raw NCBI merged-ID row has no corresponding retained retired taxon row, so no `replaces` value should be generated.
- The aggregate GOLD transform supplies a taxon-level organism count of six.
- The local native GOLD snapshot supplies six exact organisms with four projects and four joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Barnettozyma californica` as `SPECIES`, and the generated record follows the source rank exactly.
