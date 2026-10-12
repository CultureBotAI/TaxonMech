# YAML Record Review: Aspergillus hiratsukae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_hiratsukae.yaml
- Started UTC: 2026-09-21T18:06:00Z
- Finished UTC: 2026-09-21T18:07:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1194566 |
| label | Aspergillus hiratsukae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_hiratsukae.yaml`. It carries two NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_hiratsukae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_hiratsukae.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_hiratsukae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 268714 has `NCBITaxon:1194566`, label `Aspergillus hiratsukae`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, two exact synonyms, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 58263 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` line 94639 redirects old ID `NCBITaxon:75549` into `NCBITaxon:1194566`. An exact first-column scan of `data/raw/ncbitaxon_taxa.tsv` for that old ID returned no retained retired row, so the record has no `replaces` value to list.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 268714 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58263 | Supported exactly: `attested rule: Aspergillus hiratsukae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 4634 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1194566`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 12735-12738 | Supported exactly with four `typematerial.dmp` type-material designations for `CBS 294.93`, `NHL 3008`, and their colon-normalized variants under taxon name `Aspergillus hiratsukae`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1194566` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has sixteen direct strain records and sixteen matching deposit-taxonomy records for taxon ID `1194566`, including one entry with exact type-material strings, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:1194566`. |

The local native GOLD snapshot contains two exact organism rows, `CNM-CM6106` and `CNM-CM5793`, with two linked sequencing-project rows and two project-linked analysis rows. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, one old merged ID, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot has two organisms, two sequencing projects, and two project-linked analyses for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
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

- The old NCBI ID merged into this current taxon does not become a `replaces` value because it is absent from the retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
