# YAML Record Review: Aspergillus mottae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_mottae.yaml
- Started UTC: 2026-09-21T18:52:40Z
- Finished UTC: 2026-09-21T18:53:48Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1034302 |
| label | Aspergillus mottae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_mottae.yaml`. It carries three NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_mottae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_mottae.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_mottae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 221570 has `NCBITaxon:1034302`, label `Aspergillus mottae`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 57249 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` lines 1746 and 1753 redirect old IDs `NCBITaxon:1051591` and `NCBITaxon:1051598` into `NCBITaxon:1034302`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 221570 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 57249 | Supported exactly: `attested rule: Aspergillus mottae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 464 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1034302`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 1715-1719 | Supported exactly with the `CBS 130016` culture-from-holotype designation, its colon-normalized variant, and `09MAsp200` plus `MUM 10.231` holotype designations under taxon name `Aspergillus mottae`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with organism `Go0108179`, strain `CBS 130016`, and two linked sequencing projects; no local native analysis row targeted this organism or its projects. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1034302` or the reviewed NCBI/native GOLD designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; StrainInfo has no direct strain record, deposit-taxonomy record, assembly overlay, or related-record overlay for `NCBITaxon:1034302`. |

The native GOLD `Aspergillus mottae CBS 130016` organism links to two BioProjects, but that GOLD evidence does not emit `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows because `CBS 130016` is absent from the BacDive-derived local strain inventory.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row and two sequencing projects for this taxon, with no matched BacDive-derived local strain identifier to join through.
- StrainInfo and BacDive do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The native GOLD organism and the NCBI culture-from-holotype row agree on `CBS 130016`, but no BacDive or StrainInfo row for that designation is filed under `NCBITaxon:1034302`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
