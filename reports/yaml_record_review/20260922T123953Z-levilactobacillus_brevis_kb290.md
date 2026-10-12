# YAML Record Review: Levilactobacillus brevis KB290

## Target

- Record: `data/taxa/bacteria/levilactobacillus_brevis_kb290.yaml`
- Identifier: `NCBITaxon:1001583`
- Slug: `levilactobacillus_brevis_kb290`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1580` (`Levilactobacillus brevis`)

## Validation

- `just validate data/taxa/bacteria/levilactobacillus_brevis_kb290.yaml`: passed.
- `just validate-strict data/taxa/bacteria/acinetobacter_sp_va2s2.yaml data/taxa/bacteria/sphingomonas_sp_a_5.yaml data/taxa/bacteria/bacillus_amyloliquefaciens_ll3.yaml data/taxa/bacteria/levilactobacillus_brevis_kb290.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001583` / `Levilactobacillus brevis KB290`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, rank `STRAIN`, parent `NCBITaxon:1580`, and genetic code `11` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.
- The NCBI lineage places this strain under `Levilactobacillus brevis`.

## Evidence

Two source attestations are backed by local source rows keyed to `NCBITaxon:1001583`:

- `NCBITAXON`: 1 name assertion.
- `GTDB`: `GTDB:s__Levilactobacillus_brevis`, `skos:closeMatch`, 231 genomes.

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001583` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, and `gtdb_mappings.tsv` rows, and no ATB, BacDive, GOLD, MADIN, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record includes the expected NCBI synonyms, GTDB cross-reference, `taxonomy_mappings` entry, and two source attestations. `strain_count: 0` is consistent with the absence of child strain rows in the reviewed local source footprint.

## Findings

- Major: the GTDB mapping is species-level but is emitted onto a strain-level NCBI record. `GTDB:s__Levilactobacillus_brevis` and synonym text `Levilactobacillus brevis` both describe the species, while `NCBITaxon:1001583` is the `Levilactobacillus brevis KB290` strain. Treating `Levilactobacillus brevis` as an `EXACT_SYNONYM` of the strain overstates equivalence, and the 231-genome GTDB assertion reads as evidence for the strain rather than for the species cluster.

## Recommended Edits

- Route the `GTDB:s__Levilactobacillus_brevis` mapping and 231-genome count to the species-level target, `NCBITaxon:1580`, or suppress/downgrade the GTDB mapping and synonym when a GTDB species maps to a lower-rank NCBI strain.
- Add a regression check that rejects `EXACT_SYNONYM` emission when the synonym is generated from a GTDB species mapping onto an NCBI `STRAIN`.

## Follow-up Checks

- After the GTDB rank-mismatch handling is changed, re-run seeding and confirm this strain no longer carries a species-level `GTDB:s__Levilactobacillus_brevis` exact synonym or 231-genome species assertion.

## Additional Notes

- The NCBI and GTDB evidence was reviewed from pinned local `data/raw/` snapshots rather than live provider lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `levilactobacillus_brevis_kb290` review.
