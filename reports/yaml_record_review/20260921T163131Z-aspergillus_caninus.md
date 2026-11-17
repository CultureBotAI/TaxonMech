# YAML Record Review: Aspergillus caninus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_caninus.yaml
- Started UTC: 2026-09-21T16:30:17Z
- Finished UTC: 2026-09-21T16:31:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:743110 |
| label | Aspergillus caninus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720783 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_caninus.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_caninus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_caninus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_caninus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 171275 has `NCBITaxon:743110`, label `Aspergillus caninus`, rank `SPECIES`, direct parent `NCBITaxon:2720783`, genetic code `1`, exact synonym `Phialosimplex caninus`, related synonyms `Aspergillus caninus (Sigler, Deanna A. Sutton, Gibas, Summerbell & Iwen) Houbraken, Tanney, Visagie & Samson, 2015` and `Phialosimplex caninus Sigler, Deanna A. Sutton, Gibas, Summerb. & Iwen, 2010`, and source `gold`. `curation/seed_scope.tsv` line 56575 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720783` subgenus `Aspergillus subgen. Polypaecilum`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 171275 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56575 | Supported exactly: `attested rule: Aspergillus caninus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 42126 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:743110`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 261248-261251 | Supported exactly with four `type material` designation rows from `typematerial.dmp`, keyed to `NCBITaxon:743110` and named `Phialosimplex caninus`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `743110`. |
| Empty generated StrainInfo overlay | Exact scans of `data/straininfo/exclusions.tsv`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` for the matching StrainInfo IDs | Supported; both exact StrainInfo rows for this taxon have `no_eligible_own_deposit_match` exclusions and produced no generated assembly or related-record rows. |

The local native GOLD snapshot has no organism, sequencing-project, or analysis-project row whose `ORGANISM NCBI TAX ID` is `743110`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one exact synonym, two related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no exact organism row for taxon ID `743110`; this is not a YAML defect because the generated taxon-level GOLD count is sourced from `data/raw/gold_organisms.tsv`.
- StrainInfo supplies exact rows for this taxon, but both were excluded from the generated overlay because they had no eligible own-deposit match to the BacDive-derived local strain inventory.
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
