# YAML Record Review: Aspergillus awamori var. piceus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_awamori_var_piceus.yaml
- Started UTC: 2026-09-21T16:09:52Z
- Finished UTC: 2026-09-21T16:10:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:309746 |
| label | Aspergillus awamori var. piceus |
| rank | VARIETAS |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:105351 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to the generated variety record at `data/taxa/eukaryota/aspergillus_awamori_var_piceus.yaml`, the child of the species record for `Aspergillus awamori`. It has no seeded synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_awamori_var_piceus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_awamori_var_piceus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_awamori_var_piceus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 63347 has `NCBITaxon:309746`, label `Aspergillus awamori var. piceus`, rank `VARIETAS`, parent `NCBITaxon:105351`, genetic code `1`, no synonym columns, and source `gold`. `curation/seed_scope.tsv` line 55122 keeps this variety in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly and places the variety under `Aspergillus awamori`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and empty synonyms | `data/raw/ncbitaxon_taxa.tsv` line 63347 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55122 | Supported exactly: `attested rule: Aspergillus awamori var. piceus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 31278 and native `data/gold/organisms.jsonl.gz` row 78918 | Supported exactly with one GOLD organism, `Go0138963`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `309746` and `NCBITaxon:309746` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; one deposit-only StrainInfo row involves this NCBI taxon and is excluded with `no_eligible_own_deposit_match`. |

No rows for `NCBITaxon:309746` were found in `data/raw/ncbi_type_material.tsv`, so there were no direct NCBI type-material culture tokens to test. The native GOLD culture token `JCM 22320` had no BacDive hit and one excluded StrainInfo hit, `straininfo.strain:219197`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, rank, parentage under `Aspergillus awamori`, and genetic code.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for `Aspergillus awamori var. piceus JCM 22320`.
- Native GOLD has one sequencing project and one analysis with `GCA_001599415.1`, but there is no BacDive strain join, so the GOLD chain does not create a TaxonMech strain genome link.
- BacDive has no exact record for this variety.
- StrainInfo evidence involving this variety or its GOLD culture token is excluded before seeding.
- LPSN, GTDB, NCBI type-material, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive and StrainInfo checks used exact scans of the committed gzip JSONL snapshots by NCBI taxon ID and quoted GOLD culture token.
- The native GOLD analysis row was inspected through `AP PROJECT GOLD IDS`; it does not emit because GOLD links require a whole culture token that joins to an existing BacDive-derived strain.
