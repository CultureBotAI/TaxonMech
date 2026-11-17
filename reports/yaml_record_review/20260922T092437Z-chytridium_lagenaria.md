# YAML Record Review: Chytridium lagenaria

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chytridium_lagenaria.yaml
- Started UTC: 2026-09-22T09:24:37Z
- Finished UTC: 2026-09-22T09:24:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:64509 |
| label | Chytridium lagenaria |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:4813 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic chytrid species at `data/taxa/eukaryota/chytridium_lagenaria.yaml`. It carries two NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chytridium_lagenaria.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chytridium_lagenaria.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chytridium_lagenaria.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 8175 has `NCBITaxon:64509`, label `Chytridium lagenaria`, rank `SPECIES`, direct parent `NCBITaxon:4813`, genetic code `1`, two exact synonyms, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 53086 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chytridium` under family `Chytridiaceae`.

The side-inventory merged-ID scan found `NCBITaxon:109934` pointing into this taxon, but no retained retired row maps to this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 8175 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53086 | Supported exactly: `attested rule: Chytridium lagenaria, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40314 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:64509`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0136945` for `Chytridium lagenaria Arg66`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0141925` and `Gp0215043` join to `Go0136945`. |
| Empty native GOLD analysis surface | Exact native GOLD analysis scan by project IDs | Supported; no native GOLD analysis rows join to exact projects `Gp0141925` and `Gp0215043`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with three exact direct StrainInfo records and four exact deposit-taxonomy matches under taxon ID `64509`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `64509`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:64509`. |
| Empty type-material and auxiliary source surfaces | Exact scans of `data/raw/ncbi_type_material.tsv` plus the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no type-material or auxiliary source row mentions `NCBITaxon:64509`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; side-inventory old ID `NCBITaxon:109934` points into this taxon, but no retained retired row exists for the generator to carry into `replaces`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chytridium` parent, two exact synonyms, and one related synonym.
- The NCBI merged-ID side inventory has one old ID that is not present as a retained retired row, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, two joined projects, and no joined analysis rows for this taxon.
- Native StrainInfo has exact rows for this taxon, but there are no local BacDive-derived strain records or generated StrainInfo overlay rows under `NCBITaxon:64509`.
- BacDive, type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chytridium lagenaria` as `SPECIES`, and the generated record follows the source rank exactly.
