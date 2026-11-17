# YAML Record Review: Nohea delmarensis

## Target

- Record: `data/taxa/eukaryota/nohea_delmarensis.yaml`
- Identifier: `NCBITaxon:1001692`
- Slug: `nohea_delmarensis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:45821` (`Nohea`)

## Validation

- `just validate data/taxa/eukaryota/nohea_delmarensis.yaml`: passed.
- `just validate-strict data/taxa/bacteria/aeromonas_sp_fars89d3a.yaml data/taxa/bacteria/aeromonas_sp_fars89d3b.yaml data/taxa/bacteria/aeromonas_sp_fars89d4.yaml data/taxa/eukaryota/nohea_delmarensis.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001692` / `Nohea delmarensis`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for an in-scope, direct NCBI seed record with corroborating GOLD evidence.
- `parent_taxon: NCBITaxon:45821` matches the pinned NCBI parent, `Nohea`.
- The lineage stays within Eukaryota through `Opisthokonta`, Fungi, `Ascomycota`, `Sordariomycetes`, `Microascales`, `Halosphaeriaceae`, and `Nohea`.

## Evidence

The two `source_attestations` entries are internally consistent:

- `source: NCBITAXON`; `source_id: NCBITaxon:1001692`; `source_label: Nohea delmarensis`; `assertion_count: 1`; `assertion_unit: NAME`
- `source: GOLD`; `source_id: NCBITaxon:1001692`; `source_label: Nohea delmarensis`; `assertion_count: 1`; `assertion_unit: ORGANISM`

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001692` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, and `data/raw/gold_organisms.tsv` rows, and no extra ATB, BacDive, GTDB, MADIN, or strain-info rows keyed to the reviewed identifier. The NCBI raw row's `attested_by` value also includes `gold`, matching the separate GOLD organism-count source footprint.

## Completeness

The record carries the exact NCBI synonym `Naufragella delmarensis` plus two related authority-bearing NCBI synonyms:

- `Naufragella delmarensis Kohlm. & Volkm.-Kohlm., 1998`
- `Nohea delmarensis (Kohlm. & Volkm.-Kohlm.) Abdel-Wahab, 2011`

It has no `strains`, `equivalent_identifiers`, `comments`, `xrefs`, or product-level sections. That is consistent with the NCBI plus GOLD source footprint and `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None urgent. Re-check only if a future source refresh adds ATB, BacDive, GTDB, MADIN, or strain-info rows for `NCBITaxon:1001692`.

## Additional Notes

- The NCBI and GOLD evidence come from pinned local `data/raw/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `nohea_delmarensis` review.
