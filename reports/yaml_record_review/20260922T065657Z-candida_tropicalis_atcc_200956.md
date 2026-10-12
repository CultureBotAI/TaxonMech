# YAML Record Review: Candida tropicalis ATCC 200956

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candida_tropicalis_atcc_200956.yaml
- Started UTC: 2026-09-22T06:56:57Z
- Finished UTC: 2026-09-22T06:56:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1312901 |
| label | Candida tropicalis ATCC 200956 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5482 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal strain at `data/taxa/eukaryota/candida_tropicalis_atcc_200956.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*candida_tropicalis_atcc_200956.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candida_tropicalis_atcc_200956.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candida_tropicalis_atcc_200956.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 311516 has `NCBITaxon:1312901`, label `Candida tropicalis ATCC 200956`, rank `STRAIN`, direct parent `NCBITaxon:5482`, genetic code `12`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 59361 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent species `Candida tropicalis`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 311516 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 59361 | Supported exactly: `attested rule: Candida tropicalis ATCC 200956, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 7661 | Supported exactly with 13 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1312901`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with 14 native organisms, from `Go0041072` plus `Go0624962` through `Go0624974`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with two projects, `Gp0041072` and `Gp0831262`, for the exact organism rows. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention `NCBITaxon:1312901`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1312901`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1312901`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1312901`. |

The local native GOLD snapshot has 14 exact organisms and two joined projects for ATCC 200956, NRRL Y-607, NRRL Y-12968, NRRL Y-12699, NBRC 1400, NBRC 1070, JCM 1541, IFO 1400, IFO 1070, DSM 11953, CCRC 20520, ATCC 750, ATCC 7349, and ATCC 4563, with no joined analysis rows. The exact NCBI type-material, BacDive, StrainInfo, raw strain, and auxiliary-source scans are all empty for this strain taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, and the direct `Candida tropicalis` parent.
- NCBI does not supply merged-ID or type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of 13.
- The local native GOLD snapshot supplies 14 exact organisms with two projects and no joined analyses.
- BacDive and exact StrainInfo scans do not supply local generated strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Candida tropicalis ATCC 200956` as `STRAIN`, and the generated record follows the source rank exactly.
