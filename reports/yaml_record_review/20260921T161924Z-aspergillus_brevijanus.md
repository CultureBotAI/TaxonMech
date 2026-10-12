# YAML Record Review: Aspergillus brevijanus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_brevijanus.yaml
- Started UTC: 2026-09-21T16:17:10Z
- Finished UTC: 2026-09-21T16:19:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:176172 |
| label | Aspergillus brevijanus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_brevijanus.yaml`. It carries two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_brevijanus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_brevijanus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_brevijanus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 35688 has `NCBITaxon:176172`, label `Aspergillus brevijanus`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, related synonyms `Aspergillus brevijanus S.W. Peterson, 2008` and `Aspergillus janus var. brevis`, and source `gold`. `curation/seed_scope.tsv` line 54297 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720871` subgenus `Aspergillus subgen. Circumdati`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 35688 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54297 | Supported exactly: `attested rule: Aspergillus brevijanus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15334 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:176172`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 57442-57461 | Supported exactly with 20 `culture from holotype` designation rows from `typematerial.dmp`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz` | Supported; no exact BacDive record was filed under taxon ID `176172`, and none of the NCBI type-material designations appeared as exact JSON string values. |
| Empty StrainInfo overlay | Exact direct and deposit taxon scans of `data/straininfo/records.jsonl.gz` | Supported; no direct or deposit-only StrainInfo row asserted taxon ID `176172`. |

Native GOLD contains one exact organism row, `Go0108239` for `CBS 111.46`, and two sequencing-project rows, `Gp0108239` and `Gp0108240`, for that organism. It has no analysis row linked through either `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`, and no `CBS 111.46` row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

Several NCBI type-material labels, including `ATCC 16828`, `CBS 111.46`, `FRR 1935`, `IMI 016066`, `IMI 016066ii`, `NCTC 6971`, `NRRL 1935`, `QM 7417`, and `WB 1935`, appear on StrainInfo SI-ID 152901. That StrainInfo source row is filed under `Aspergillus janus` / NCBITaxon:176171 and no deposit asserts NCBITaxon:176172, so it is not an exact StrainInfo overlay for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and two sequencing-project rows for `CBS 111.46`; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
