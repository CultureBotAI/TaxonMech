# YAML Record Review: Aspergillus caespitosus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_caespitosus.yaml
- Started UTC: 2026-09-21T16:25:20Z
- Finished UTC: 2026-09-21T16:26:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:176165 |
| label | Aspergillus caespitosus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_caespitosus.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_caespitosus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_caespitosus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_caespitosus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 35684 has `NCBITaxon:176165`, label `Aspergillus caespitosus`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, related synonym `Aspergillus caespitosus Raper & Thom, 1944`, and source `gold`. `curation/seed_scope.tsv` line 54293 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720870` subgenus `Aspergillus subgen. Nidulantes`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 35684 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54293 | Supported exactly: `attested rule: Aspergillus caespitosus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15330 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:176165`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 57407-57410 | Supported exactly with four culture-from-neotype or neotype designation rows from `typematerial.dmp`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `176165`. |
| Empty generated StrainInfo overlay | Exact scans of `data/straininfo/exclusions.tsv`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` for the matching StrainInfo IDs | Supported; all nine exact StrainInfo rows for this taxon have `no_eligible_own_deposit_match` exclusions and produced no generated assembly or related-record rows. |

The local native GOLD snapshot has no organism, sequencing-project, or analysis-project row whose `ORGANISM NCBI TAX ID` is `176165`.

The NCBI type-material labels `NRRL 1929` and `CBS 103.45` appear on StrainInfo SI-ID 265529, which is filed directly under `Aspergillus caespitosus`; that StrainInfo row is excluded from the generated overlay because no matching BacDive-derived local strain exists.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no exact organism row for taxon ID `176165`; this is not a YAML defect because the generated taxon-level GOLD count is sourced from `data/raw/gold_organisms.tsv`.
- StrainInfo supplies exact rows for this taxon, but each was excluded from the generated overlay because it had no eligible own-deposit match to the BacDive-derived local strain inventory.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive, StrainInfo overlay, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
