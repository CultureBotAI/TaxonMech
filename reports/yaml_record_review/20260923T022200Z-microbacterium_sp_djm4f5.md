# YAML Record Review: Microbacterium sp. DJM4F5

- Repository: TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_djm4f5.yaml`
- Started UTC: 2026-09-23T02:22:00Z
- Finished UTC: 2026-09-23T02:22:00Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005800`
- Label: `Microbacterium sp. DJM4F5`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2609290` (`unclassified Microbacterium`)

## Validation

- `just validate-strict data/taxa/bacteria/methylobacterium_sp_djm4a7.yaml data/taxa/bacteria/microbacterium_sp_djm4b11.yaml data/taxa/bacteria/microbacterium_sp_djm4e6.yaml data/taxa/bacteria/microbacterium_sp_djm4f5.yaml` passed with 4 files scanned and 0 errors.
- `just validate data/taxa/bacteria/microbacterium_sp_djm4f5.yaml` passed.
- No prior report for `microbacterium_sp_djm4f5` was present under `reports/yaml_record_review/`; this was checked with `find`, which includes ignored report files.

## Identity and Grounding

- The YAML identifier and label match `data/raw/ncbitaxon_taxa.tsv:210552`.
- The NCBI source row has rank `SPECIES`, parent `NCBITaxon:2609290`, genetic code `11`, no synonyms, and snapshot `2026-09-13`, matching the seeded record.
- The record is grounded exactly to `NCBITaxon:1005800` and carries `mapping_status: SEEDED`, which is appropriate for a sparse one-source NCBI placeholder species.
- The lineage terminates at `NCBITaxon:2609290` (`unclassified Microbacterium`), the same value used by `parent_taxon`.

## Evidence

- `data/taxa/PATHS.tsv:1888` maps `NCBITaxon:1005800` to `microbacterium_sp_djm4f5`.
- `curation/seed_scope.tsv:311268` keeps `NCBITaxon:1005800` in scope as an attested NCBI-backed record with one source.
- `source_attestations` contains one `NCBITAXON` entry with `source_id: NCBITaxon:1005800`, `source_label: Microbacterium sp. DJM4F5`, and the expected NCBI snapshot note.
- Exact local source searches found no same-taxon rows for the full identifier, label, or slug in GTDB, strain assembly, strain genome, strain related, Madin, GOLD, ATB, or StrainInfo source files. The `rg --no-ignore --hidden` checks included ignored files.

## Completeness

- No nomenclature block is required because the pinned NCBI row has no synonym data.
- No taxonomy mapping is required because the local GTDB mapping table has no row for `NCBITaxon:1005800`.
- The `strain_count: 0` value is consistent with the absence of strain assembly or genome rows for this taxon.

## Findings

- No curation issues found.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- Live NCBI was not used; this review treats the checked-in NCBI, GTDB, ATB, StrainInfo, Madin, and GOLD source snapshots as the authoritative curation inputs.
