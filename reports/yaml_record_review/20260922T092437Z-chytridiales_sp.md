# YAML Record Review: Chytridiales sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chytridiales_sp.yaml
- Started UTC: 2026-09-22T09:24:37Z
- Finished UTC: 2026-09-22T09:24:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2011832 |
| label | Chytridiales sp. |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:109868 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic chytrid species-level NCBI taxon at `data/taxa/eukaryota/chytridiales_sp.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chytridiales_sp.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chytridiales_sp.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chytridiales_sp.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 510007 has `NCBITaxon:2011832`, label `Chytridiales sp.`, rank `SPECIES`, direct parent `NCBITaxon:109868`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 61849 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `unclassified Chytridiales` under order `Chytridiales`.

The merged-ID scan found no old IDs pointing into this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 510007 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61849 | Supported exactly: `attested rule: Chytridiales sp., 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 18573 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2011832`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0515126` for `Chytridiales sp. JEL0842`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0435892` joins to `Go0515126`. |
| Empty native GOLD analysis surface | Exact native GOLD analysis scan by project IDs | Supported; no native GOLD analysis rows join to exact project `Gp0435892`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `2011832`. |
| Empty native and generated StrainInfo surfaces | Exact scans of native StrainInfo plus `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no native direct row, native deposit-taxonomy hit, generated assembly, exclusion, or related-record row mentions `NCBITaxon:2011832`. |
| Empty type-material and auxiliary source surfaces | Exact scans of `data/raw/ncbi_type_material.tsv` plus the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no type-material or auxiliary source row mentions `NCBITaxon:2011832`. |
| Omitted `replaces` | Exact scan of merged NCBI IDs | Supported; no old ID maps into this current taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `unclassified Chytridiales` parent, and no synonyms.
- The NCBI merged-ID side inventory has no old ID for this taxon, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one joined project, and no joined analysis rows for this taxon.
- BacDive, StrainInfo, type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chytridiales sp.` as `SPECIES`, and the generated record follows the source rank exactly.
