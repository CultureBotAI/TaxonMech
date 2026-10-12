# YAML Record Review: Aspergillus niger ATCC 13496

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_niger_atcc_13496.yaml
- Started UTC: 2026-09-21T19:20:16Z
- Finished UTC: 2026-09-21T19:21:25Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1353008 |
| label | Aspergillus niger ATCC 13496 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5061 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic strain record at `data/taxa/eukaryota/aspergillus_niger_atcc_13496.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_niger_atcc_13496.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_niger_atcc_13496.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_niger_atcc_13496.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 326813 has `NCBITaxon:1353008`, label `Aspergillus niger ATCC 13496`, rank `STRAIN`, direct parent `NCBITaxon:5061`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 59624 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate species parent `Aspergillus niger`.

`data/raw/ncbi_merged_ids.tsv` has no rows redirecting old IDs into `NCBITaxon:1353008`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 326813 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 59624 | Supported exactly: `attested rule: Aspergillus niger ATCC 13496, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 8552 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1353008`. |
| NCBI type-material inventory | Exact `data/raw/ncbi_type_material.tsv` scan | Supported; no NCBI type-material rows are filed under `NCBITaxon:1353008`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; no native GOLD organism, project, or genome-analysis rows are filed under this exact NCBI taxon in the local snapshot. |
| Empty BacDive strain surface | Exact taxon and exact raw-table scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1353008`. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:1353008`. |

The GOLD support for this generated record comes from the aggregate `data/raw/gold_organisms.tsv` row. The local native GOLD organism, project, and analysis snapshots do not contain an exact row with NCBI taxon `1353008`, so there are no native GOLD culture tokens to join to BacDive-derived local strain IDs for this exact strain-rank taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and no synonyms or type-material designations for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no organism, project, or genome-analysis rows for this exact taxon.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The aggregate GOLD count can have no native exact organism rows because `data/raw/gold_organisms.tsv` is an aggregate KG-Microbe inventory while the native GOLD rows come from the committed local GOLD snapshot.
