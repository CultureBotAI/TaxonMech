# YAML Record Review: Aspergillus cervinus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_cervinus.yaml
- Started UTC: 2026-09-21T16:39:09Z
- Finished UTC: 2026-09-21T16:40:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41749 |
| label | Aspergillus cervinus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_cervinus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_cervinus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_cervinus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_cervinus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4878 has `NCBITaxon:41749`, label `Aspergillus cervinus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, related synonym `Aspergillus cervinus Massee, 1914`, and source `gold`. `curation/seed_scope.tsv` line 52490 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720872` subgenus `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` records `NCBITaxon:1928187` as merged into `NCBITaxon:41749`, but the old ID is not a retained row in `data/raw/ncbitaxon_taxa.tsv`. The record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 4878 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52490 | Supported exactly: `attested rule: Aspergillus cervinus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34941 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41749`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 207049-207064 | Supported exactly with 16 rows: four culture-from-neotype designations for `NRRL 5025`, 10 culture-from-type-material designations for `ATCC 16915`, `CBS 537.65`, `IMI 126542`, `QM 8875`, and `WB 5025`, and two neotype designations for `CBS 196.64`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41749` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`; exact checks of `data/straininfo/exclusions.tsv`, `assemblies.tsv`, and `related_records.tsv.gz` | Supported; 18 StrainInfo rows referenced this taxon through direct or deposit-level taxon assertions, including exact type-material designations, but all were excluded as `no_eligible_own_deposit_match` and none generated assemblies or related records. |

Native GOLD contains one exact organism row, `Go0446089` for `CBS 196.64`, and two sequencing-project rows, `Gp0312186` and `Gp0317275`, for that organism. It has no analysis row linked through either `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`, and no `CBS 196.64` row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one synonym, the old-ID merge context reviewed above, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and two sequencing-project rows for `CBS 196.64`; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo supplies 18 rows that reference this taxon, but all are excluded from the overlay because there is no eligible BacDive-derived local strain for those StrainInfo records.
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
