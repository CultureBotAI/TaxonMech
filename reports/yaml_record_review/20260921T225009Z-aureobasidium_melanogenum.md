# YAML Record Review: Aureobasidium melanogenum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aureobasidium_melanogenum.yaml
- Started UTC: 2026-09-21T22:48:35Z
- Finished UTC: 2026-09-21T22:50:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:46634 |
| label | Aureobasidium melanogenum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5579 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/aureobasidium_melanogenum.yaml`. It carries two exact NCBI synonyms, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aureobasidium_melanogenum.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aureobasidium_melanogenum.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aureobasidium_melanogenum.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 5869 has `NCBITaxon:46634`, label `Aureobasidium melanogenum`, rank `SPECIES`, direct parent `NCBITaxon:5579`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52710 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aureobasidium` under `Saccotheciaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 5869 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52710 | Supported exactly: `attested rule: Aureobasidium melanogenum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 36340 | Supported exactly with one aggregate KG-Microbe GOLD row asserting 50 organisms directly under `NCBITaxon:46634`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 217846-217847 | Supported exactly with two `typematerial.dmp` culture-from-type-material designations for `CBS 105.22`. |
| Native GOLD organism evidence | Exact native GOLD organism scan plus targeted complete native GOLD rescan | Supported exactly with 49 organism rows in the local native snapshot, from HN6.2 `Go0384797` on line 280202 through EXF-8016 `Go0631753` on line 462239. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan plus targeted complete native GOLD rescan | Supported exactly with 49 project rows in the local native snapshot, from `Gp0235921` on line 156686 through `Gp0645355` on line 482302. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs plus targeted complete native GOLD rescan | Supported exactly with 49 native analysis rows joined through the matching project IDs. |
| Native StrainInfo evidence | Exact native StrainInfo direct and deposit-taxonomy scans | Supported with 41 direct native StrainInfo rows and 59 deposit-taxonomy hits under taxon ID `46634`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:46634`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `46634`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:46634`. |

The aggregate GOLD transform asserts 50 organism rows directly under this taxon, while the current local native GOLD snapshot has 49 exact organism/project/analysis triplets. Native StrainInfo contributes many exact rows, but none of the native GOLD or StrainInfo rows produce local strain entries because no BacDive-derived strain or generated StrainInfo overlay row is filed under this target.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aureobasidium` parent, two exact synonyms, two related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of 50.
- The local native GOLD snapshot supplies 49 exact organisms with 49 joined projects and 49 joined analysis rows.
- The local native StrainInfo snapshot supplies 41 exact direct rows and 59 deposit-taxonomy hits, but the generated StrainInfo overlay surface is empty for this target.
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
- The native GOLD project scan was expanded beyond the bounded sample to verify all 49 organism IDs, their 49 projects, and their 49 joined analysis rows.
- NCBI ranks `Aureobasidium melanogenum` as `SPECIES`, and the generated record follows the source rank exactly.
