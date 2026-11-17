# YAML Record Review: Bradymyces alpinus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/bradymyces_alpinus.yaml
- Started UTC: 2026-09-22T03:06:52Z
- Finished UTC: 2026-09-22T03:06:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1562577 |
| label | Bradymyces alpinus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1562575 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/bradymyces_alpinus.yaml`. It carries four NCBI related synonyms, no exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no StrainInfo rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*bradymyces_alpinus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/bradymyces_alpinus.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/bradymyces_alpinus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 401720 has `NCBITaxon:1562577`, label `Bradymyces alpinus`, rank `SPECIES`, direct parent `NCBITaxon:1562575`, genetic code `1`, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 60468 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Bradymyces` under family `Trichomeriaceae`.

The side merged-ID inventory maps `NCBITaxon:1431292`, `NCBITaxon:1492068`, and `NCBITaxon:701993` into this taxon, but no committed retained retired-row evidence points at it, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 401720 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60468 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 12520 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1562577`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0583374`, for strain CCFEE 5478. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one joined project, `Gp0587337`, for strain CCFEE 5478. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis joins to this taxon by exact organism ID or project ID. |
| NCBI merged-ID side inventory | Exact `data/raw/ncbi_merged_ids.tsv` scan | Supported; old IDs `NCBITaxon:1431292`, `NCBITaxon:1492068`, and `NCBITaxon:701993` merge into `NCBITaxon:1562577`, but they are not retained retired rows and therefore do not generate `replaces`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six culture-from-holotype spellings for CBS 138368, CCF 4803, and CCFEE 5493 plus two holotype spellings for PRM 923905. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1562577`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `1562577`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1562577`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1562577`. |

The local native GOLD snapshot has one exact CCFEE 5478 organism and one joined project, but no joined analysis.

The NCBI type-material inventory contributes eight rows for CBS 138368, CCF 4803, CCFEE 5493, and PRM 923905.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Bradymyces` parent, four related synonyms, and eight type-material rows.
- NCBI supplies three side-inventory old IDs in `data/raw/ncbi_merged_ids.tsv`, but no retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one joined project, and no joined analyses.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:1562577\t' data/raw/ncbi_type_material.tsv` scan to recover all eight rows.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Bradymyces alpinus` as `SPECIES`, and the generated record follows the source rank exactly.
