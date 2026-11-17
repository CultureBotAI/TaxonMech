# YAML Record Review: Aspergillus phoenicis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_phoenicis.yaml
- Started UTC: 2026-09-21T20:00:10Z
- Finished UTC: 2026-09-21T20:01:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5063 |
| label | Aspergillus phoenicis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_phoenicis.yaml`. It carries four NCBI exact synonyms, four NCBI related synonyms, no NCBI type-material rows, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_phoenicis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_phoenicis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_phoenicis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2212 has `NCBITaxon:5063`, label `Aspergillus phoenicis`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, four exact synonyms, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51922 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` lines 30575-30576 redirect old IDs `NCBITaxon:186679` and `NCBITaxon:186681` into `NCBITaxon:5063`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2212 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51922 | Supported exactly: `attested rule: Aspergillus phoenicis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37427 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5063`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows are filed under `NCBITaxon:5063`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with three exact organism rows, four linked sequencing projects, and one linked analysis under NCBI taxon `5063`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5063`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5063`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5063`. |

The native GOLD snapshot has three exact organism rows for NCBI taxon `5063`: `Go0036537` for `ATCC 13157`, `Go0036539` for `ATCC 15555`, and `Go0036540` for `ATCC 15556`. They join to four sequencing projects, and one `ATCC 13157` analysis is linked through `AP PROJECT GOLD IDS`.

Native StrainInfo has 38 direct strain rows and 102 deposit-taxonomy hits under taxon `5063`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:5063` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the merged old IDs.
- The aggregate GOLD transform supplies a taxon-level organism count of three and correctly leaves descendant taxon evidence to child records.
- The local native GOLD snapshot has three exact organism rows, four linked sequencing projects, and one linked analysis, with no matched BacDive-derived local strain identifiers to join through.
- BacDive does not supply exact local strain records for this taxon, and the native StrainInfo records do not produce generated overlay rows.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- GOLD analyses for this taxon are linked through project IDs, so the native scan checked `AP PROJECT GOLD IDS` as well as direct `AP ORGANISM GOLD ID` values.
