# YAML Record Review: Aspergillus europaeus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_europaeus.yaml
- Started UTC: 2026-09-21T17:22:01Z
- Finished UTC: 2026-09-21T17:23:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:660491 |
| label | Aspergillus europaeus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720873 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_europaeus.yaml`. It carries three NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_europaeus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_europaeus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_europaeus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 152897 has `NCBITaxon:660491`, label `Aspergillus europaeus`, rank `SPECIES`, direct parent `NCBITaxon:2720873`, genetic code `1`, related synonyms `Aspergillus europaeus Hubka, A. Novakova, Samson, Houbraken, Frisvad & M. Kolarik, 2016`, `Aspergillus sp. 6 VH-2015`, and `Aspergillus sp. CBS 229.67`, and source `gold`. `curation/seed_scope.tsv` line 56299 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720873` subgenus `Aspergillus subgen. Cremei`.

`data/raw/ncbi_merged_ids.tsv` has one row that redirects `NCBITaxon:1762011` into `NCBITaxon:660491`, but an exact first-column scan of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:1762011`. The generated YAML therefore has no `replaces` value to add.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 152897 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56299 | Supported exactly: `attested rule: Aspergillus europaeus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40658 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:660491`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 246446-246453 | Supported exactly with eight `typematerial.dmp` culture-from-holotype designations for `CBS 134393`, `CCF 4409`, `IBT 32228`, and `NRRL 66252`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `660491` or the reviewed NCBI type-material designations. |
| Empty StrainInfo assembly and related-record surface | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, and generated raw strain tables | Supported; StrainInfo has four direct taxon matches for `660491`, but it emits no assembly, related-record, or generated strain rows for this taxon. The exact `CBS 229.67` string appears once only in a StrainInfo record assigned to `Aspergillus wentii`. |

The aggregate GOLD transform contributes one organism assertion, while the local native GOLD snapshot has no exact organism, linked project, or linked isolate-analysis rows for this taxon. The YAML's GOLD source attestation is therefore aggregate-only and still supported by `data/raw/gold_organisms.tsv`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, three synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local StrainInfo snapshot has four direct strain records for this taxon, but they have no local assembly or related-record export rows.
- BacDive and native GOLD do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, native GOLD, and retained-retired-ID checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
