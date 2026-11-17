# YAML Record Review: Aspergillus papuensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_papuensis.yaml
- Started UTC: 2026-09-21T19:48:10Z
- Finished UTC: 2026-09-21T19:49:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1825619 |
| label | Aspergillus papuensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_papuensis.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_papuensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_papuensis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_papuensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 476220 has `NCBITaxon:1825619`, label `Aspergillus papuensis`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61330 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` line 65928 redirects old ID `NCBITaxon:320691` into `NCBITaxon:1825619`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 476220 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61330 | Supported exactly: `attested rule: Aspergillus papuensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 16183 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1825619`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 62600-62605 | Supported exactly with `CBS 841.96` and `IBT 27801` culture-from-holotype variants plus `CBS H-6277` holotype variants for `Aspergillus papuensis`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; the current local native GOLD projection has no exact organism, project, or analysis rows under NCBI taxon `1825619`. |
| Empty BacDive strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1825619`. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:1825619`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1825619`. |

The aggregate GOLD transform contains one organism assertion for `NCBITaxon:1825619`, while the current native GOLD projection has zero exact organism rows for numeric taxon ID `1825619`. The YAML correctly follows `data/raw/gold_organisms.tsv`, which is the aggregate attestation source used during seeding.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, the merged old ID, and the type-material designations reviewed above.
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
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
