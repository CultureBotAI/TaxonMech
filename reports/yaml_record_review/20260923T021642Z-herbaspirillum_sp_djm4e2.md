# YAML Record Review: Herbaspirillum sp. DJM4E2

- Repository: TaxonMech
- Record: `data/taxa/bacteria/herbaspirillum_sp_djm4e2.yaml`
- Started UTC: 2026-09-23T02:16:42Z
- Finished UTC: 2026-09-23T02:16:42Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005790`
- Label: `Herbaspirillum sp. DJM4E2`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2624150` (`unclassified Herbaspirillum`)

## Validation

- `just validate-strict data/taxa/bacteria/enterobacter_sp_djm5b5.yaml data/taxa/bacteria/herbaspirillum_sp_djm4e2.yaml data/taxa/bacteria/janthinobacterium_sp_djm5a12.yaml data/taxa/bacteria/klebsiella_sp_djm4e1.yaml` passed with 4 files scanned and 0 errors.
- `just validate data/taxa/bacteria/herbaspirillum_sp_djm4e2.yaml` passed.
- No prior report for `herbaspirillum_sp_djm4e2` was present under `reports/yaml_record_review/`; this was checked with `find`, which includes ignored report files.

## Identity and Grounding

- The YAML identifier and label match `data/raw/ncbitaxon_taxa.tsv:210542`.
- The NCBI source row has rank `SPECIES`, genetic code `11`, no synonyms, and snapshot `2026-09-13`, matching the seeded record.
- The record is grounded exactly to `NCBITaxon:1005790` and carries `mapping_status: SEEDED`, which is appropriate for a sparse one-source NCBI placeholder species.
- The parent taxon is the terminal lineage parent, `NCBITaxon:2624150` (`unclassified Herbaspirillum`), so the lineage and `parent_taxon` agree.

## Evidence

- `curation/seed_scope.tsv:311258` keeps `NCBITaxon:1005790` in scope as an attested NCBI-backed record with one source.
- `source_attestations` contains one `NCBITAXON` entry with `source_id: NCBITaxon:1005790`, `source_label: Herbaspirillum sp. DJM4E2`, and the expected NCBI snapshot note.
- Exact local source searches found no same-taxon rows for the full identifier, label, or slug in ATB or StrainInfo. The `rg --no-ignore --hidden` check included ignored files.
- Earlier exact scans found no same-taxon GTDB, strain assembly, strain genome, strain related, Madin, or GOLD source rows, so there is no omitted local evidence to project into this record.

## Completeness

- No nomenclature block is required because the pinned NCBI row has no synonym data.
- No taxonomy mapping is required because the local GTDB mapping table has no row for `NCBITaxon:1005790`.
- The `strain_count: 0` value is consistent with the absence of strain assembly or genome rows for this taxon.

## Findings

- No curation issues found.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- Live NCBI was not used; this review treats the checked-in NCBI, GTDB, ATB, StrainInfo, Madin, and GOLD source snapshots as the authoritative curation inputs.
