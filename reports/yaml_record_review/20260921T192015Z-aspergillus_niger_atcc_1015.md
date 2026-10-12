# YAML Record Review: Aspergillus niger ATCC 1015

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_niger_atcc_1015.yaml
- Started UTC: 2026-09-21T19:18:48Z
- Finished UTC: 2026-09-21T19:20:15Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:380704 |
| label | Aspergillus niger ATCC 1015 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5061 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic strain record at `data/taxa/eukaryota/aspergillus_niger_atcc_1015.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_niger_atcc_1015.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_niger_atcc_1015.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_niger_atcc_1015.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 80058 has `NCBITaxon:380704`, label `Aspergillus niger ATCC 1015`, rank `STRAIN`, direct parent `NCBITaxon:5061`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 55441 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate species parent `Aspergillus niger`.

`data/raw/ncbi_merged_ids.tsv` has no rows redirecting old IDs into `NCBITaxon:380704`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 80058 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55441 | Supported exactly: `attested rule: Aspergillus niger ATCC 1015, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 33892 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:380704`. |
| NCBI type-material inventory | Exact `data/raw/ncbi_type_material.tsv` scan | Supported; no NCBI type-material rows are filed under `NCBITaxon:380704`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism row, two linked sequencing projects, and two genome analyses linked through `AP PROJECT GOLD IDS`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `380704` or the reviewed native GOLD designation. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:380704`. |

The native GOLD snapshot has the exact organism `Aspergillus niger ATCC 1015` on line 15067, sequencing projects `Gp0017642` and `Gp0098640` on lines 14578 and 57456, and genome analyses `Ga0039285` and `Ga0228418` on lines 25023 and 138905. A quoted `ATCC 1015` token appears once in the StrainInfo snapshot, but no StrainInfo record is filed under NCBI taxon `380704`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and no synonyms or type-material designations for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot has one organism row, two linked sequencing projects, and two genome analyses for this taxon, with no matched BacDive-derived local strain identifier to join through.
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
- The aggregate GOLD count can exceed native exact organism rows because `data/raw/gold_organisms.tsv` is an aggregate KG-Microbe inventory while the native GOLD rows come from the committed local GOLD snapshot.
- The native GOLD analysis rows leave `AP ORGANISM GOLD ID` blank but name project `Gp0017642` in `AP PROJECT GOLD IDS`; the project exact scan accounts for these links.
