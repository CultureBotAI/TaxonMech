# YAML Record Review: Aspergillus caperatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_caperatus.yaml
- Started UTC: 2026-09-21T16:32:32Z
- Finished UTC: 2026-09-21T16:33:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1924926 |
| label | Aspergillus caperatus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_caperatus.yaml`. It carries one NCBI exact synonym, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_caperatus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_caperatus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_caperatus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 495708 has `NCBITaxon:1924926`, label `Aspergillus caperatus`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, exact synonym `Aspergillus caperatus A.J. Chen, Frisvad & Samson, 2017`, related synonym `Aspergillus sp. 12 VH-2016`, and source `gold`. `curation/seed_scope.tsv` line 61626 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720874` subgenus `Aspergillus subgen. Aspergillus`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 495708 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61626 | Supported exactly: `attested rule: Aspergillus caperatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 17592 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1924926`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI `typematerial.dmp` row is keyed to `NCBITaxon:1924926`. |
| Empty BacDive strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1924926`. |
| Empty StrainInfo overlay | Exact direct and deposit taxon scans of `data/straininfo/records.jsonl.gz` | Supported; no StrainInfo record asserted taxon ID `1924926`. |

Native GOLD contains one exact organism row, `Go0446149` for `DTO 337-E6`, and three sequencing-project rows, `Gp0312246`, `Gp0487766`, and `Gp0509221`, for that organism. The native GOLD row spells the organism name `Aspergillus capperatus`, but its `ORGANISM NCBI TAX ID` is `1924926`; no exact `DTO 337-E6` string was found in BacDive or StrainInfo, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one exact synonym, and one related synonym.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and three sequencing-project rows for `DTO 337-E6`; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, NCBI type-material, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive, StrainInfo, native GOLD, and type-material checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The absence of `nomenclature` is expected for this eukaryotic record because TaxonMech generates nomenclature from LPSN only.
