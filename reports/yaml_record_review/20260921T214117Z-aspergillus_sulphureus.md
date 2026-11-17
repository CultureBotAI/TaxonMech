# YAML Record Review: Aspergillus sulphureus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_sulphureus.yaml
- Started UTC: 2026-09-21T21:40:01Z
- Finished UTC: 2026-09-21T21:41:17Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:138284 |
| label | Aspergillus sulphureus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_sulphureus.yaml`. It carries one related NCBI synonym, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_sulphureus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_sulphureus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_sulphureus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 27769 has `NCBITaxon:138284`, label `Aspergillus sulphureus`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, one related synonym, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 53987 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly through the immediate parent `Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:138284`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 27769 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53987 | Supported exactly: `attested rule: Aspergillus sulphureus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 8991 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:138284`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows are filed under taxon ID `138284`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, three sequencing projects, and one matching native GOLD analysis row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `138284`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 29 direct records and 47 deposit-taxonomy hits under `138284`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:138284`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:138284`. |

The native GOLD snapshot has one exact organism row on line 59859 for `Aspergillus sulphureus CBS 550.65` under NCBI taxon `138284`, strain `CBS 550.65`, and GOLD organism `Go0108227`. That organism joins to sequencing projects `Gp0108227`, `Gp0108228`, and `Gp0248662` on lines 61599, 61600, and 164108, and the native GOLD analysis row on line 134008 joins through `AP PROJECT GOLD IDS` to `Gp0108227`.

Native StrainInfo has 29 direct strain rows under taxon `138284`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus` parent, and the one related synonym.
- NCBI has no type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, three linked sequencing projects, and one linked genome analysis.
- BacDive does not supply exact local strain evidence for this taxon, and the native StrainInfo exact hits have no BacDive-derived local strain to overlay.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aspergillus sulphureus` as `SPECIES`, and the generated record follows the source rank exactly.
