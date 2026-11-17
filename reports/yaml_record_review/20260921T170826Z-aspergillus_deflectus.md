# YAML Record Review: Aspergillus deflectus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_deflectus.yaml
- Started UTC: 2026-09-21T17:06:30Z
- Finished UTC: 2026-09-21T17:08:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41745 |
| label | Aspergillus deflectus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_deflectus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_deflectus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_deflectus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_deflectus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4876 has `NCBITaxon:41745`, label `Aspergillus deflectus`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, related synonym `Aspergillus deflectus Fennell & Raper, 1955`, and source `gold`. `curation/seed_scope.tsv` line 52488 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720870` subgenus `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:41745`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 4876 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52488 | Supported exactly: `attested rule: Aspergillus deflectus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34939 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41745`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 207019-207034 | Supported exactly with sixteen `typematerial.dmp` designations spanning culture-from-lectotype `NRRL 2206`, culture-from-neotype `CBS 109.55`, and culture-from-type-material `ATCC 16807`, `IMI 61448`, `QM 1904`, `UC4638`, and `WB 2206` aliases. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41745` or the reviewed NCBI type-material designations. |
| Empty StrainInfo assembly and related-record surface | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, and generated raw strain tables | Supported; StrainInfo has twelve direct taxon matches for `41745`, including exact type-token deposits for `CBS 109.55`, `ATCC 16807`, and `NRRL 2206`, but it emits no assembly, related-record, or generated strain rows for this taxon. |

The aggregate GOLD transform contributes one organism assertion, while the local native GOLD snapshot has no exact organism, linked project, or linked isolate-analysis rows for this taxon. The YAML's GOLD source attestation is therefore aggregate-only and still supported by `data/raw/gold_organisms.tsv`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local StrainInfo snapshot has twelve direct strain records for this taxon, but they have no local assembly or related-record export rows.
- BacDive and native GOLD do not supply exact records for this taxon.
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
