# YAML Record Review: Aspergillus awamori

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_awamori.yaml
- Started UTC: 2026-09-21T16:08:40Z
- Finished UTC: 2026-09-21T16:09:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:105351 |
| label | Aspergillus awamori |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to the generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_awamori.yaml`, not the adjacent child record for `Aspergillus awamori var. piceus`. It has NCBI synonyms for `Aspergillus niger var. awamori`, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_awamori.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_awamori.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_awamori.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 18887 has `NCBITaxon:105351`, label `Aspergillus awamori`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, the exact synonym and three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53694 keeps this species in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly. The NCBI inventory has one child under this species, `NCBITaxon:309746` / `Aspergillus awamori var. piceus`, but the reviewed YAML correctly denotes only the parent species.

`data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:1608276`, `NCBITaxon:5055`, and `NCBITaxon:52868` to `NCBITaxon:105351`. A structured exact scan of `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and `curation/seed_scope.tsv` found no retained retired taxon, scoped row, or generated path for those three old IDs, so the raw redirect rows alone do not require generated `replaces` entries.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 18887 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53694 | Supported exactly: `attested rule: Aspergillus awamori, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 997 and native `data/gold/organisms.jsonl.gz` rows 2145 and 462027 | Supported exactly with two direct GOLD organism rows for `NCBITaxon:105351`. |
| Empty BacDive strain surface | Exact subtree scan of `data/bacdive/records.jsonl.gz` for taxon IDs `105351`, `309746`, `NCBITaxon:105351`, and `NCBITaxon:309746` | Supported; no exact BacDive records were found for the species or its child variety. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` for the species and child variety | Supported; 177 direct rows and 9 deposit-only rows involving these NCBI taxon IDs are all excluded with no unexcluded IDs. |

No rows for `NCBITaxon:105351` were found in `data/raw/ncbi_type_material.tsv`, so there were no direct NCBI type-material culture tokens to test against BacDive or StrainInfo.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one exact synonym, and three related synonyms.
- The aggregate GOLD transform and native GOLD snapshot both support two organism rows filed directly under `NCBITaxon:105351`.
- Native GOLD has two sequencing projects and one analysis with `GCA_003850985.1`, but the joined organism has no culture collection ID and there is no BacDive strain join, so this GOLD chain does not create a TaxonMech strain genome link.
- BacDive has no exact records for the species or its child variety.
- StrainInfo rows for this species subtree are intentionally excluded before seeding.
- LPSN, GTDB, NCBI type-material, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The `source_attestations` GOLD note is correct: GOLD counts only the two direct organism rows for `NCBITaxon:105351`; descendant taxon `NCBITaxon:309746` is not gathered into the GOLD count.
- The empty BacDive and StrainInfo checks included the direct child variety to match the species-level BacDive subtree rule.
