# YAML Record Review: Aspergillus niger CBS 513.88

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_niger_cbs_513_88.yaml
- Started UTC: 2026-09-21T19:22:54Z
- Finished UTC: 2026-09-21T19:24:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:425011 |
| label | Aspergillus niger CBS 513.88 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5061 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic strain record at `data/taxa/eukaryota/aspergillus_niger_cbs_513_88.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_niger_cbs_513_88.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_niger_cbs_513_88.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_niger_cbs_513_88.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 93816 has `NCBITaxon:425011`, label `Aspergillus niger CBS 513.88`, rank `STRAIN`, direct parent `NCBITaxon:5061`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 55615 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate species parent `Aspergillus niger`.

`data/raw/ncbi_merged_ids.tsv` has no rows redirecting old IDs into `NCBITaxon:425011`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 93816 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55615 | Supported exactly: `attested rule: Aspergillus niger CBS 513.88, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35166 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:425011`. |
| NCBI type-material inventory | Exact `data/raw/ncbi_type_material.tsv` scan | Supported; no NCBI type-material rows are filed under `NCBITaxon:425011`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism row, one linked sequencing project, and one genome analysis linked through `AP PROJECT GOLD IDS`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `425011` or the reviewed native GOLD designation. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:425011`. |

The native GOLD snapshot has the exact organism `Aspergillus niger CBS 513.88` on line 198, linked sequencing project `Gp0000211` on line 203, and genome analysis `Ga0027582` on line 18052. The analysis leaves `AP ORGANISM GOLD ID` blank but names project `Gp0000211` in `AP PROJECT GOLD IDS`, and the project exact scan accounts for that link.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and no synonyms or type-material designations for this taxon.
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
