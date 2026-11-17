# YAML Record Review: Aspergillus candidus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_candidus.yaml
- Started UTC: 2026-09-21T16:28:57Z
- Finished UTC: 2026-09-21T16:30:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41067 |
| label | Aspergillus candidus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_candidus.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_candidus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_candidus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_candidus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4768 has `NCBITaxon:41067`, label `Aspergillus candidus`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, related synonym `Aspergillus candidus Link, 1809`, and source `gold`. `curation/seed_scope.tsv` line 52467 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720871` subgenus `Aspergillus subgen. Circumdati`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 4768 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52467 | Supported exactly: `attested rule: Aspergillus candidus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34722 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41067`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 205652-205655 | Supported exactly with four culture-from-neotype designation rows from `typematerial.dmp`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41067`. |
| Empty generated StrainInfo overlay | Exact scans of `data/straininfo/exclusions.tsv`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` for the matching StrainInfo IDs | Supported; all 118 exact or deposit-only StrainInfo rows for this taxon have `no_eligible_own_deposit_match` exclusions and produced no generated assembly or related-record rows. |

Native GOLD contains one exact organism row, `Go0108069` for `CBS 102.13`, and two sequencing-project rows, `Gp0108069` and `Gp0108070`, for that organism. It has no analysis row linked through either `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`, and no `CBS 102.13` row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

The NCBI neotype labels `ATCC 1002` and `CBS 566.65` appear in the StrainInfo snapshot, but only on source rows excluded from the generated overlay because no matching BacDive-derived local strain exists.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and two sequencing-project rows for `CBS 102.13`; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo supplies exact and deposit-level rows for this taxon, but each was excluded from the generated overlay because it had no eligible own-deposit match to the BacDive-derived local strain inventory.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive, StrainInfo overlay, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
