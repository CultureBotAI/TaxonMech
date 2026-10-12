# YAML Record Review: Aspergillus baeticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_baeticus.yaml
- Started UTC: 2026-09-21T16:10:55Z
- Finished UTC: 2026-09-21T16:11:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1194636 |
| label | Aspergillus baeticus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_baeticus.yaml`. It carries four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_baeticus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_baeticus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_baeticus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 268717 has `NCBITaxon:1194636`, label `Aspergillus baeticus`, rank `SPECIES`, parent `NCBITaxon:2720870`, genetic code `1`, the four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58265 keeps this identifier in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly and places this species under `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:1118481`, `NCBITaxon:1118482`, and `NCBITaxon:1120492` to `NCBITaxon:1194636`. A structured exact scan of `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and `curation/seed_scope.tsv` found no retained retired taxon, scoped row, or generated path for those old IDs, so the raw redirect rows alone do not require generated `replaces` entries.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 268717 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58265 | Supported exactly: `attested rule: Aspergillus baeticus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 4636 and native `data/gold/organisms.jsonl.gz` row 304938 | Supported exactly with one GOLD organism, `Go0446147`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `1194636` and `NCBITaxon:1194636` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; one direct NCBI-taxonomy StrainInfo row exists and is excluded with `no_eligible_own_deposit_match`. |

`data/raw/ncbi_type_material.tsv` has six NCBI type-material rows for `CCF 4226`, `CMFISB 2153`, `NRRL 62501`, and colon-separated variants. Exact quoted-token scans for those values found no matching BacDive or StrainInfo snapshot records.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and four related synonyms.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for `Aspergillus baeticus IBT 34334`.
- Native GOLD has two transcriptome projects for `Go0446147`, but no analysis rows; without a BacDive strain join, these projects do not create TaxonMech strain related records.
- BacDive has no exact records for the taxon or the checked type-material tokens.
- The one StrainInfo row for this NCBI taxon is intentionally excluded before seeding.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive and StrainInfo checks used exact scans of the committed gzip JSONL snapshots by NCBI taxon ID and quoted type-material tokens.
- The old-ID check used structured exact matching over the complete seeding and path TSVs to avoid false substring hits.
