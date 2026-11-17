# YAML Record Review: Aspergillus fruticulosus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_fruticulosus.yaml
- Started UTC: 2026-09-21T17:39:00Z
- Finished UTC: 2026-09-21T17:39:46Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1250369 |
| label | Aspergillus fruticulosus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_fruticulosus.yaml`. It carries three NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_fruticulosus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_fruticulosus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_fruticulosus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 288703 has `NCBITaxon:1250369`, label `Aspergillus fruticulosus`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, exact synonyms `Aspergillus fructiculosa`, `Aspergillus fruticans`, and `Emericella fruticulosa`, related synonym `Aspergillus fruticulosus Raper & Fennell, 1965`, and source `gold`. `curation/seed_scope.tsv` line 58690 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` redirects old ID `NCBITaxon:41729` into `NCBITaxon:1250369`, but exact first-column scanning of `data/raw/ncbitaxon_taxa.tsv` found no retained retired row for that old ID; the record therefore has no generated predecessor to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 288703 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58690 | Supported exactly: `attested rule: Aspergillus fruticulosus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 6014 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1250369`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 16944-16959 | Supported exactly with 16 `typematerial.dmp` rows covering `NRRL 4903`, `CBS 486.65`, `ATCC 16823`, `IMI 139279`, `O-1077`, `QM 8033`, and `WB 4903` variants under taxon name `Aspergillus fruticulosus`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1250369` or the reviewed NCBI type-material and native-GOLD strain designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has six direct strain records and six deposit-taxonomy records for taxon ID `1250369`, including one entry with the exact reviewed NCBI type-material strings and one entry with the native-GOLD `CBS 989.72` string, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:1250369`. |

Native GOLD contains one exact organism row for `CBS 989.72` and two linked sequencing-project rows. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, four synonyms, the reviewed type-material designations, and one unretained old-ID merge into this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and two sequencing projects for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
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
- The old-ID absence check used exact first-column scanning of `data/raw/ncbitaxon_taxa.tsv`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
