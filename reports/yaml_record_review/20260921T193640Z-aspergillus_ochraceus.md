# YAML Record Review: Aspergillus ochraceus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_ochraceus.yaml
- Started UTC: 2026-09-21T19:35:19Z
- Finished UTC: 2026-09-21T19:36:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:40380 |
| label | Aspergillus ochraceus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_ochraceus.yaml`. It carries two NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_ochraceus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_ochraceus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_ochraceus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4587 has `NCBITaxon:40380`, label `Aspergillus ochraceus`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52425 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` line 59388 redirects old ID `NCBITaxon:2980028` into `NCBITaxon:40380`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4587 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52425 | Supported exactly: `attested rule: Aspergillus ochraceus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34517 | Supported exactly with fifteen aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:40380`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 204315-204318 | Supported exactly with `CBS 108.08` and `NRRL 398` culture-from-neotype variants for `Aspergillus ochraceus`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with twelve organism rows and five linked sequencing projects. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `40380` or the reviewed NCBI/native GOLD designations. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has 183 direct records and 187 deposit-taxonomy records under `NCBITaxon:40380`, with no assembly, exclusion, or related-record overlay rows for this target. |

The local native GOLD snapshot has exact organism rows for `Aspergillus ochraceus` strains `fc-1`, `ITEM 7043`, `MUT 2036`, `WB 398`, `QM 6731`, `NRRL 1642`, `IMI 016247`, `DSM 824`, `CMI 016247`, `CBS 108.08`, `ATCC 1008`, and `260-112`. Five native GOLD projects link to those organism rows, with no linked genome-analysis rows in the local snapshot.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of fifteen.
- The local native GOLD snapshot has twelve organism rows and five linked sequencing projects for this taxon, with no genome analyses and no matched BacDive-derived local strain identifier to join through.
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
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
