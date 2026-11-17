# YAML Record Review: Aspergillus sclerotioniger CBS 115572

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_sclerotioniger_cbs_115572.yaml
- Started UTC: 2026-09-21T20:46:59Z
- Finished UTC: 2026-09-21T20:47:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1450535 |
| label | Aspergillus sclerotioniger CBS 115572 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:319627 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic strain at `data/taxa/eukaryota/aspergillus_sclerotioniger_cbs_115572.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_sclerotioniger_cbs_115572.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_sclerotioniger_cbs_115572.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_sclerotioniger_cbs_115572.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 366261 has `NCBITaxon:1450535`, label `Aspergillus sclerotioniger CBS 115572`, rank `STRAIN`, direct parent `NCBITaxon:319627`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 60190 keeps this strain in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate species parent `Aspergillus sclerotioniger`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:1450535`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this strain; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 366261 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60190 | Supported exactly: `attested rule: Aspergillus sclerotioniger CBS 115572, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 10967 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1450535`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows are filed under the strain-level taxon ID `1450535`. |
| Empty native GOLD surface | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; no native GOLD organism, project, or analysis row is filed directly under NCBI taxon `1450535`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1450535`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1450535`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1450535`. |

No native StrainInfo direct strain rows or deposit-taxonomy hits were filed under taxon `1450535`; all generated strain, assembly, and related-record tables are also empty for `NCBITaxon:1450535`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies strain identity, lineage, genetic code, and the direct species parent.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no exact organism, sequencing-project, or analysis rows under this strain taxon.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, type-material, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- Parent-species type-material, native GOLD, and StrainInfo evidence is represented on `data/taxa/eukaryota/aspergillus_sclerotioniger.yaml`; this generated strain record only gathers rows filed directly under `NCBITaxon:1450535`.
