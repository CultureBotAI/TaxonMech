# YAML Record Review: Aspergillus oryzae RIB40

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_oryzae_rib40.yaml
- Started UTC: 2026-09-21T19:43:15Z
- Finished UTC: 2026-09-21T19:45:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:510516 |
| label | Aspergillus oryzae RIB40 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5062 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic strain at `data/taxa/eukaryota/aspergillus_oryzae_rib40.yaml`. It carries no NCBI synonyms, no NCBI type-material rows, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_oryzae_rib40.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_oryzae_rib40.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_oryzae_rib40.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 115919 has `NCBITaxon:510516`, label `Aspergillus oryzae RIB40`, rank `STRAIN`, direct parent `NCBITaxon:5062`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 55865 keeps this strain in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus oryzae`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:510516`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this strain; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 115919 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55865 | Supported exactly: `attested rule: Aspergillus oryzae RIB40, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37493 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:510516`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows are filed under `NCBITaxon:510516`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one exact organism row, one linked sequencing project, and one linked analysis under NCBI taxon `510516`. |
| Empty BacDive strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `510516`. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:510516`. |

The native GOLD snapshot has one exact organism row, `Go0415749` for `Aspergillus oryzae RIB 40` on line 301806. It joins to project `Gp0308842` on line 208145 and to the `Aspergillus oryzae RIB 40` analysis on line 176581 through `AP PROJECT GOLD IDS`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and the lack of exact or related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism/project/analysis chain for this taxon, with no matched BacDive-derived local strain identifier to join through.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- GOLD links its only native analysis to this organism through the project ID; the local native scan therefore checked `AP PROJECT GOLD IDS` as well as `AP ORGANISM GOLD ID`.
