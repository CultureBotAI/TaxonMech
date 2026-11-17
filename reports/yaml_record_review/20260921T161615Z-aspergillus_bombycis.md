# YAML Record Review: Aspergillus bombycis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_bombycis.yaml
- Started UTC: 2026-09-21T16:15:35Z
- Finished UTC: 2026-09-21T16:16:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:109264 |
| label | Aspergillus bombycis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_bombycis.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_bombycis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_bombycis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_bombycis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 19657 has `NCBITaxon:109264`, label `Aspergillus bombycis`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, related synonym `Aspergillus bombycis S.W. Peterson, Yoko Ito, B.W. Horn & T. Goto, 2001`, and source `gold`. `curation/seed_scope.tsv` line 53736 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly. The absence of a subgenus entry is source-faithful because the NCBI row parents this species directly to `Aspergillus`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 19657 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53736 | Supported exactly: `attested rule: Aspergillus bombycis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 1690 and native `data/gold/organisms.jsonl.gz` row 276905 | Supported exactly with one GOLD organism, `Go0373239`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `109264` and `NCBITaxon:109264` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; two direct NCBI-taxonomy StrainInfo rows exist, and both are excluded with `no_eligible_own_deposit_match`. |

`data/raw/ncbi_type_material.tsv` has eight NCBI type-material rows for `CBS 117187`, `NRRL 26010`, `BPI 745225`, and alternate punctuation variants. Exact quoted-token scans for those values found no BacDive hits and found only excluded `straininfo.strain:148767`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and one related synonym.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for `Aspergillus bombycis NRRL 26010`.
- Native GOLD has one sequencing project and one analysis with `GCA_001792695.1`; the culture token has no BacDive strain join, so this GOLD chain does not create a TaxonMech strain genome link.
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
- The native GOLD analysis row was inspected through `AP PROJECT GOLD IDS`; it does not emit because GOLD links require a whole culture token that joins to an existing BacDive-derived strain.
