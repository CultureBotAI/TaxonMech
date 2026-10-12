# YAML Record Review: Cladorrhinum hyalocarpum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cladorrhinum_hyalocarpum.yaml
- Started UTC: 2026-09-22T10:09:43Z
- Finished UTC: 2026-09-22T10:09:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2587396 |
| label | Cladorrhinum hyalocarpum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:223374 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cladorrhinum_hyalocarpum.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladorrhinum_hyalocarpum.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cladorrhinum_hyalocarpum.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cladorrhinum_hyalocarpum.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already passed on the current checkout. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 534325 has `NCBITaxon:2587396`, label `Cladorrhinum hyalocarpum`, rank `SPECIES`, direct parent `NCBITaxon:223374`, genetic code `1`, exact synonym `Thielavia hyalocarpa`, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 62859 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cladorrhinum` under family `Podosporaceae`.

The side-inventory merged-ID scan found `NCBITaxon:113615` pointing into this taxon, but no retained retired row maps to this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 534325 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62859 | Supported exactly: `attested rule: Cladorrhinum hyalocarpum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 23675 | Supported exactly with two aggregate GOLD organism assertions for `NCBITaxon:2587396`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has two exact organism rows, `Go0651430` and `Go0651434`, for `Cladorrhinum hyalocarpum`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0688334`, `Gp0688338`, `Gp0699256`, and `Gp0699299` join to the two exact organism IDs. |
| Empty native GOLD analysis surface | Exact native GOLD analysis scan by joined project IDs | Supported; no native GOLD analysis rows join to exact projects `Gp0688334`, `Gp0688338`, `Gp0699256`, or `Gp0699299`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two `CBS 322.70` type-material spelling variants on lines 103488-103489, both under the synonym `Thielavia hyalocarpa`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with three exact direct StrainInfo records and three exact deposit-taxonomy matches under taxon ID `2587396`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `2587396`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2587396`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2587396`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; side-inventory old ID `NCBITaxon:113615` points into this taxon, but no retained retired row exists for the generator to carry into `replaces`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cladorrhinum` parent, one exact synonym, three related synonyms, and two type-material rows.
- The NCBI merged-ID side inventory has one old ID that is not present as a retained retired row, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms, four joined projects, and no joined analysis rows for this taxon.
- Native StrainInfo has exact rows for this taxon, but there are no local BacDive-derived strain records or generated StrainInfo overlay rows under `NCBITaxon:2587396`.
- BacDive, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- An `rg --no-ignore --hidden` check over `data/raw`, `data/straininfo`, and `curation/seed_scope.tsv` included ignored files while confirming there were no additional maintained rows for this taxon beyond the expected NCBI, GOLD aggregate, NCBI merged-ID, seed-scope, NCBI type-material, native GOLD, and native StrainInfo evidence.
- NCBI ranks `Cladorrhinum hyalocarpum` as `SPECIES`, and the generated record follows the source rank exactly.
