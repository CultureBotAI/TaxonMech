# YAML Record Review: Aspergillus coreanus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_coreanus.yaml
- Started UTC: 2026-09-21T16:50:58Z
- Finished UTC: 2026-09-21T16:52:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:151553 |
| label | Aspergillus coreanus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_coreanus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_coreanus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_coreanus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_coreanus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 31453 has `NCBITaxon:151553`, label `Aspergillus coreanus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, related synonym `Aspergillus coreanus S.B. Hong, Frisvad & Samson, 2006`, and source `gold`. `curation/seed_scope.tsv` line 54074 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720872` subgenus `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:151553`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 31453 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54074 | Supported exactly: `attested rule: Aspergillus coreanus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 11949 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:151553`. |
| Empty BacDive strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `151553`. |
| Empty StrainInfo overlay | Exact direct and deposit taxon scans of `data/straininfo/records.jsonl.gz` | Supported; no StrainInfo record asserted taxon ID `151553` through its direct strain taxon or any deposit taxon. |

The local native GOLD snapshot has no exact organism row for `NCBITaxon:151553`; the source attestation is therefore limited to the committed aggregate `data/raw/gold_organisms.tsv` count. This is not a YAML defect because the aggregate transform can retain KG-Microbe GOLD evidence that is not represented by an exact row in the current local native GOLD JSONL files.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and one synonym.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- BacDive and StrainInfo do not supply exact records for this taxon.
- The local native GOLD snapshot has no exact rows for the target taxon.
- LPSN, GTDB, causal-graph, curated-evidence, and NCBI type-material sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The absence of NCBI type-material rows means there is no eukaryotic type-material evidence to suppress from `nomenclature` for this record.
