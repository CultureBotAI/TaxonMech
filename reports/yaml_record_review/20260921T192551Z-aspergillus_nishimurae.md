# YAML Record Review: Aspergillus nishimurae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_nishimurae.yaml
- Started UTC: 2026-09-21T19:24:07Z
- Finished UTC: 2026-09-21T19:25:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1220166 |
| label | Aspergillus nishimurae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_nishimurae.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_nishimurae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_nishimurae.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_nishimurae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 276580 has `NCBITaxon:1220166`, label `Aspergillus nishimurae`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58464 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` line 64206 redirects old ID `NCBITaxon:311974` into `NCBITaxon:1220166`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 276580 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58464 | Supported exactly: `attested rule: Aspergillus nishimurae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 5289 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1220166`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 14750-14755 | Supported exactly with `CBS 117265` and `IBT 3016` reference-material variants for `Aspergillus nishimurae`, plus `CBM FA-919` holotype variants for `Neosartorya nishimurae`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism row and one linked sequencing project. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1220166` or the reviewed NCBI/native GOLD designations. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has one direct record under `NCBITaxon:1220166` and no assembly, exclusion, or related-record overlay rows for this target. |

The native GOLD snapshot has the exact organism `Aspergillus nishimurae IFM 54133` on line 74707 and linked sequencing project `Gp0134052` on line 81898, with no linked genome-analysis rows. StrainInfo has exact strain record `siID` 145605 on line 98539, but its `IHEM 1377` deposit does not emit `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows because it does not join through a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row and one linked sequencing project for this taxon, with no genome analyses and no matched BacDive-derived local strain identifier to join through.
- StrainInfo has an exact direct record and deposit-taxonomy row for this taxon but no assembly, exclusion, or related-record overlay rows.
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
