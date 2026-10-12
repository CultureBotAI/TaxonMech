# YAML Record Review: Aspergillus cleistominutus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_cleistominutus.yaml
- Started UTC: 2026-09-21T16:48:43Z
- Finished UTC: 2026-09-21T16:49:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:210209 |
| label | Aspergillus cleistominutus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_cleistominutus.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_cleistominutus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_cleistominutus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_cleistominutus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 41362 has `NCBITaxon:210209`, label `Aspergillus cleistominutus`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, exact synonym `Emericella cleistominuta`, related synonyms `Aspergillus cleistominutus B.S. Mehrotra & R. Prasad` and `Emericella cleistominuta B.S. Mehrotra & R. Prasad, 1969`, and source `gold`. `curation/seed_scope.tsv` line 54515 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly. NCBI currently places `Aspergillus cleistominutus` directly under genus `Aspergillus` with no intervening subgenus row.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:210209`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 41362 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54515 | Supported exactly: `attested rule: Aspergillus cleistominutus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 20119 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:210209`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `210209` or the reviewed native GOLD designation. |
| Empty StrainInfo overlay | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`; exact checks of `data/straininfo/exclusions.tsv`, `assemblies.tsv`, and `related_records.tsv.gz` | Supported; one StrainInfo row asserted this taxon, but it was excluded as `no_eligible_own_deposit_match` and generated no assemblies or related records. |

Native GOLD contains one exact organism row, `Go0108101` for `CBS 200.75`; two sequencing-project rows, `Gp0108101` and `Gp0108102`; and one isolate genome analysis, `Ga0220800`, linked through `AP PROJECT GOLD IDS`. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and three synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism, two sequencing projects, and one project-linked analysis for `CBS 200.75`; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo supplies one taxon-linked row, but it is excluded from the overlay because there is no eligible BacDive-derived local strain for that StrainInfo record.
- BacDive does not supply exact records for this taxon or its reviewed GOLD designation.
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
