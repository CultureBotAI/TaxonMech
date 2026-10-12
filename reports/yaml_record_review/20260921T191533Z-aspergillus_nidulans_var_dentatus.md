# YAML Record Review: Aspergillus nidulans var. dentatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_nidulans_var_dentatus.yaml
- Started UTC: 2026-09-21T19:14:19Z
- Finished UTC: 2026-09-21T19:15:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:286160 |
| label | Aspergillus nidulans var. dentatus |
| rank | VARIETAS |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:162425 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic varietas record at `data/taxa/eukaryota/aspergillus_nidulans_var_dentatus.yaml`. It carries three NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_nidulans_var_dentatus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_nidulans_var_dentatus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_nidulans_var_dentatus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 58513 has `NCBITaxon:286160`, label `Aspergillus nidulans var. dentatus`, rank `VARIETAS`, direct parent `NCBITaxon:162425`, genetic code `1`, three exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55001 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate species parent `Aspergillus nidulans`.

`data/raw/ncbi_merged_ids.tsv` line 76718 redirects old ID `NCBITaxon:41741` into `NCBITaxon:286160`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 58513 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55001 | Supported exactly: `attested rule: Aspergillus nidulans var. dentatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 27796 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:286160`. |
| NCBI type-material inventory | Exact `data/raw/ncbi_type_material.tsv` scan | Supported; no NCBI type-material rows are filed under `NCBITaxon:286160`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism row and three linked sequencing projects. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `286160` or the reviewed NCBI/native GOLD designations. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has eight direct records under `NCBITaxon:286160` and no assembly, exclusion, or related-record overlay rows for this target. |

The native GOLD snapshot has the exact organism `Aspergillus dentatus CBS 114.63` on line 59800, with standard-draft project `Gp0108105` on line 61485 and transcriptome projects `Gp0248677` and `Gp0397232` on lines 164123 and 283804. StrainInfo also has an exact `CBS 114.63` deposit on line 88844, but that designation does not emit `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows because it does not join through a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and no type-material designations for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row and three linked sequencing projects for this taxon, with no genome analyses and no matched BacDive-derived local strain identifier to join through.
- StrainInfo has exact direct and deposit-taxonomy rows for this taxon but no assembly, exclusion, or related-record overlay rows.
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
- Native GOLD's exact organism row carries `CBS 114.63` as both `ORGANISM CULTURE COLLECTION ID` and `ORGANISM STRAIN`, and the exact StrainInfo token scan found the same designation once under `NCBITaxon:286160`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
