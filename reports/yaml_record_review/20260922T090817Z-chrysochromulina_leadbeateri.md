# YAML Record Review: Chrysochromulina leadbeateri

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chrysochromulina_leadbeateri.yaml
- Started UTC: 2026-09-22T09:08:17Z
- Finished UTC: 2026-09-22T09:08:17Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:412156 |
| label | Chrysochromulina leadbeateri |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:35140 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic haptophyte species at `data/taxa/eukaryota/chrysochromulina_leadbeateri.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chrysochromulina_leadbeateri.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chrysochromulina_leadbeateri.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chrysochromulina_leadbeateri.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 89712 has `NCBITaxon:412156`, label `Chrysochromulina leadbeateri`, rank `SPECIES`, direct parent `NCBITaxon:35140`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 55555 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chrysochromulina` under family `Chrysochromulinaceae`.

The merged-ID scan found no old IDs pointing into this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 89712 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55555 | Supported exactly: `attested rule: Chrysochromulina leadbeateri, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34762 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:412156`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0692372` for `Chrysochromulina leadbeateri UIO 393`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0803317` and `Gp0803318` join to `Go0692372`. |
| Empty native GOLD analysis surface | Exact native GOLD analysis scan by project IDs | Supported; no native GOLD analysis rows join to exact projects `Gp0803317` and `Gp0803318`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `412156`. |
| Empty native and generated StrainInfo surfaces | Exact scans of native StrainInfo plus `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no native direct row, native deposit-taxonomy hit, generated assembly, exclusion, or related-record row mentions `NCBITaxon:412156`. |
| Empty type-material and auxiliary source surfaces | Exact scans of `data/raw/ncbi_type_material.tsv` plus the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no type-material or auxiliary source row mentions `NCBITaxon:412156`. |
| Omitted `replaces` | Exact scan of merged NCBI IDs | Supported; no old ID maps into this current taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chrysochromulina` parent, and one related synonym.
- The NCBI merged-ID side inventory has no old ID for this taxon, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, two joined projects, and no joined analysis rows for this taxon.
- BacDive, StrainInfo, type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chrysochromulina leadbeateri` as `SPECIES`, and the generated record follows the source rank exactly.
