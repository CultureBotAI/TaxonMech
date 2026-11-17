# YAML Record Review: Chaetothyriales sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chaetothyriales_sp.yaml
- Started UTC: 2026-09-22T08:41:24Z
- Finished UTC: 2026-09-22T08:41:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1715222 |
| label | Chaetothyriales sp. |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:316340 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal NCBI species under `unclassified Chaetothyriales` at `data/taxa/eukaryota/chaetothyriales_sp.yaml`. It carries no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chaetothyriales_sp.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chaetothyriales_sp.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chaetothyriales_sp.yaml` exited successfully and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 447639 has `NCBITaxon:1715222`, label `Chaetothyriales sp.`, rank `SPECIES`, direct parent `NCBITaxon:316340`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 61153 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `unclassified Chaetothyriales` under order `Chaetothyriales`.

The merged-ID scan found no old IDs pointing into this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, and genetic code | `data/raw/ncbitaxon_taxa.tsv` line 447639 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61153 | Supported exactly: `attested rule: Chaetothyriales sp., 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 14877 | Supported exactly with four aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1715222`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has exact organism rows for `Go0584567`, `Go0584568`, and `Go0584570`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0589705`, `Gp0589706`, and `Gp0589708` join to the three exact GOLD organism IDs. |
| Empty native GOLD analysis surface | Exact native GOLD analysis scan by project IDs | Supported; no native GOLD analysis rows join to exact projects `Gp0589705`, `Gp0589706`, or `Gp0589708`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1715222`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1715222`. |
| Empty type-material and auxiliary source surfaces | Exact scans of `data/raw/ncbi_type_material.tsv` plus the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no type-material or auxiliary source row mentions `NCBITaxon:1715222`. |
| Omitted `replaces` | Exact scan of merged NCBI IDs | Supported; no old ID maps into this current taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, and the direct `unclassified Chaetothyriales` parent.
- The NCBI merged-ID side inventory has no old ID for this taxon, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of four.
- The local native GOLD snapshot supplies three exact organisms, three joined projects, and no joined analysis rows for this taxon.
- BacDive, StrainInfo, type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks this exact `Chaetothyriales sp.` taxon as `SPECIES`, and the generated record follows the source rank exactly.
- The KG-Microbe aggregate GOLD row is the owning evidence for the generated `assertion_count`; this repo's supplemental native GOLD snapshot currently has three exact organism rows for `NCBITaxon:1715222`.
