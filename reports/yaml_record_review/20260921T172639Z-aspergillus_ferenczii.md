# YAML Record Review: Aspergillus ferenczii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_ferenczii.yaml
- Started UTC: 2026-09-21T17:25:37Z
- Finished UTC: 2026-09-21T17:26:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:454254 |
| label | Aspergillus ferenczii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_ferenczii.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_ferenczii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_ferenczii.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_ferenczii.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 101654 has `NCBITaxon:454254`, label `Aspergillus ferenczii`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, exact synonym `Neosartorya ferenczii`, related synonyms `Aspergillus ferenczii (Varga & Samson) Samson, Varga, Visagie & Houbraken, 2014`, `Neosartorya ferenczii Varga & Samson, 2007`, and `Neosartorya sp. NRRL 4179`, and source `gold`. `curation/seed_scope.tsv` line 55712 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly. NCBI places this species directly under genus `NCBITaxon:5052`, so the generated record has no subgenus between `Aspergillus` and the species.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:454254`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 101654 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55712 | Supported exactly: `attested rule: Aspergillus ferenczii, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35997 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:454254`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 214386-214393 | Supported exactly with eight `typematerial.dmp` culture-from-holotype designations for `CBS 121594`, `DTO24F2`, `IBT 27813`, and `NRRL 4179`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `454254` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz` | Supported; no StrainInfo record asserted taxon ID `454254` through its direct strain taxon or any deposit taxon. The exact `NRRL 4179` string appears once only in a StrainInfo record assigned to `NCBITaxon:41049`. |

The aggregate GOLD transform contributes one organism assertion, while the local native GOLD snapshot has no exact organism, linked project, or linked isolate-analysis rows for this taxon. The YAML's GOLD source attestation is therefore aggregate-only and still supported by `data/raw/gold_organisms.tsv`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, four synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- BacDive, StrainInfo, and native GOLD do not supply exact records for this taxon.
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
