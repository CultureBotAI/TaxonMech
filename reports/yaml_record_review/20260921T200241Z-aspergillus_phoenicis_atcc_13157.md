# YAML Record Review: Aspergillus phoenicis ATCC 13157

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_phoenicis_atcc_13157.yaml
- Started UTC: 2026-09-21T20:01:25Z
- Finished UTC: 2026-09-21T20:02:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1353007 |
| label | Aspergillus phoenicis ATCC 13157 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5063 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic strain at `data/taxa/eukaryota/aspergillus_phoenicis_atcc_13157.yaml`. It carries no NCBI synonyms, no NCBI type-material rows, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_phoenicis_atcc_13157.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_phoenicis_atcc_13157.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_phoenicis_atcc_13157.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 326812 has `NCBITaxon:1353007`, label `Aspergillus phoenicis ATCC 13157`, rank `STRAIN`, direct parent `NCBITaxon:5063`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 59623 keeps this strain in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus phoenicis`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:1353007`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this strain; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 326812 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 59623 | Supported exactly: `attested rule: Aspergillus phoenicis ATCC 13157, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 8551 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1353007`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows are filed under `NCBITaxon:1353007`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; the current local native GOLD projection has no exact organism, project, or analysis rows under NCBI taxon `1353007`. |
| Empty BacDive strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1353007`. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:1353007`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1353007`. |

The aggregate GOLD transform contains one organism assertion for `NCBITaxon:1353007`, while the current native GOLD projection has zero exact organism rows for numeric taxon ID `1353007`. The YAML correctly follows `data/raw/gold_organisms.tsv`, which is the aggregate attestation source used during seeding.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and the lack of exact or related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The current local native GOLD snapshot has no exact organism/project/analysis chain for this taxon.
- BacDive, StrainInfo, LPSN, GTDB, MediaDive, Madin et al., and BactoTraits do not supply exact records for this taxon.
- Causal-graph and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The GOLD aggregate in `data/raw/gold_organisms.tsv` can differ from the count of exact rows in the native GOLD projection; the YAML assertion count correctly follows the aggregate raw inventory.
