# YAML Record Review: Aspergillus transmontanensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_transmontanensis.yaml
- Started UTC: 2026-09-21T21:59:48Z
- Finished UTC: 2026-09-21T22:00:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1034304 |
| label | Aspergillus transmontanensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_transmontanensis.yaml`. It carries nine related NCBI synonyms, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_transmontanensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_transmontanensis.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_transmontanensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 221572 has `NCBITaxon:1034304`, label `Aspergillus transmontanensis`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, nine related synonyms, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 57251 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` redirects old IDs `NCBITaxon:1017321`, `NCBITaxon:1051590`, `NCBITaxon:1051592`, `NCBITaxon:1051593`, `NCBITaxon:1051594`, `NCBITaxon:1051595`, `NCBITaxon:1051596`, and `NCBITaxon:2606529` into `NCBITaxon:1034304`. `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 221572 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 57251 | Supported exactly: `attested rule: Aspergillus transmontanensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 466 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1034304`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with seven rows: four culture-from-holotype spellings for CBS 130015, plus holotype rows for 09AAsp260 and MUM 10.214 variants. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, three sequencing projects, and no matching native GOLD analysis row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1034304`. |
| Empty native and generated StrainInfo surfaces | Exact scans of native and generated StrainInfo snapshots | Supported; no native or generated StrainInfo row mentions `NCBITaxon:1034304`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1034304`. |

The native GOLD snapshot has one exact organism row on line 59845 for `Aspergillus transmontanensis CBS 130015` under NCBI taxon `1034304`, strain `CBS 130015`, and GOLD organism `Go0108199`. That organism joins to sequencing projects `Gp0108199`, `Gp0108200`, and `Gp0248669` on lines 61573, 61574, and 164115; the bounded native GOLD analysis scan found no analysis row linked to that organism or project.

Native StrainInfo has no direct strain rows or deposit-taxonomy hits under taxon `1034304`, and the generated StrainInfo overlay files contain no rows for `NCBITaxon:1034304`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Circumdati` parent, and the nine related synonyms.
- NCBI has seven type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, three linked sequencing projects, and no linked genome analysis.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aspergillus transmontanensis` as `SPECIES`, and the generated record follows the source rank exactly.
