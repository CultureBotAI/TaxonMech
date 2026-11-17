# YAML Record Review: Trichoderma lacuwombatense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/trichoderma_lacuwombatense.yaml
- Started UTC: 2026-09-22T00:35:15Z
- Finished UTC: 2026-09-22T00:36:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1490993 |
| label | Trichoderma lacuwombatense |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5543 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/trichoderma_lacuwombatense.yaml`. It carries two NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*trichoderma_lacuwombatense.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/trichoderma_lacuwombatense.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/trichoderma_lacuwombatense.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 381679 has `NCBITaxon:1490993`, label `Trichoderma lacuwombatense`, rank `SPECIES`, direct parent `NCBITaxon:5543`, genetic code `1`, two exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 60281 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Trichoderma` under family `Hypocreaceae`.

`data/raw/ncbi_merged_ids.tsv` maps three old IDs to this taxon: `NCBITaxon:234718`, `NCBITaxon:317023`, and `NCBITaxon:332946`. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this taxon with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 381679 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60281 | Supported exactly: `attested rule: Trichoderma lacuwombatense, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 11573 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1490993`. |
| Empty native GOLD organism evidence | Exact native GOLD organism scan | Supported; no native GOLD organism row in the local JSONL snapshot has `ORGANISM NCBI TAX ID` `1490993`. |
| Empty native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; with no matching local organism IDs, no native GOLD project row joins to this taxon. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 11 rows on lines 35941-35951. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1490993`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1490993`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1490993`. |

The NCBI type-material inventory contributes seven `culture from holotype` rows for CBS 122668 and GJS 99-198, two `holotype` rows for PDD 77489, and two `isotype` rows for BPI 746621 under the source taxon name `Hypocrea lacuwombatensis`. The local native GOLD JSONL snapshot has no exact organism, project, or analysis rows for this taxon even though the aggregate GOLD transform contributes a taxon-level assertion count of one.

The native StrainInfo snapshot has seven exact direct rows and seven exact deposit rows under `NCBITaxon:1490993`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Trichoderma` parent, two exact synonyms, three related synonyms, and 11 type-material rows.
- NCBI supplies three raw merged-ID rows, but does not supply a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies no exact organisms, projects, or analyses for this taxon.
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
- NCBI ranks `Trichoderma lacuwombatense` as `SPECIES`, and the generated record follows the source rank exactly.
