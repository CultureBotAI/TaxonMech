# YAML Record Review: Acetobacter sp. JU_27

- Repository: TaxonMech
- Record: data/taxa/bacteria/acetobacter_sp_ju_27.yaml
- Started UTC: 2026-09-26T10:31:04Z
- Finished UTC: 2026-09-26T10:31:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | data/taxa/bacteria/acetobacter_sp_ju_27.yaml |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1798925 |
| Label | Acetobacter sp. JU_27 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2628570 |
| Generated | Yes - seeded from committed inventories |
| PATHS.tsv | NCBITaxon:1798925 -> acetobacter_sp_ju_27 on line 275969 |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacter_sp_ju_27.yaml` | Pass; linkml-validate reported no issues |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_jdb71.yaml data/taxa/bacteria/acetobacter_sp_jg_2009.yaml data/taxa/bacteria/acetobacter_sp_ju_27.yaml data/taxa/bacteria/acetobacter_sp_jwb.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |

## Identity and Grounding

| Claim | Evidence |
|---|---|
| The record denotes `NCBITaxon:1798925` with label `Acetobacter sp. JU_27`. | `data/raw/ncbitaxon_taxa.tsv` line 469226 has `NCBITaxon:1798925`, label `Acetobacter sp. JU_27`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source set `ncbitaxon`, and taxonomy snapshot `2026-09-13`. |
| The record is in scope. | `curation/seed_scope.tsv` line 529780 contains `NCBITaxon:1798925` with the reason `attested rule: Acetobacter sp. JU_27, 1 sources incl. NCBI`. |
| The lineage is consistent with the pinned NCBI rows. | Bounded raw-source scan checked all 10 YAML lineage entries against `data/raw/ncbitaxon_taxa.tsv` and found no missing rows or label/rank mismatches. |

## Evidence

- The NCBI Taxonomy `source_attestations` entry is supported by the exact `data/raw/ncbitaxon_taxa.tsv` target row.
- Exact raw scans found no GTDB, LPSN, Madin, BactoTraits, or MediaDive rows for this identifier, matching the absence of `taxonomy_mappings`, `nomenclature`, synonyms, and xrefs.
- `data/raw/ncbi_merged_ids.tsv` has no rows merged into `NCBITaxon:1798925`; no retained retired IDs are expected.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:1798925`; no type-material entry is expected.

## Completeness

- The exact BacDive JSON scan found no records with NCBI taxon `1798925`.
- The native GOLD organism, project, and analysis scans found no rows for NCBI taxon `1798925`.
- The exact StrainInfo JSON and TSV scans found no direct strain, deposit, assembly, exclusion, or related-record rows for NCBI taxon `1798925`.
- The bounded raw strain scans found no exact target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
- A broader `rg --no-ignore --hidden` exact-CURIE search across `data/atb`, `data/straininfo`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, and `data/seqcode` found no text hits for this target; ignored paths were included.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this pass verdict.

## Additional Notes

- This was a read-only review. The generated YAML was not edited.
- Duplicate-report preflight used `find reports/yaml_record_review`, which included ignored report files; exact source scans covered the committed raw/source inventory surfaces listed above.
