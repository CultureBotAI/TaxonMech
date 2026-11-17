# YAML Record Review: Aspergillus bisporus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_bisporus.yaml
- Started UTC: 2026-09-21T16:14:34Z
- Finished UTC: 2026-09-21T16:15:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41753 |
| label | Aspergillus bisporus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_bisporus.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_bisporus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_bisporus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_bisporus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4881 has `NCBITaxon:41753`, label `Aspergillus bisporus`, rank `SPECIES`, parent `NCBITaxon:2720870`, genetic code `1`, related synonym `Aspergillus bisporus Kwon-Chung & Fennell, 1971`, and source `gold`. `curation/seed_scope.tsv` line 52493 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly and places this species under `Aspergillus subgen. Nidulantes`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 4881 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52493 | Supported exactly: `attested rule: Aspergillus bisporus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34944 and native `data/gold/organisms.jsonl.gz` row 59793 | Supported exactly with one GOLD organism, `Go0108091`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `41753` and `NCBITaxon:41753` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; three direct NCBI-taxonomy StrainInfo rows exist, and every one is excluded with `no_eligible_own_deposit_match`. |

`data/raw/ncbi_type_material.tsv` has six NCBI type-material rows for `ATCC 22527`, `CBS 707.71`, `NRRL 3693`, and colon-separated variants. Exact quoted-token scans for those values found no BacDive hits and found only excluded `straininfo.strain:264469`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and one related synonym.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for `Aspergillus bisporus CBS 707.71`.
- Native GOLD has two sequencing projects for `Go0108091`, but no analysis rows; without a BacDive strain join, these projects do not create TaxonMech strain related records or genome links.
- BacDive has no exact records for the taxon or the checked type-material tokens.
- StrainInfo rows for this NCBI taxon are intentionally excluded before seeding.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive and StrainInfo checks used exact scans of the committed gzip JSONL snapshots by NCBI taxon ID and quoted type-material tokens.
- The absence of `nomenclature` is expected for this eukaryotic record because TaxonMech generates nomenclature from LPSN only.
