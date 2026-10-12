# YAML Record Review: Acetobacter sp. DmelCS_115

- Repository: TaxonMech
- Record: data/taxa/bacteria/acetobacter_sp_dmelcs_115.yaml
- Started UTC: 2026-09-26T09:38:58Z
- Finished UTC: 2026-09-26T09:38:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | data/taxa/bacteria/acetobacter_sp_dmelcs_115.yaml |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1283147 |
| Label | Acetobacter sp. DmelCS_115 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2628570 |
| Generated | Yes - seeded from committed inventories |
| PATHS.tsv | NCBITaxon:1283147 -> acetobacter_sp_dmelcs_115 on line 97762 |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacter_sp_dmelcs_115.yaml` | Pass; linkml-validate reported no issues |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_dmelcs_114.yaml data/taxa/bacteria/acetobacter_sp_dmelcs_115.yaml data/taxa/bacteria/acetobacter_sp_dmelcs_116.yaml data/taxa/bacteria/acetobacter_sp_dmelcs_117.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |

## Identity and Grounding

| Claim | Evidence |
|---|---|
| The record denotes `NCBITaxon:1283147` with label `Acetobacter sp. DmelCS_115`. | `data/raw/ncbitaxon_taxa.tsv` line 300057 has `NCBITaxon:1283147`, label `Acetobacter sp. DmelCS_115`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source set `ncbitaxon`, and taxonomy snapshot `2026-09-13`. |
| The record is in scope. | `curation/seed_scope.tsv` line 386471 contains `NCBITaxon:1283147` with the reason `attested rule: Acetobacter sp. DmelCS_115, 1 sources incl. NCBI`. |
| The lineage is consistent with the pinned NCBI rows. | Bounded raw-source scan checked all 10 YAML lineage entries against `data/raw/ncbitaxon_taxa.tsv` and found no missing rows or label/rank mismatches. |

## Evidence

- The sole `source_attestations` entry is for NCBI Taxonomy and is supported by the exact `data/raw/ncbitaxon_taxa.tsv` target row.
- The record has no synonyms, nomenclature, taxonomy mappings, strain records, genome assemblies, genome records, related records, or causal graphs that would need additional narrow evidence.
- `data/raw/ncbi_merged_ids.tsv` has no rows merged into `NCBITaxon:1283147`; no retained retired IDs are expected.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:1283147`; no type-material entry is expected.

## Completeness

- The empty optional sections match the exact-source scan: no target rows were found in `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.
- The exact BacDive JSON scan found no records with NCBI taxon `1283147`.
- The exact GOLD scan found no organism, project, or analysis rows for NCBI taxon `1283147`.
- The exact StrainInfo JSON and TSV scans found no direct strain, deposit, assembly, exclusion, or related-record rows for NCBI taxon `1283147`.
- The bounded raw strain scans found no exact target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this pass verdict.

## Additional Notes

- This was a read-only review. The generated YAML was not edited.
- The bounded searches included ignored report files for duplicate-report preflight via `find reports/yaml_record_review` and exact source scans over the committed raw/source inventory surfaces listed above.
