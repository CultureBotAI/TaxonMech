# YAML Record Review: Aspergillus oleicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_oleicola.yaml
- Started UTC: 2026-09-21T19:37:55Z
- Finished UTC: 2026-09-21T19:39:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1250372 |
| label | Aspergillus oleicola |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_oleicola.yaml`. It carries three NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_oleicola.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_oleicola.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_oleicola.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 288704 has `NCBITaxon:1250372`, label `Aspergillus oleicola`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, three exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58691 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` lines 43754-43755 redirect old IDs `NCBITaxon:251367` and `NCBITaxon:251368` into `NCBITaxon:1250372`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 288704 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58691 | Supported exactly: `attested rule: Aspergillus oleicola, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 6015 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1250372`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 16960-16963 | Supported exactly with `CBS 119.37` culture-from-holotype variants and `IBT 21903` culture-from-type-material variants for `Aspergillus oleicola`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism row and two linked sequencing projects. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1250372` or the reviewed NCBI/native GOLD designations. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:1250372`. |

The native GOLD snapshot has one exact organism row by NCBI taxon, filed as `Aspergillus olivicola CBS 597.65` on line 59812, with linked standard-draft project `Gp0108129` and transcriptome project `Gp0108130` on lines 61507-61508. StrainInfo contains quoted `CBS 119.37` and `CBS 597.65` token hits, but those records are not filed under the reviewed NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row and two linked sequencing projects for this taxon, with no genome analyses and no matched BacDive-derived local strain identifier to join through.
- BacDive and StrainInfo do not supply exact records for this taxon.
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
