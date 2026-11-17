# YAML Record Review: Aspergillus terricola var. indicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_terricola_var_indicus.yaml
- Started UTC: 2026-09-21T21:53:10Z
- Finished UTC: 2026-09-21T21:53:49Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:138288 |
| label | Aspergillus terricola var. indicus |
| rank | VARIETAS |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:36642 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic variety at `data/taxa/eukaryota/aspergillus_terricola_var_indicus.yaml`. It carries one exact NCBI synonym, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_terricola_var_indicus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_terricola_var_indicus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_terricola_var_indicus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 27771 has `NCBITaxon:138288`, label `Aspergillus terricola var. indicus`, rank `VARIETAS`, direct parent `NCBITaxon:36642`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53989 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus terricola`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:138288`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this variety; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 27771 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53989 | Supported exactly: `attested rule: Aspergillus terricola var. indicus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 8994 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:138288`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with ten `Aspergillus indicus` type-material rows for ATCC 15054, CBS 167.63, IMI 172295, QM 8903, and WB 4680 variants. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, two sequencing projects, and no matching native GOLD analysis row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `138288`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has one direct record and five deposit-taxonomy hits under `138288`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:138288`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:138288`. |

The native GOLD snapshot has one exact organism row on line 59808 for `Aspergillus indicus CBS 952.97` under NCBI taxon `138288`, strain `CBS 952.97`, and GOLD organism `Go0108121`. That organism joins to sequencing projects `Gp0108121` and `Gp0108122` on lines 61500 and 61501; the bounded native GOLD analysis scan found no analysis row linked to that organism or project.

Native StrainInfo has one direct strain row and five deposit-taxonomy hits under taxon `138288`. That native StrainInfo hit does not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus terricola` species parent, one exact synonym, and two related synonyms.
- NCBI has ten type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, two linked sequencing projects, and no linked genome analysis.
- BacDive does not supply exact local strain evidence for this taxon, and the native StrainInfo exact hit has no BacDive-derived local strain to overlay.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aspergillus terricola var. indicus` as `VARIETAS`, and the generated record follows the source rank exactly.
