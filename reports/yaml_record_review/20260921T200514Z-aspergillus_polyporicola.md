# YAML Record Review: Aspergillus polyporicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_polyporicola.yaml
- Started UTC: 2026-09-21T20:04:00Z
- Finished UTC: 2026-09-21T20:05:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1588045 |
| label | Aspergillus polyporicola |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_polyporicola.yaml`. It carries two NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_polyporicola.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_polyporicola.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_polyporicola.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 410644 has `NCBITaxon:1588045`, label `Aspergillus polyporicola`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 60542 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` line 78930 redirects old ID `NCBITaxon:454255` into `NCBITaxon:1588045`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 410644 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60542 | Supported exactly: `attested rule: Aspergillus polyporicola, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 12830 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1588045`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 44742-44749 | Supported exactly with `CCF 4553` and `NRRL 32683` culture-from-holotype variants plus `PRM 923452` holotype and `PRM 923453` isotype variants for `Aspergillus polyporicola`. |
| Native GOLD evidence | Exact native GOLD organism and sequencing-project scans | Supported exactly with one exact organism row and three linked sequencing projects under NCBI taxon `1588045`. |
| Empty BacDive strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1588045`. |
| Empty StrainInfo overlay surface | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; no direct, deposit-taxonomy, assembly, exclusion, or related-record rows are filed under `NCBITaxon:1588045`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1588045`. |

The native GOLD snapshot has one exact organism row, `Go0446118` for `Aspergillus polyporicola DTO 316-C2` on line 304913. It joins to minimal-draft project `Gp0312215` on line 211447 and transcriptome projects `Gp0487760` and `Gp0509206` on lines 349013 and 368453, with no linked genome-analysis rows.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two related synonyms, the merged old ID, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism with three linked sequencing projects, no genome analyses, and no matched BacDive-derived local strain identifier to join through.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
