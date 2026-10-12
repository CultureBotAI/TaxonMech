# YAML Record Review: Acetobacter sp. DmW_043

- Repository: TaxonMech
- Record: data/taxa/bacteria/acetobacter_sp_dmw_043.yaml
- Started UTC: 2026-09-26T10:01:16Z
- Finished UTC: 2026-09-26T10:01:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | data/taxa/bacteria/acetobacter_sp_dmw_043.yaml |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1670658 |
| Label | Acetobacter sp. DmW_043 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2628570 |
| Generated | Yes - seeded from committed inventories |
| PATHS.tsv | NCBITaxon:1670658 -> acetobacter_sp_dmw_043 on line 241040 |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacter_sp_dmw_043.yaml` | Pass; linkml-validate reported no issues |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_dmelcs_144.yaml data/taxa/bacteria/acetobacter_sp_dmelcs_145.yaml data/taxa/bacteria/acetobacter_sp_dmw_043.yaml data/taxa/bacteria/acetobacter_sp_dmw_125.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |

## Identity and Grounding

| Claim | Evidence |
|---|---|
| The record denotes `NCBITaxon:1670658` with label `Acetobacter sp. DmW_043`. | `data/raw/ncbitaxon_taxa.tsv` line 435318 has `NCBITaxon:1670658`, label `Acetobacter sp. DmW_043`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`. |
| The record is in scope. | `curation/seed_scope.tsv` line 75017 contains `NCBITaxon:1670658` with the reason `attested rule: Acetobacter sp. DmW_043, 2 sources incl. NCBI`. |
| The lineage is consistent with the pinned NCBI rows. | Bounded raw-source scan checked all 10 YAML lineage entries against `data/raw/ncbitaxon_taxa.tsv` and found no missing rows or label/rank mismatches. |

## Evidence

- The NCBI Taxonomy `source_attestations` entry is supported by the exact `data/raw/ncbitaxon_taxa.tsv` target row.
- `data/raw/gtdb_mappings.tsv` line 47593 maps `GTDB:s__Acetobacter_thailandicus` to `NCBITaxon:1670658` with `skos:closeMatch` and 8 genomes, matching the YAML `taxonomy_mappings` entry.
- `data/raw/gtdb_species.tsv` line 3342 has `GTDB:s__Acetobacter_thailandicus`, label `s__Acetobacter_thailandicus`, parent `GTDB:g__Acetobacter`, and 8 genomes, supporting the GTDB exact synonym, xref, and GENOME attestation.
- The GTDB species also maps to other NCBI taxa, so the seeded `skos:closeMatch` is appropriately weaker than an exact match or equivalence assertion.
- `data/raw/ncbi_merged_ids.tsv` has no rows merged into `NCBITaxon:1670658`; no retained retired IDs are expected.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:1670658`; no type-material entry is expected.

## Completeness

- The exact-source scan found the expected GTDB mapping and found no target rows in `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.
- The exact BacDive JSON scan found no records with NCBI taxon `1670658`.
- Native GOLD projection rows mention this taxon through organism `Go0475615`, project `Gp0359260`, and one analysis row with `AP_PROJECT_GOLD_IDS` set to `Gp0359260`, but no GOLD evidence joined to a curated strain row.
- The exact StrainInfo JSON and TSV scans found no direct strain, deposit, assembly, exclusion, or related-record rows for NCBI taxon `1670658`.
- The bounded raw strain scans found no exact target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this pass verdict.

## Additional Notes

- This was a read-only review. The generated YAML was not edited.
- Native GOLD rows are retained in the complete projection, while YAML `strains[].related_records` is seeded from joined strain/deposit evidence in `strain_related_records.tsv`; the absence of a GOLD related record here is consistent with the empty strain join.
- The bounded searches included ignored report files for duplicate-report preflight via `find reports/yaml_record_review` and exact source scans over the committed raw/source inventory surfaces listed above.
