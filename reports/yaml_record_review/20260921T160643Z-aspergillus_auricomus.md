# YAML Record Review: Aspergillus auricomus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_auricomus.yaml
- Started UTC: 2026-09-21T16:05:58Z
- Finished UTC: 2026-09-21T16:06:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:138274 |
| label | Aspergillus auricomus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_auricomus.yaml`. It carries NCBI synonyms for `Sterigmatocystis auricoma`, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_auricomus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_auricomus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_auricomus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 27761 has `NCBITaxon:138274`, label `Aspergillus auricomus`, rank `SPECIES`, parent `NCBITaxon:2720871`, genetic code `1`, exact synonym `Sterigmatocystis auricoma`, the two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53979 keeps this taxon in scope through the attested-source rule, consistent with the generated `SEEDED` status.

The YAML lineage matches the NCBI inventory parent chain exactly and places this species under `Aspergillus subgen. Circumdati`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 27761 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53979 | Supported exactly: `attested rule: Aspergillus auricomus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 8979 and native `data/gold/organisms.jsonl.gz` rows 59847 and 59858 | Supported exactly with two native GOLD organism rows carrying `ORGANISM NCBI TAX ID` `138274`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `138274` and `NCBITaxon:138274` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; fourteen direct rows and one deposit-only row involving this NCBI taxon are all excluded with `no_eligible_own_deposit_match`. |

`data/raw/ncbi_type_material.tsv` has eighteen NCBI type-material rows for neotype and type-material designations including `CBS 467.65`, `NRRL 391`, `ATCC 16890`, `IBT 14581`, `IMI 172277`, `LCP 89.2596`, `LSHBA 41`, `WB 391`, and colon-separated variants. Exact quoted-token scans for those values found no BacDive hits and found only excluded `straininfo.strain:63526`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one exact synonym, and two related synonyms.
- The aggregate GOLD transform and native GOLD snapshot both support two organism rows for NCBI taxon `138274`.
- One native GOLD row is named `Aspergillus subauricomus CBS 638.78`; its count in the YAML follows GOLD's supplied NCBI taxon ID rather than normalizing that organism name.
- Native GOLD has four sequencing projects across the two organisms but no analysis rows; without a BacDive strain join, these projects do not create TaxonMech strain related records or genome links.
- BacDive has no exact records for the taxon or the checked type-material tokens.
- StrainInfo rows for this taxon are intentionally excluded before seeding.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive and StrainInfo checks used exact scans of the committed gzip JSONL snapshots by NCBI taxon ID and quoted type-material tokens.
- The `Aspergillus subauricomus` GOLD organism name is visible only in native GOLD context; the generated taxon-level GOLD count remains an assertion count, not a curated synonym or taxonomic judgement.
