# YAML Record Review: Aspergillus brevipes

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_brevipes.yaml
- Started UTC: 2026-09-21T16:19:25Z
- Finished UTC: 2026-09-21T16:20:54Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:75551 |
| label | Aspergillus brevipes |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_brevipes.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_brevipes.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_brevipes.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_brevipes.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 10741 has `NCBITaxon:75551`, label `Aspergillus brevipes`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, related synonym `Aspergillus brevipes G. Smith, 1952`, and source `gold`. `curation/seed_scope.tsv` line 53276 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720872` subgenus `Aspergillus subgen. Fumigati`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 10741 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53276 | Supported exactly: `attested rule: Aspergillus brevipes, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 42377 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:75551`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 262344-262362 | Supported exactly with 19 designation rows from `typematerial.dmp`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `75551`. |
| Empty generated strain surface | Exact scans of `data/raw/culture_collection_strains.tsv`, `data/raw/strain_related_records.tsv`, `data/raw/strain_assemblies.tsv`, and `data/raw/strain_genome_records.tsv` | Supported; none of the raw seed tables contain a `NCBITaxon:75551` strain assertion. |

Raw StrainInfo contains one strain filed directly under `Aspergillus brevipes` and one additional strain with deposits that assert NCBITaxon:75551. The generated StrainInfo overlay also contains two `NCBITaxon:75551` related-record rows from SI-ID 63335 for `JCM 17347`, but those rows are attached to `kgmicrobe.strain:bacdive_16572`, a `Nonomuraea soli` BacDive strain. Because no BacDive-derived local strain is filed under `Aspergillus brevipes`, those overlay rows are not reachable from this record during seeding.

The local native GOLD snapshot has no organism, sequencing-project, or analysis-project row whose `ORGANISM NCBI TAX ID` is `75551`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no exact organism row for taxon ID `75551`; this is not a YAML defect because the generated taxon-level GOLD count is sourced from `data/raw/gold_organisms.tsv`.
- StrainInfo contains exact taxon assertions for `75551`, but TaxonMech uses StrainInfo as an overlay on BacDive-derived local strain rows and no such BacDive strain is filed under this species.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive, raw strain-table, StrainInfo overlay, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
