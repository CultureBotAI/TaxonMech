# YAML Record Review: Aureobasidium pullulans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aureobasidium_pullulans.yaml
- Started UTC: 2026-09-21T22:52:24Z
- Finished UTC: 2026-09-21T22:53:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5580 |
| label | Aureobasidium pullulans |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5579 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/aureobasidium_pullulans.yaml`. It carries four exact NCBI synonyms, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aureobasidium_pullulans.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aureobasidium_pullulans.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aureobasidium_pullulans.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2476 has `NCBITaxon:5580`, label `Aureobasidium pullulans`, rank `SPECIES`, direct parent `NCBITaxon:5579`, genetic code `1`, four exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52038 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aureobasidium` under `Saccotheciaceae`.

`data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:1229722`, `NCBITaxon:178873`, and `NCBITaxon:559562` into `NCBITaxon:5580`, but none of those old IDs has a retained retired row in `data/raw/ncbitaxon_taxa.tsv`; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2476 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52038 | Supported exactly: `attested rule: Aureobasidium pullulans, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 38776 | Supported exactly with one aggregate KG-Microbe GOLD row asserting 58 organisms directly under `NCBITaxon:5580`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 235058-235059 | Supported exactly with two `typematerial.dmp` culture-from-neotype designations for `CBS 584.75` under `Dematium pullulans`. |
| Historical NCBI merges | `data/raw/ncbi_merged_ids.tsv` lines 8708, 28287, and 86319 plus exact retained-old-ID scan | Supported; three old IDs merge into this target but do not generate `replaces` without retained retired NCBI inventory rows. |
| Native GOLD organism evidence | Exact native GOLD organism scan plus targeted complete native GOLD rescan | Supported exactly with 57 organism rows in the local native snapshot, from ATCC 62921 `Go0002478` on line 2223 through Aurpu_var_pul1 `Go0677982` on line 502613. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan plus targeted complete native GOLD rescan | Supported exactly with 64 project rows in the local native snapshot, from `Gp0002478` on line 2253 through `Gp0779823` on line 578860. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs plus targeted complete native GOLD rescan | Supported exactly with 56 native analysis rows joined through the matching project IDs. |
| Native StrainInfo evidence | Exact native StrainInfo direct and deposit-taxonomy scans | Supported with 244 direct native StrainInfo rows and 328 deposit-taxonomy hits under taxon ID `5580`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5580`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5580`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5580`. |

The aggregate GOLD transform asserts 58 organism rows directly under this taxon, while the current local native GOLD snapshot has 57 exact organisms, 64 projects, and 56 joined analysis rows. Native StrainInfo contributes hundreds of exact rows, but none of the native GOLD or StrainInfo rows produce local strain entries because no BacDive-derived strain or generated StrainInfo overlay row is filed under this target.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aureobasidium` parent, four exact synonyms, two related synonyms, the visible merged-ID context, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of 58.
- The local native GOLD snapshot supplies 57 exact organisms with 64 joined projects and 56 joined analysis rows.
- The local native StrainInfo snapshot supplies 244 exact direct rows and 328 deposit-taxonomy hits, but the generated StrainInfo overlay surface is empty for this target.
- BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The native GOLD project scan was expanded beyond the bounded sample to verify all 57 organism IDs, their 64 projects, and their 56 joined analysis rows.
- NCBI ranks `Aureobasidium pullulans` as `SPECIES`, and the generated record follows the source rank exactly.
