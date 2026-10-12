# YAML Record Review: Aspergillus botucatensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_botucatensis.yaml
- Started UTC: 2026-09-21T16:16:24Z
- Finished UTC: 2026-09-21T16:17:05Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1907480 |
| label | Aspergillus botucatensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_botucatensis.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_botucatensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_botucatensis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_botucatensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 493030 has `NCBITaxon:1907480`, label `Aspergillus botucatensis`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, related synonym `Aspergillus botucatensis Y. Horie, Miyaji & Nishim., 1995`, and source `gold`. `curation/seed_scope.tsv` line 61531 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly. The absence of a subgenus entry is source-faithful because the NCBI row parents this species directly to `Aspergillus`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 493030 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61531 | Supported exactly: `attested rule: Aspergillus botucatensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 17258 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1907480`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `1907480` and `NCBITaxon:1907480` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` for strain and deposit taxon IDs `1907480` and `NCBITaxon:1907480` | Supported; no direct or deposit-only StrainInfo rows were found. |

No rows for `NCBITaxon:1907480` were found in `data/raw/ncbi_type_material.tsv`, so there were no NCBI type-material culture tokens to test against BacDive or StrainInfo.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and one related synonym.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no organism, sequencing-project, or analysis-project row for taxon ID `1907480`; this is not a YAML defect because the generated taxon-level GOLD count is sourced from `data/raw/gold_organisms.tsv`.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, NCBI type-material, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive, StrainInfo, native GOLD, and type-material checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The absence of `nomenclature` is expected for this eukaryotic record because TaxonMech generates nomenclature from LPSN only.
