# YAML Record Review: Aspergillus bertholletiae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_bertholletiae.yaml
- Started UTC: 2026-09-21T16:11:48Z
- Finished UTC: 2026-09-21T16:12:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1226010 |
| label | Aspergillus bertholletiae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_bertholletiae.yaml`. It carries two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_bertholletiae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_bertholletiae.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_bertholletiae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 279511 has `NCBITaxon:1226010`, label `Aspergillus bertholletiae`, rank `SPECIES`, parent `NCBITaxon:2720871`, genetic code `1`, the two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58496 keeps this identifier in scope through the attested-source rule, consistent with the generated `SEEDED` status.

The YAML lineage matches the NCBI inventory parent chain exactly and places this species under `Aspergillus subgen. Circumdati`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 279511 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58496 | Supported exactly: `attested rule: Aspergillus bertholletiae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 5392 and native `data/gold/organisms.jsonl.gz` row 59830 | Supported exactly with one GOLD organism, `Go0108169`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `1226010` and `NCBITaxon:1226010` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` for strain and deposit taxon IDs `1226010` and `NCBITaxon:1226010` | Supported; no direct or deposit-only StrainInfo rows were found. |

`data/raw/ncbi_type_material.tsv` has six NCBI type-material rows for `IBT 29228`, `ITAL 270/06`, `CCT 7615`, and colon-separated variants. Exact quoted-token scans for those values found no matching BacDive or StrainInfo snapshot records.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and two related synonyms.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for taxon `1226010`; the native row spells the organism name as `Aspergillus bertholletius IBT 29228` but carries the reviewed NCBI taxon ID.
- Native GOLD has three sequencing projects for `Go0108169`, but no analysis rows; without a BacDive strain join, these projects do not create TaxonMech strain related records or genome links.
- BacDive and StrainInfo do not supply exact taxon or type-material token matches.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive and StrainInfo checks used exact scans of the committed gzip JSONL snapshots by NCBI taxon ID and quoted type-material tokens.
- The native GOLD spelling drift is retained as source context; the generated taxon-level count is keyed by NCBI taxon ID.
