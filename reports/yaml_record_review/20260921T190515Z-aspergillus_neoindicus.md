# YAML Record Review: Aspergillus neoindicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_neoindicus.yaml
- Started UTC: 2026-09-21T19:04:01Z
- Finished UTC: 2026-09-21T19:05:15Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1641034 |
| label | Aspergillus neoindicus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_neoindicus.yaml`. It carries two NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_neoindicus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_neoindicus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_neoindicus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 427950 has `NCBITaxon:1641034`, label `Aspergillus neoindicus`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, two exact synonyms, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 60946 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` line 76821 redirects old ID `NCBITaxon:41902` into `NCBITaxon:1641034`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 427950 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60946 | Supported exactly: `attested rule: Aspergillus neoindicus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 14066 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1641034`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 49047-49054 | Supported exactly with `CBS 444.75`, `IMI 334935`, `ITCC 1575`, and `NRRL 6134` type-material designations plus colon-normalized variants under taxon name `Aspergillus neoindicus`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported as empty for the local native snapshot; no exact organism, project, or analysis row targets taxon ID `1641034`. |
| BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported as empty; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1641034` or the reviewed NCBI designations. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has one direct record under `NCBITaxon:1641034` and no assembly or related-record overlay rows for this target. |

The aggregate GOLD count is present in `data/raw/gold_organisms.tsv`. The local native GOLD snapshot does not contain an exact organism, sequencing-project, or analysis row for this taxon; correspondingly, no native GOLD row generates strain, assembly, genome, or related-record assertions.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no exact organism row for this taxon, and the GOLD adapter has no BacDive-derived local strain identifier to join through.
- StrainInfo has an exact direct record for this taxon but no assembly, exclusion, or related-record overlay rows.
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
- The exact quoted-token scan found `CBS 444.75`, `IMI 334935`, and `NRRL 6134` in a StrainInfo deposit row, but those deposits are filed under `Fennellia flavipes`, NCBI taxon `1588043`, and `Aspergillus niveus`, NCBI taxon `41281`; they are not exact taxonomic support for `NCBITaxon:1641034`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
