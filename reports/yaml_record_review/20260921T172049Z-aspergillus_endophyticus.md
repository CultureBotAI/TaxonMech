# YAML Record Review: Aspergillus endophyticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_endophyticus.yaml
- Started UTC: 2026-09-21T17:19:49Z
- Finished UTC: 2026-09-21T17:20:49Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1924927 |
| label | Aspergillus endophyticus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_endophyticus.yaml`. It carries two NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_endophyticus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_endophyticus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_endophyticus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 495709 has `NCBITaxon:1924927`, label `Aspergillus endophyticus`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, related synonyms `Aspergillus endophyticus Hubka, A.J. Chen, & Samson, 2017` and `Aspergillus sp. 13 VH-2016`, and source `gold`. `curation/seed_scope.tsv` line 61627 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720874` subgenus `Aspergillus subgen. Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:1924927`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 495709 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61627 | Supported exactly: `attested rule: Aspergillus endophyticus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 17593 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1924927`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` exact scan | Supported; no NCBI `typematerial.dmp` rows are filed under `NCBITaxon:1924927`. |
| Empty BacDive strain surface | Exact taxon scan of `data/bacdive/records.jsonl.gz`; exact `DTO 354-I2` quoted-token scan of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1924927` or the native GOLD culture token. |
| Empty StrainInfo overlay | Exact direct and deposit taxon scans of `data/straininfo/records.jsonl.gz`; exact `DTO 354-I2` quoted-token scan of `data/straininfo/records.jsonl.gz` | Supported; no StrainInfo record asserted taxon ID `1924927` through its direct strain taxon or any deposit taxon, and none carried the native GOLD culture token as an exact JSON string value. |

Native GOLD contains one exact organism row for `DTO 354-I2` and three linked sequencing-project rows. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and two synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and three sequencing projects for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, type-material, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
