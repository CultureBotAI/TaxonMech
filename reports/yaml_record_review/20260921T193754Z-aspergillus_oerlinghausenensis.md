# YAML Record Review: Aspergillus oerlinghausenensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_oerlinghausenensis.yaml
- Started UTC: 2026-09-21T19:36:41Z
- Finished UTC: 2026-09-21T19:37:54Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1774284 |
| label | Aspergillus oerlinghausenensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_oerlinghausenensis.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_oerlinghausenensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_oerlinghausenensis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_oerlinghausenensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 462870 has `NCBITaxon:1774284`, label `Aspergillus oerlinghausenensis`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 61240 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no rows redirecting old IDs into `NCBITaxon:1774284`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 462870 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61240 | Supported exactly: `attested rule: Aspergillus oerlinghausenensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15455 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1774284`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 58346-58349 | Supported exactly with `CBS 139183` and `DTO 316-A3` culture-from-holotype variants for `Aspergillus oerlinghausenensis`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism row and three linked sequencing projects. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1774284` or the reviewed NCBI/native GOLD designations. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:1774284`. |

The native GOLD snapshot has the exact organism `Aspergillus oerlinghausenensis CBS 139183` on line 304883, with minimal-draft project `Gp0312178` on line 211419 and transcriptome projects `Gp0348452` and `Gp0397224` on lines 241511 and 283798. No linked native GOLD genome-analysis rows are present in the local snapshot.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row and three linked sequencing projects for this taxon, with no genome analyses and no matched BacDive-derived local strain identifier to join through.
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
