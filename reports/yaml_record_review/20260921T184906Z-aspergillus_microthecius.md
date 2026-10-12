# YAML Record Review: Aspergillus microthecius

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_microthecius.yaml
- Started UTC: 2026-09-21T18:48:05Z
- Finished UTC: 2026-09-21T18:49:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1883079 |
| label | Aspergillus microthecius |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_microthecius.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no NCBI type-material designations, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_microthecius.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_microthecius.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_microthecius.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 490332 has `NCBITaxon:1883079`, label `Aspergillus microthecius`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 61436 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:1883079`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 490332 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61436 | Supported exactly: `attested rule: Aspergillus microthecius, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 16924 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1883079`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported as empty; no committed NCBI type-material row targets `NCBITaxon:1883079`. |
| Empty BacDive strain surface | Exact taxon scan of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1883079`. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; StrainInfo has no direct strain record, deposit-taxonomy record, assembly overlay, or related-record overlay for `NCBITaxon:1883079`. |

The aggregate GOLD count is present in `data/raw/gold_organisms.tsv`. The local native GOLD snapshot does not contain an exact organism, sequencing-project, or analysis row for this taxon; correspondingly, no native GOLD row generates strain, assembly, genome, or related-record assertions.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and a related synonym.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no exact organism row for this taxon, and the GOLD adapter has no BacDive-derived local strain identifier to join through.
- StrainInfo and BacDive do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, curated-evidence, and type-material sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- No NCBI type-material rows were available for review; no strain-designation token scan was needed for this taxon.
