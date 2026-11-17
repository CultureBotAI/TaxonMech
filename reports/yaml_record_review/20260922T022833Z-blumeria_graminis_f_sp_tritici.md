# YAML Record Review: Blumeria graminis f. sp. tritici

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/blumeria_graminis_f_sp_tritici.yaml
- Started UTC: 2026-09-22T02:28:33Z
- Finished UTC: 2026-09-22T02:28:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:62690 |
| label | Blumeria graminis f. sp. tritici |
| rank | FORMA_SPECIALIS |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:34373 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal forma specialis at `data/taxa/eukaryota/blumeria_graminis_f_sp_tritici.yaml`. It carries one NCBI exact synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*blumeria_graminis_f_sp_tritici.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/blumeria_graminis_f_sp_tritici.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/blumeria_graminis_f_sp_tritici.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 7919 has `NCBITaxon:62690`, label `Blumeria graminis f. sp. tritici`, rank `FORMA_SPECIALIS`, direct parent `NCBITaxon:34373`, genetic code `1`, one exact synonym, and source `gold`. `curation/seed_scope.tsv` line 53047 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Blumeria graminis` under genus `Blumeria`.

The side merged-ID inventory maps `NCBITaxon:67577` into this taxon, but no committed retained retired-row evidence points at it, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 7919 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53047 | Supported exactly: `attested rule: Blumeria graminis f. sp. tritici, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 39990 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:62690`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0588665`, for strain ERS2646739. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one joined project, `Gp0602611`, for strain ERS2646739. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis, `Blumeria graminis f. sp. tritici ERS2646739`, joined through `Gp0602611`. |
| NCBI merged-ID side inventory | Exact `data/raw/ncbi_merged_ids.tsv` scan | Supported; old ID `NCBITaxon:67577` merges into `NCBITaxon:62690`, but it is not a retained retired row and therefore does not generate `replaces`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row mentions `NCBITaxon:62690`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `62690`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `62690`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:62690`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:62690`. |

The local native GOLD snapshot has one exact ERS2646739 organism, one joined project, and one analysis joined through the project ID.

The NCBI type-material inventory contributes no rows for this taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Blumeria graminis` parent, and one exact synonym.
- NCBI supplies one side-inventory old ID in `data/raw/ncbi_merged_ids.tsv`, but no retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one joined project, and one project-joined analysis.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- Native GOLD analysis rows can join by project ID as well as organism ID; the ERS2646739 analysis is recovered through `AP PROJECT GOLD IDS`, so it does not require a direct `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Blumeria graminis f. sp. tritici` as `FORMA_SPECIALIS`, and the generated record follows the source rank exactly.
