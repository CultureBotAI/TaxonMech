# YAML Record Review: Beauveria bassiana

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/beauveria_bassiana.yaml
- Started UTC: 2026-09-22T00:09:03Z
- Finished UTC: 2026-09-22T00:10:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:176275 |
| label | Beauveria bassiana |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5581 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/beauveria_bassiana.yaml`. It carries six NCBI exact synonyms, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*beauveria_bassiana.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/beauveria_bassiana.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/beauveria_bassiana.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 35700 has `NCBITaxon:176275`, label `Beauveria bassiana`, rank `SPECIES`, direct parent `NCBITaxon:5581`, genetic code `1`, six exact synonyms, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54305 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Beauveria` under family `Cordycipitaceae`.

`data/raw/ncbi_merged_ids.tsv` maps five old IDs to this taxon: `NCBITaxon:1208601`, `NCBITaxon:139634`, `NCBITaxon:1671127`, `NCBITaxon:475271`, and `NCBITaxon:5582`. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this taxon with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 35700 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54305 | Supported exactly: `attested rule: Beauveria bassiana, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15346 | Supported exactly with 17 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:176275`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with 15 native organisms, from `Go0002496` through `Go0632003`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with 16 projects, including two projects for `Go0384330` strain ARSEF 8028. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with 12 analysis rows joining through exact local project IDs. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six rows on lines 57561-57566. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `176275`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:176275`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:176275`. |

The NCBI type-material inventory contributes two `culture from neotype` rows for ARSEF 1564 and four `type material` rows for ARSEF 7047 and BPI 880999 under the source taxon name `Botrytis bassiana`. The local native GOLD snapshot has 15 exact organisms, 16 exact projects, and 12 joined analysis rows.

The native StrainInfo snapshot has 272 exact direct rows and 339 exact deposit rows under `NCBITaxon:176275`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Beauveria` parent, six exact synonyms, four related synonyms, and six type-material rows.
- NCBI supplies five raw merged-ID rows, but does not supply a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of 17.
- The local native GOLD snapshot supplies 15 exact organisms with 16 projects and 12 joined analyses.
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
- NCBI ranks `Beauveria bassiana` as `SPECIES`, and the generated record follows the source rank exactly.
