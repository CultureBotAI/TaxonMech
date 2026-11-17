# YAML Record Review: Aspergillus inflatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_inflatus.yaml
- Started UTC: 2026-09-21T18:16:51Z
- Finished UTC: 2026-09-21T18:18:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:69776 |
| label | Aspergillus inflatus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720873 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_inflatus.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_inflatus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_inflatus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_inflatus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 9672 has `NCBITaxon:69776`, label `Aspergillus inflatus`, rank `SPECIES`, direct parent `NCBITaxon:2720873`, genetic code `1`, exact synonym `Penicillium inflatum`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53185 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Cremei`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:69776`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 9672 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53185 | Supported exactly: `attested rule: Aspergillus inflatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 41543 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:69776`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 258122-258127 | Supported exactly with six `typematerial.dmp` culture-from-holotype and type-material designations for `CBS 682.70`, `FRR 1549`, `IMI 191498`, and their colon-normalized variants under taxon name `Penicillium inflatum`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `69776` or the reviewed NCBI type-material and GOLD culture designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has eighteen direct strain records and eighteen matching deposit-taxonomy records for taxon ID `69776`, including one entry with exact type-material strings, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:69776`. |

Native GOLD contains one exact organism row for `CBS 123889` and two linked sequencing-project rows. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and two sequencing projects for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo has exact taxon records, but no assembly or related-record exports for them and no BacDive-derived strains to overlay.
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
