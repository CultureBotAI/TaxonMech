# YAML Record Review: Acetobacter sp. KSO5

- Repository: TaxonMech
- Record: data/taxa/bacteria/acetobacter_sp_kso5.yaml
- Started UTC: 2026-09-26T10:34:18Z
- Finished UTC: 2026-09-26T10:34:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | data/taxa/bacteria/acetobacter_sp_kso5.yaml |
| Class | TaxonRecord |
| Identifier | NCBITaxon:3373674 |
| Label | Acetobacter sp. KSO5 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2628570 |
| Generated | Yes - seeded from committed inventories |
| PATHS.tsv | NCBITaxon:3373674 -> acetobacter_sp_kso5 on line 448883 |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacter_sp_kso5.yaml` | Pass; linkml-validate reported no issues |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_kso5.yaml data/taxa/bacteria/acetobacter_sp_lmg_1506.yaml data/taxa/bacteria/acetobacter_sp_lmg_1507.yaml data/taxa/bacteria/acetobacter_sp_lmg_1543.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |

## Identity and Grounding

| Claim | Evidence |
|---|---|
| The record denotes `NCBITaxon:3373674` with label `Acetobacter sp. KSO5`. | `data/raw/ncbitaxon_taxa.tsv` line 621881 has `NCBITaxon:3373674`, label `Acetobacter sp. KSO5`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`. |
| The record is in scope. | `curation/seed_scope.tsv` line 130652 contains `NCBITaxon:3373674` with the reason `attested rule: Acetobacter sp. KSO5, 2 sources incl. NCBI`. |
| The lineage is consistent with the pinned NCBI rows. | Bounded raw-source scan checked all 10 YAML lineage entries against `data/raw/ncbitaxon_taxa.tsv` and found no missing rows or label/rank mismatches. |

## Evidence

- The NCBI Taxonomy `source_attestations` entry is supported by the exact `data/raw/ncbitaxon_taxa.tsv` target row.
- `data/raw/gtdb_mappings.tsv` line 275067 maps `GTDB:s__Acetobacter_cerevisiae` to `NCBITaxon:3373674` with `skos:closeMatch` and 10 genomes, matching the YAML `taxonomy_mappings` entry.
- `data/raw/gtdb_species.tsv` line 3291 has `GTDB:s__Acetobacter_cerevisiae`, label `s__Acetobacter_cerevisiae`, parent `GTDB:g__Acetobacter`, and 10 genomes, supporting the GTDB exact synonym, xref, and GENOME attestation.
- The GTDB species also maps to other NCBI taxa, so the seeded `skos:closeMatch` is appropriately weaker than an exact match or equivalence assertion.
- `data/raw/ncbi_merged_ids.tsv` has no rows merged into `NCBITaxon:3373674`; no retained retired IDs are expected.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:3373674`; no type-material entry is expected.

## Completeness

- The exact-source scan found the expected GTDB mapping and found no target rows in `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.
- The exact BacDive JSON scan found no records with NCBI taxon `3373674`.
- The native GOLD organism, project, and analysis scans found no rows for NCBI taxon `3373674`.
- The exact StrainInfo JSON and TSV scans found no direct strain, deposit, assembly, exclusion, or related-record rows for NCBI taxon `3373674`.
- The bounded raw strain scans found no exact target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this pass verdict.

## Additional Notes

- This was a read-only review. The generated YAML was not edited.
- Duplicate-report preflight used `find reports/yaml_record_review`, which included ignored report files; exact source scans covered the committed raw/source inventory surfaces listed above.
