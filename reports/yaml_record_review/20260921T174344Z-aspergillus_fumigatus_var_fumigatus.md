# YAML Record Review: Aspergillus fumigatus var. fumigatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_fumigatus_var_fumigatus.yaml
- Started UTC: 2026-09-21T17:43:00Z
- Finished UTC: 2026-09-21T17:43:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41122 |
| label | Aspergillus fumigatus var. fumigatus |
| rank | VARIETAS |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:746128 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic variety record at `data/taxa/eukaryota/aspergillus_fumigatus_var_fumigatus.yaml`. It carries two NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_fumigatus_var_fumigatus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_fumigatus_var_fumigatus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_fumigatus_var_fumigatus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4770 has `NCBITaxon:41122`, label `Aspergillus fumigatus var. fumigatus`, rank `VARIETAS`, direct parent `NCBITaxon:746128`, genetic code `1`, exact synonyms `Aspergillus acolumnaris` and `Aspergillus fumigatus var. acolumnaris`, related synonym `Aspergillus fumigatus var. fumigatus Fresen., 1863`, and source `gold`. `curation/seed_scope.tsv` line 52468 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the parent species `Aspergillus fumigatus` and its subgenus `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:41122`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4770 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52468 | Supported exactly: `attested rule: Aspergillus fumigatus var. fumigatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34734 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41122`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 205751-205769 | Supported exactly with 19 `typematerial.dmp` rows covering the `Aspergillus fumigatus` type-material designations filed under `NCBITaxon:41122`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41122` or the reviewed NCBI type-material and native-GOLD strain designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has 130 direct strain records and 153 deposit-taxonomy records for taxon ID `41122`, including entries with the exact reviewed type-material strings and the native-GOLD `JCM 10253` string, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:41122`. |

Native GOLD contains one exact organism row for `JCM 10253`, one linked sequencing-project row, and one linked analysis row through `AP PROJECT GOLD IDS`. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies variety identity, lineage, genetic code, three synonyms, and the reviewed type-material designations.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism, one sequencing project, and one linked analysis for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo has direct records for this taxon, but no assembly or related-record exports for it and no BacDive-derived strain to overlay.
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
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
