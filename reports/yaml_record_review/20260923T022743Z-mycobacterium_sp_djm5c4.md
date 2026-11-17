# YAML Record Review: Mycobacterium sp. DJM5C4

- Repository: TaxonMech
- Record: `data/taxa/bacteria/mycobacterium_sp_djm5c4.yaml`
- Started UTC: 2026-09-23T02:27:43Z
- Finished UTC: 2026-09-23T02:27:43Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005805`
- Label: `Mycobacterium sp. DJM5C4`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2642494` (`unclassified Mycobacterium`)

## Validation

- `just validate-strict data/taxa/bacteria/mycobacterium_sp_djm5c4.yaml data/taxa/bacteria/paenibacillus_sp_djm4a6.yaml data/taxa/bacteria/paenibacillus_sp_djm4b1.yaml data/taxa/bacteria/paenibacillus_sp_djm4b10.yaml` passed with 4 files scanned and 0 errors.
- `just validate data/taxa/bacteria/mycobacterium_sp_djm5c4.yaml` passed.
- No prior report for `mycobacterium_sp_djm5c4` was present under `reports/yaml_record_review/`; this was checked with `find`, which includes ignored report files.

## Identity and Grounding

- The YAML identifier and label match `data/raw/ncbitaxon_taxa.tsv:210557`.
- The NCBI source row has rank `SPECIES`, parent `NCBITaxon:2642494`, genetic code `11`, no synonyms, and snapshot `2026-09-13`, matching the seeded record.
- The record is grounded exactly to `NCBITaxon:1005805` and carries `mapping_status: SEEDED`, which is appropriate for a sparse one-source NCBI placeholder species.
- The lineage terminates at `NCBITaxon:2642494` (`unclassified Mycobacterium`), the same value used by `parent_taxon`.

## Evidence

- `data/taxa/PATHS.tsv:1893` maps `NCBITaxon:1005805` to `mycobacterium_sp_djm5c4`.
- `curation/seed_scope.tsv:311273` keeps `NCBITaxon:1005805` in scope as an attested NCBI-backed record with one source.
- `source_attestations` contains one `NCBITAXON` entry with `source_id: NCBITaxon:1005805`, `source_label: Mycobacterium sp. DJM5C4`, and the expected NCBI snapshot note.
- Exact local source searches found no same-taxon rows for the full identifier, label, or slug in GTDB, strain assembly, strain genome, strain related, Madin, GOLD, ATB, or StrainInfo source files. The `rg --no-ignore --hidden` checks included ignored files.

## Completeness

- No nomenclature block is required because the pinned NCBI row has no synonym data.
- No taxonomy mapping is required because the local GTDB mapping table has no row for `NCBITaxon:1005805`.
- The `strain_count: 0` value is consistent with the absence of strain assembly or genome rows for this taxon.

## Findings

- No curation issues found.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- Live NCBI was not used; this review treats the checked-in NCBI, GTDB, ATB, StrainInfo, Madin, and GOLD source snapshots as the authoritative curation inputs.
