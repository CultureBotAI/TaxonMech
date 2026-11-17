# YAML Record Review: Cadophora sp. MPI-SDFR-AT-0126

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cadophora_sp_mpi_sdfr_at_0126.yaml
- Started UTC: 2026-09-22T03:31:29Z
- Finished UTC: 2026-09-22T03:31:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2138324 |
| label | Cadophora sp. MPI-SDFR-AT-0126 |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2637819 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cadophora_sp_mpi_sdfr_at_0126.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*cadophora_sp_mpi_sdfr_at_0126.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cadophora_sp_mpi_sdfr_at_0126.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cadophora_sp_mpi_sdfr_at_0126.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 519050 has `NCBITaxon:2138324`, label `Cadophora sp. MPI-SDFR-AT-0126`, rank `SPECIES`, direct parent `NCBITaxon:2637819`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 62379 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `unclassified Cadophora` under genus `Cadophora`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:2138324`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and empty synonyms | `data/raw/ncbitaxon_taxa.tsv` line 519050 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62379 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 20333 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2138324`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0136936` for `Leotiomycetes sp. MPI-SDFR-AT-0126` at line 77615. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by projects `Gp0141916` and `Gp0197109` for `Go0136936`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by one analysis row joined through project `Gp0141916`. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:2138324`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material row mentions `NCBITaxon:2138324`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2138324`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:2138324`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2138324`. |

The committed aggregate GOLD row is mirrored by an exact native GOLD organism, two native project rows, and one analysis row joined through project `Gp0141916`.

The native GOLD rows use the broader organism name `Leotiomycetes sp. MPI-SDFR-AT-0126`, but they carry exact NCBI taxon ID `2138324`, so they support the taxon-level GOLD attestation.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `unclassified Cadophora` parent, and no synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, two project rows, and one joined analysis row.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- NCBI type-material, NCBI merged-ID, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- Exact local native GOLD scans recovered one organism row, two project rows, and one analysis row for `NCBITaxon:2138324`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Cadophora sp. MPI-SDFR-AT-0126` as `SPECIES`, and the generated record follows the source rank exactly.
