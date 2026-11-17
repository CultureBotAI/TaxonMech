# YAML Record Review: Aspergillus dromiae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_dromiae.yaml
- Started UTC: 2026-09-21T17:12:26Z
- Finished UTC: 2026-09-21T17:13:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2663347 |
| label | Aspergillus dromiae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_dromiae.yaml`. It carries two NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_dromiae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_dromiae.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_dromiae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 541313 has `NCBITaxon:2663347`, label `Aspergillus dromiae`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, related synonyms `Aspergillus dromiae A.J. Chen, Frisvad & Samson, 2016` and `Aspergillus sp. 3 AJC-2016`, and source `gold`. `curation/seed_scope.tsv` line 62925 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720870` subgenus `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` has one row that redirects `NCBITaxon:1810888` into `NCBITaxon:2663347`, but an exact first-column scan of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:1810888`. The generated YAML therefore has no `replaces` value to add.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 541313 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62925 | Supported exactly: `attested rule: Aspergillus dromiae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 24449 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2663347`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` exact scan | Supported; no NCBI `typematerial.dmp` rows are filed under `NCBITaxon:2663347`. |
| Empty BacDive strain surface | Exact taxon scan of `data/bacdive/records.jsonl.gz`; exact `CBS 140633` quoted-token scan of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2663347` or the native GOLD culture token. |
| Empty StrainInfo overlay | Exact direct and deposit taxon scans of `data/straininfo/records.jsonl.gz`; exact `CBS 140633` quoted-token scan of `data/straininfo/records.jsonl.gz` | Supported; no StrainInfo record asserted taxon ID `2663347` through its direct strain taxon or any deposit taxon, and none carried the native GOLD culture token as an exact JSON string value. |

Native GOLD contains one exact organism row for `CBS 140633` and two linked sequencing-project rows. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and two synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and two sequencing projects for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, type-material, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, native GOLD, and retained-retired-ID checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
