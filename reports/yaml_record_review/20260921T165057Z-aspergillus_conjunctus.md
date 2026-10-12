# YAML Record Review: Aspergillus conjunctus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_conjunctus.yaml
- Started UTC: 2026-09-21T16:49:51Z
- Finished UTC: 2026-09-21T16:50:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41746 |
| label | Aspergillus conjunctus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_conjunctus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_conjunctus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_conjunctus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_conjunctus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4877 has `NCBITaxon:41746`, label `Aspergillus conjunctus`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, related synonym `Aspergillus conjunctus Kwon-Chung & Fennell, 1965`, and source `gold`. `curation/seed_scope.tsv` line 52489 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720870` subgenus `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:41746`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 4877 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52489 | Supported exactly: `attested rule: Aspergillus conjunctus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34940 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41746`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 207035-207048 | Supported exactly with 14 rows: four culture-from-lectotype designations for `NRRL 5080`, two culture-from-neotype designations for `CBS 476.65`, and eight culture-from-type-material designations for `ATCC 16796`, `IMI 135421`, `QM 8878`, and `WB 5080`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41746` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`; exact checks of `data/straininfo/exclusions.tsv`, `assemblies.tsv`, and `related_records.tsv.gz` | Supported; one StrainInfo row asserted this taxon, including exact type-material designations, but it was excluded as `no_eligible_own_deposit_match` and generated no assemblies or related records. |

The local native GOLD snapshot has no exact organism row for `NCBITaxon:41746`; the source attestation is therefore limited to the committed aggregate `data/raw/gold_organisms.tsv` count. This is not a YAML defect because the aggregate transform can retain KG-Microbe GOLD evidence that is not represented by an exact row in the current local native GOLD JSONL files.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- StrainInfo supplies one taxon-linked row, but it is excluded from the overlay because there is no eligible BacDive-derived local strain for that StrainInfo record.
- BacDive does not supply exact records for this taxon or its reviewed type-material designations.
- The local native GOLD snapshot has no exact rows for the target taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
