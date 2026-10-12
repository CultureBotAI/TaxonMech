# YAML Record Review: Aspergillus flavus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_flavus.yaml
- Started UTC: 2026-09-21T17:31:30Z
- Finished UTC: 2026-09-21T17:33:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5059 |
| label | Aspergillus flavus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_flavus.yaml`. It carries three NCBI exact synonyms, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_flavus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_flavus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_flavus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2208 has `NCBITaxon:5059`, label `Aspergillus flavus`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, exact synonyms `Aspergillus flavus var. parvisclerotigenus`, `Aspergillus parvisclerotigenus`, and `Petromyces flavus`, related synonyms `Aspergillus flavus Link, 1809`, `Aspergillus flavus var. parvisclerotigenus Mich. Saito & Tsuruta, 1993`, `Aspergillus parvisclerotigenus (Mich. Saito & Tsuruta) Frisvad & Samson, 2005`, and `Petromyces flavus B.W. Horn, I. Carbone & G.G. Moore 2009`, and source `gold`. `curation/seed_scope.tsv` line 51918 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`. `data/raw/ncbitaxon_taxa.tsv` also contains child strain `NCBITaxon:332952` under this species; the GOLD source attestation correctly reports only rows filed directly under `NCBITaxon:5059`.

`data/raw/ncbi_merged_ids.tsv` redirects old ID `NCBITaxon:422207` into `NCBITaxon:5059`, but exact first-column scanning of `data/raw/ncbitaxon_taxa.tsv` found no retained retired row for that old ID; the record therefore has no generated predecessor to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2208 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51918 | Supported exactly: `attested rule: Aspergillus flavus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37422 | Supported exactly with 78 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5059`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 225376-225391 | Supported exactly with 16 `typematerial.dmp` culture-from-neotype designations for `ATCC 16883`, `CBS 569.65`, `IMI 124930`, and `NRRL 1957` variants under taxon name `Aspergillus flavus`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5059` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has 663 direct strain records and 735 deposit-taxonomy records for taxon ID `5059`, including one entry with the exact `ATCC 16883`, `CBS 569.65`, `IMI 124930`, and `NRRL 1957` neotype strings, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:5059`. |

Native GOLD contains 78 exact organism rows for this taxon, 93 linked sequencing-project rows, and 46 linked analysis rows through `AP PROJECT GOLD IDS`. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, seven synonyms, the reviewed type-material designations, one child strain taxon, and one unretained old-ID merge into this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of 78, filed directly under this taxon.
- The local native GOLD snapshot has 78 organisms, 93 sequencing projects, and 46 linked analyses for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo has direct records for this taxon, but no assembly or related-record exports for it and no BacDive-derived strain to overlay.
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
- The old-ID absence check used exact first-column scanning of `data/raw/ncbitaxon_taxa.tsv`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
