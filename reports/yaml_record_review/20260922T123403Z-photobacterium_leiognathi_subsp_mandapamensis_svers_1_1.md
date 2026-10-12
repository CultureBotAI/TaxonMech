# YAML Record Review: Photobacterium leiognathi subsp. mandapamensis svers.1.1.

## Target

- Record: `data/taxa/bacteria/photobacterium_leiognathi_subsp_mandapamensis_svers_1_1.yaml`
- Identifier: `NCBITaxon:1001530`
- Slug: `photobacterium_leiognathi_subsp_mandapamensis_svers_1_1`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:48408` (`Photobacterium leiognathi subsp. mandapamensis`)

## Validation

- `just validate data/taxa/bacteria/photobacterium_leiognathi_subsp_mandapamensis_svers_1_1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/photobacterium_leiognathi_subsp_mandapamensis_svers_1_1.yaml data/taxa/bacteria/actinomycete_a2_2011.yaml data/taxa/bacteria/bacterium_b5_2011.yaml data/taxa/bacteria/francisella_tularensis_subsp_tularensis_ti0902.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001530` / `Photobacterium leiognathi subsp. mandapamensis svers.1.1.`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, rank `STRAIN`, parent `NCBITaxon:48408`, and genetic code `11` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.
- The NCBI lineage places this strain under `Photobacterium leiognathi`, then `Photobacterium leiognathi subsp. mandapamensis`.

## Evidence

Four source attestations are backed by local source rows keyed to `NCBITaxon:1001530`:

- `NCBITAXON`: 1 name assertion.
- `GTDB`: `GTDB:s__Photobacterium_leiognathi`, `skos:closeMatch`, 121 genomes.
- `GOLD`: 1 organism assertion.
- `MADIN`: 1 trait assertion.

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001530` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, and `madin_taxa.tsv` rows, and no ATB, BacDive, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record includes the expected NCBI synonyms, GTDB cross-reference, `taxonomy_mappings` entry, and four source attestations. `strain_count: 0` is consistent with this record itself being a terminal strain-level NCBI concept in the reviewed local inputs.

## Findings

- Major: the GTDB mapping is species-level but is emitted onto a strain-level NCBI record. `GTDB:s__Photobacterium_leiognathi` and synonym text `Photobacterium leiognathi` both describe the species, while `NCBITaxon:1001530` is a single `Photobacterium leiognathi subsp. mandapamensis` strain. Treating `Photobacterium leiognathi` as an `EXACT_SYNONYM` of the strain overstates equivalence, and the 121-genome GTDB assertion reads as evidence for the strain rather than for the species cluster.

## Recommended Edits

- Route the `GTDB:s__Photobacterium_leiognathi` mapping and 121-genome count to the species-level target, `NCBITaxon:553611`, or suppress/downgrade the GTDB mapping and synonym when a GTDB species maps to a lower-rank NCBI strain.
- Add a regression check that rejects `EXACT_SYNONYM` emission when the synonym is generated from a GTDB species mapping onto an NCBI `STRAIN`.

## Follow-up Checks

- After the GTDB rank-mismatch handling is changed, re-run seeding and confirm this strain no longer carries a species-level `GTDB:s__Photobacterium_leiognathi` exact synonym or 121-genome species assertion.

## Additional Notes

- The NCBI, GTDB, GOLD, and MADIN evidence was reviewed from pinned local `data/raw/` snapshots rather than live provider lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `photobacterium_leiognathi_subsp_mandapamensis_svers_1_1` review.
