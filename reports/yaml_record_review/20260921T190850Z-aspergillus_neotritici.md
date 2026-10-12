# YAML Record Review: Aspergillus neotritici

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_neotritici.yaml
- Started UTC: 2026-09-21T19:07:37Z
- Finished UTC: 2026-09-21T19:08:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2932460 |
| label | Aspergillus neotritici |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_neotritici.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_neotritici.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_neotritici.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_neotritici.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 573323 has `NCBITaxon:2932460`, label `Aspergillus neotritici`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 63379 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` lines 31052 and 80820 redirect old IDs `NCBITaxon:1883084` and `NCBITaxon:478866` into `NCBITaxon:2932460`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 573323 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 63379 | Supported exactly: `attested rule: Aspergillus neotritici, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 28904 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:2932460`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 143472-143483 | Supported exactly with `CCF` culture-from-holotype variants, `PRM` holotype variants, and `CBS 266.81` culture-from-reference-material variants under the accepted and exact-synonym taxon names. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with two organism rows, two linked sequencing projects, and two genome analyses linked through `AP PROJECT GOLD IDS`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2932460` or the reviewed NCBI/native GOLD designations. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has sixteen direct records under `NCBITaxon:2932460` and no assembly or related-record overlay rows for this target. |

The native GOLD snapshot has `Aspergillus tritici S2209` and `Aspergillus tritici PF2201` organism/project pairs plus genome analyses `Ga0663519` and `Ga0663520`, but that GOLD evidence does not emit `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows because neither `S2209` nor `PF2201` is present in the BacDive-derived local strain inventory.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot has two organism rows, two sequencing projects, and two genome analyses for this taxon, with no matched BacDive-derived local strain identifier to join through.
- StrainInfo has exact direct records for this taxon but no assembly, exclusion, or related-record overlay rows.
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
- The exact `CBS 266.81` quoted-token scan found a StrainInfo deposit under `Aspergillus candidus`, NCBI taxon `41067`; it is not exact taxonomic support for `NCBITaxon:2932460`.
- The native GOLD analysis rows leave `AP ORGANISM GOLD ID` blank but name projects `Gp0702026` and `Gp0702027` in `AP PROJECT GOLD IDS`; the project exact scan accounts for these links.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
