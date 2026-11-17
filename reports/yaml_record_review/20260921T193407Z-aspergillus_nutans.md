# YAML Record Review: Aspergillus nutans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_nutans.yaml
- Started UTC: 2026-09-21T19:32:54Z
- Finished UTC: 2026-09-21T19:34:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41752 |
| label | Aspergillus nutans |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_nutans.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_nutans.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_nutans.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_nutans.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4880 has `NCBITaxon:41752`, label `Aspergillus nutans`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 52492 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no rows redirecting old IDs into `NCBITaxon:41752`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4880 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52492 | Supported exactly: `attested rule: Aspergillus nutans, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34943 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41752`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 207084-207095 | Supported exactly with NRRL culture-from-lectotype variants, CBS culture-from-neotype variants, and ATCC/IFO/QM culture-from-type-material variants for `Aspergillus nutans`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism row and three linked sequencing projects. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41752` or the reviewed NCBI/native GOLD designations. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has nine direct records under `NCBITaxon:41752` and no assembly, exclusion, or related-record overlay rows for this target. |

The native GOLD snapshot has the exact organism `Aspergillus nutans CBS 121.56` on line 304871, with minimal-draft project `Gp0312162` on line 211408 and transcriptome projects `Gp0317283` and `Gp0397206` on lines 216457 and 283783. StrainInfo has exact quoted-token hits for the NCBI type designations on line 50773, but those designations do not emit `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows because they do not join through a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
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
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
