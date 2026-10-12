# YAML Record Review: Aspergillus nidulans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_nidulans.yaml
- Started UTC: 2026-09-21T19:08:51Z
- Finished UTC: 2026-09-21T19:12:49Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:162425 |
| label | Aspergillus nidulans |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_nidulans.yaml`. It carries four NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_nidulans.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_nidulans.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_nidulans.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 33422 has `NCBITaxon:162425`, label `Aspergillus nidulans`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, four exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54199 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` line 82605 redirects old ID `NCBITaxon:5072` into `NCBITaxon:162425`, but the old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 33422 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54199 | Supported exactly: `attested rule: Aspergillus nidulans, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 13907 | Supported exactly with 113 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:162425`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 47837-47838 | Supported exactly with `ATCC 10074` and `ATCC:10074` culture-from-neotype designations under exact synonym `Sterigmatocystis nidulans`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with 106 organism rows, 211 linked sequencing projects, and two genome analyses linked through `AP PROJECT GOLD IDS`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `162425` or the reviewed NCBI/native GOLD designations. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has 1,317 direct records and 1,333 exact deposit-taxonomy rows under `NCBITaxon:162425`, with no assembly, exclusion, or related-record overlay rows for this target. |

The native GOLD snapshot has many exact `Aspergillus nidulans` organism and sequencing-project records, including organism rows beginning at lines 2218, 2219, 53291, 56714, and 60604 and project rows beginning at lines 2248, 2249, 53024, 57598, and 62603. Genome analyses `Ga0032531` and `Ga0664105` link through sequencing projects `Gp0088989` and `Gp0702028`, respectively. None of the GOLD evidence emits `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows for this taxon because the exact GOLD culture and strain tokens do not join to a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of 113.
- The local native GOLD snapshot has 106 organism rows, 211 linked sequencing projects, and two genome analyses for this taxon, with no matched BacDive-derived local strain identifier to join through.
- StrainInfo has exact direct and deposit-taxonomy rows for this taxon but no assembly, exclusion, or related-record overlay rows.
- BacDive does not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- StrainInfo contains exact deposit records for `ATCC 10074`, `ATCC 38163`, `FGSC A713`, `FGSC A1146`, and `FGSC A1149`, but these do not overlay this generated record without a BacDive-derived local strain join.
- Native GOLD has 32 exact organism rows with non-empty `ORGANISM CULTURE COLLECTION ID` values, but those culture-collection tokens also do not join to a BacDive-derived local strain.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
