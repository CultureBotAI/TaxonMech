# YAML Record Review: Aspergillus ruber CBS 135680

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_ruber_cbs_135680.yaml
- Started UTC: 2026-09-21T20:35:51Z
- Finished UTC: 2026-09-21T20:37:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1388766 |
| label | Aspergillus ruber CBS 135680 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:396024 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic strain at `data/taxa/eukaryota/aspergillus_ruber_cbs_135680.yaml`. It carries two NCBI exact synonyms, no NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_ruber_cbs_135680.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_ruber_cbs_135680.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_ruber_cbs_135680.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 340520 has `NCBITaxon:1388766`, label `Aspergillus ruber CBS 135680`, rank `STRAIN`, direct parent `NCBITaxon:396024`, genetic code `1`, two exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 59821 keeps this strain in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the terminal parent species `Aspergillus ruber`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:1388766`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this strain; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 340520 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 59821 | Supported exactly: `attested rule: Aspergillus ruber CBS 135680, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 9198 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1388766`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows are filed under the strain-level `NCBITaxon:1388766`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; no exact local native GOLD organism, project, or genome-analysis rows were filed under strain taxon `1388766`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1388766`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1388766`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1388766`. |

The local native GOLD JSONL snapshot files represent `CBS 135680` under the parent species taxon `NCBITaxon:396024`, while this strain record is grounded by the exact NCBI strain taxon `NCBITaxon:1388766` and the aggregate GOLD row for that strain taxon.

Native BacDive and StrainInfo have no exact entries under taxon `1388766`, and the generated StrainInfo overlay files contain no rows for `NCBITaxon:1388766`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies strain identity, lineage, genetic code, and two exact strain-name synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one for this exact strain taxon.
- Exact local native GOLD scans under `1388766` are empty because the committed native rows file `CBS 135680` under the parent species taxon.
- BacDive and StrainInfo do not supply exact strain records under this strain-level taxon ID.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
