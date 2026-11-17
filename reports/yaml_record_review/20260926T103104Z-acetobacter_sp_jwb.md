# YAML Record Review: Acetobacter sp. JWB

- Repository: TaxonMech
- Record: data/taxa/bacteria/acetobacter_sp_jwb.yaml
- Started UTC: 2026-09-26T10:31:04Z
- Finished UTC: 2026-09-26T10:31:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | data/taxa/bacteria/acetobacter_sp_jwb.yaml |
| Class | TaxonRecord |
| Identifier | NCBITaxon:2259883 |
| Label | Acetobacter sp. JWB |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2628570 |
| Generated | Yes - seeded from committed inventories |
| PATHS.tsv | NCBITaxon:2259883 -> acetobacter_sp_jwb on line 335094 |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacter_sp_jwb.yaml` | Pass; linkml-validate reported no issues |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_jdb71.yaml data/taxa/bacteria/acetobacter_sp_jg_2009.yaml data/taxa/bacteria/acetobacter_sp_ju_27.yaml data/taxa/bacteria/acetobacter_sp_jwb.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |

## Identity and Grounding

| Claim | Evidence |
|---|---|
| The record denotes `NCBITaxon:2259883` with label `Acetobacter sp. JWB`. | `data/raw/ncbitaxon_taxa.tsv` line 522347 has `NCBITaxon:2259883`, label `Acetobacter sp. JWB`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`. |
| The record is in scope. | `curation/seed_scope.tsv` line 93345 contains `NCBITaxon:2259883` with the reason `attested rule: Acetobacter sp. JWB, 2 sources incl. NCBI`. |
| The lineage is consistent with the pinned NCBI rows. | Bounded raw-source scan checked all 10 YAML lineage entries against `data/raw/ncbitaxon_taxa.tsv` and found no missing rows or label/rank mismatches. |

## Evidence

- The NCBI Taxonomy `source_attestations` entry is supported by the exact `data/raw/ncbitaxon_taxa.tsv` target row.
- `data/raw/gtdb_mappings.tsv` line 178761 maps `GTDB:s__Acetobacter_oryzifermentans` to `NCBITaxon:2259883` with `skos:closeMatch` and 28 genomes, matching the YAML `taxonomy_mappings` entry.
- `data/raw/gtdb_species.tsv` line 3315 has `GTDB:s__Acetobacter_oryzifermentans`, label `s__Acetobacter_oryzifermentans`, parent `GTDB:g__Acetobacter`, and 28 genomes, supporting the GTDB exact synonym, xref, and GENOME attestation.
- The GTDB species also maps to other NCBI taxa, so the seeded `skos:closeMatch` is appropriately weaker than an exact match or equivalence assertion.
- `data/raw/ncbi_merged_ids.tsv` has no rows merged into `NCBITaxon:2259883`; no retained retired IDs are expected.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:2259883`; no type-material entry is expected.

## Completeness

- The exact-source scan found the expected GTDB mapping and found no target rows in `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.
- The exact BacDive JSON scan found no records with NCBI taxon `2259883`.
- Native GOLD projection rows mention this taxon through organism `Go0454255`, project `Gp0322561`, and one analysis row with `AP_PROJECT_GOLD_IDS` set to `Gp0322561`, but no GOLD evidence joined to a curated strain row.
- The exact StrainInfo JSON and TSV scans found no direct strain, deposit, assembly, exclusion, or related-record rows for NCBI taxon `2259883`.
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
- Duplicate-report preflight used `find reports/yaml_record_review`, which included ignored report files; exact source scans covered the committed raw/source inventory surfaces listed above.
