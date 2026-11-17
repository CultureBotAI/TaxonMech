# YAML Record Review: Aspergillus peyronelii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_peyronelii.yaml
- Started UTC: 2026-09-21T19:58:45Z
- Finished UTC: 2026-09-21T20:00:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:176177 |
| label | Aspergillus peyronelii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_peyronelii.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_peyronelii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_peyronelii.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_peyronelii.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 35691 has `NCBITaxon:176177`, label `Aspergillus peyronelii`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54300 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` lines 26414 and 31811 redirect old IDs `NCBITaxon:176162` and `NCBITaxon:1907206` into `NCBITaxon:176177`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 35691 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54300 | Supported exactly: `attested rule: Aspergillus peyronelii, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15338 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:176177`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 57497-57514 | Supported exactly with `Aspergillus arenarius` lectotype/neotype/type-material variants and `Aspergillus peyronelii` holotype/lectotype variants. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; the current local native GOLD projection has no exact organism, project, or analysis rows under NCBI taxon `176177`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `176177`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:176177`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:176177`. |

The aggregate GOLD transform contains one organism assertion for `NCBITaxon:176177`, while the current native GOLD projection has zero exact organism rows for numeric taxon ID `176177`. The YAML correctly follows `data/raw/gold_organisms.tsv`, which is the aggregate attestation source used during seeding.

Native StrainInfo has three direct strain rows and 17 deposit-taxonomy hits under taxon `176177`, including type-strain deposits for `ATCC 16840` and `ATCC 16830`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:176177` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, the merged old IDs, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The current local native GOLD snapshot has no exact organism/project/analysis chain for this taxon.
- BacDive does not supply exact local strain records for this taxon, and the native StrainInfo records do not produce generated overlay rows.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The GOLD aggregate in `data/raw/gold_organisms.tsv` can differ from the count of exact rows in the native GOLD projection; the YAML assertion count correctly follows the aggregate raw inventory.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
