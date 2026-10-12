# YAML Record Review: Aspergillus nomiae NRRL 13137

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_nomiae_nrrl_13137.yaml
- Started UTC: 2026-09-21T19:29:21Z
- Finished UTC: 2026-09-21T19:31:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1509407 |
| label | Aspergillus nomiae NRRL 13137 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:41061 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic strain record at `data/taxa/eukaryota/aspergillus_nomiae_nrrl_13137.yaml`. It carries one NCBI exact synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_nomiae_nrrl_13137.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_nomiae_nrrl_13137.yaml` exited successfully with no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_nomiae_nrrl_13137.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 388032 has `NCBITaxon:1509407`, label `Aspergillus nomiae NRRL 13137`, rank `STRAIN`, direct parent `NCBITaxon:41061`, genetic code `1`, one exact synonym, and source `gold`. `curation/seed_scope.tsv` line 60377 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate species parent `Aspergillus nomiae`.

`data/raw/ncbi_merged_ids.tsv` has no rows redirecting old IDs into `NCBITaxon:1509407`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 388032 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60377 | Supported exactly: `attested rule: Aspergillus nomiae NRRL 13137, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 11894 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1509407`. |
| NCBI type-material inventory | Exact `data/raw/ncbi_type_material.tsv` scan | Supported; no NCBI type-material rows are filed under `NCBITaxon:1509407`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism row, one linked sequencing project, and one genome analysis linked through `AP PROJECT GOLD IDS`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1509407` or the reviewed native GOLD designation. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:1509407`. |

The native GOLD snapshot has the exact organism `Aspergillus nomiae NRRL13137` on line 65655, linked sequencing project `Gp0120416` on line 70065, and genome analysis `Ga0131464` on line 77684. The analysis leaves `AP ORGANISM GOLD ID` blank but names project `Gp0120416` in `AP PROJECT GOLD IDS`, and the project exact scan accounts for that link.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one exact synonym, and no type-material designations for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row, one linked sequencing project, and one genome analysis for this taxon, with no matched BacDive-derived local strain identifier to join through.
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
