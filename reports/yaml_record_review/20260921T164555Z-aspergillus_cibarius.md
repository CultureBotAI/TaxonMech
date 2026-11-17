# YAML Record Review: Aspergillus cibarius

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_cibarius.yaml
- Started UTC: 2026-09-21T16:44:37Z
- Finished UTC: 2026-09-21T16:45:55Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1235455 |
| label | Aspergillus cibarius |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_cibarius.yaml`. It carries eight NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_cibarius.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_cibarius.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_cibarius.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 282842 has `NCBITaxon:1235455`, label `Aspergillus cibarius`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, eight related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58612 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720874` subgenus `Aspergillus subgen. Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` records `NCBITaxon:1173310`, `NCBITaxon:1187067`, `NCBITaxon:1220169`, `NCBITaxon:1232855`, `NCBITaxon:1232856`, `NCBITaxon:1232857`, and `NCBITaxon:997103` as merged into `NCBITaxon:1235455`, but none of those old IDs is a retained row in `data/raw/ncbitaxon_taxa.tsv`. The record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 282842 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58612 | Supported exactly: `attested rule: Aspergillus cibarius, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 5630 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1235455`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 15823-15824 | Supported exactly with two culture-from-type-material designations for `KACC 46346`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1235455` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`; exact checks of `data/straininfo/exclusions.tsv`, `assemblies.tsv`, and `related_records.tsv.gz` | Supported; three StrainInfo rows asserted this taxon, but all were excluded as `no_eligible_own_deposit_match` and none generated assemblies or related records. |

Native GOLD contains one exact organism row, `Go0446112` for `DTO 197-D3`, and one sequencing-project row, `Gp0312209`, for that organism. It has no analysis row linked through either `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`, and no `DTO 197-D3` row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, eight synonyms, the old-ID merge context reviewed above, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and one sequencing-project row for `DTO 197-D3`; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo supplies three taxon-linked rows, but all are excluded from the overlay because there is no eligible BacDive-derived local strain for those StrainInfo records.
- BacDive does not supply exact records for this taxon or its reviewed type-material designations.
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
