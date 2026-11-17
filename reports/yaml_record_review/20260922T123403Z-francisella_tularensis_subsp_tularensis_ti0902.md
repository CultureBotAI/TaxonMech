# YAML Record Review: Francisella tularensis subsp. tularensis TI0902

## Target

- Record: `data/taxa/bacteria/francisella_tularensis_subsp_tularensis_ti0902.yaml`
- Identifier: `NCBITaxon:1001534`
- Slug: `francisella_tularensis_subsp_tularensis_ti0902`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:119856` (`Francisella tularensis subsp. tularensis`)

## Validation

- `just validate data/taxa/bacteria/francisella_tularensis_subsp_tularensis_ti0902.yaml`: passed.
- `just validate-strict data/taxa/bacteria/photobacterium_leiognathi_subsp_mandapamensis_svers_1_1.yaml data/taxa/bacteria/actinomycete_a2_2011.yaml data/taxa/bacteria/bacterium_b5_2011.yaml data/taxa/bacteria/francisella_tularensis_subsp_tularensis_ti0902.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001534` / `Francisella tularensis subsp. tularensis TI0902`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, rank `STRAIN`, parent `NCBITaxon:119856`, and genetic code `11` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.
- The NCBI lineage places this strain under `Francisella tularensis`, then `Francisella tularensis subsp. tularensis`.

## Evidence

Four source attestations are backed by local source rows keyed to `NCBITaxon:1001534`:

- `NCBITAXON`: 1 name assertion.
- `GTDB`: `GTDB:s__Francisella_tularensis`, `skos:closeMatch`, 937 genomes.
- `GOLD`: 1 organism assertion, direct records only.
- `MADIN`: 5 trait assertions, direct records only.

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001534` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, and `madin_taxa.tsv` rows, plus a child NCBI row that lists `NCBITaxon:1001534` as parent. It found no ATB, BacDive, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record includes the expected NCBI synonyms, GTDB cross-reference, `taxonomy_mappings` entry, and four source attestations. The direct-only GOLD and MADIN notes are appropriate because child NCBI taxa, including `NCBITaxon:1001542`, are not rolled up into this strain record.

## Findings

- Major: the GTDB mapping is species-level but is emitted onto a strain-level NCBI record. `GTDB:s__Francisella_tularensis` and synonym text `Francisella tularensis` both describe the species, while `NCBITaxon:1001534` is a single `Francisella tularensis subsp. tularensis` strain. Treating `Francisella tularensis` as an `EXACT_SYNONYM` of the strain overstates equivalence, and the 937-genome GTDB assertion reads as evidence for the strain rather than for the species cluster.

## Recommended Edits

- Route the `GTDB:s__Francisella_tularensis` mapping and 937-genome count to the species-level target, `NCBITaxon:263`, or suppress/downgrade the GTDB mapping and synonym when a GTDB species maps to a lower-rank NCBI strain.
- Add a regression check that rejects `EXACT_SYNONYM` emission when the synonym is generated from a GTDB species mapping onto an NCBI `STRAIN`.

## Follow-up Checks

- After the GTDB rank-mismatch handling is changed, re-run seeding and confirm this strain no longer carries a species-level `GTDB:s__Francisella_tularensis` exact synonym or 937-genome species assertion.

## Additional Notes

- The NCBI, GTDB, GOLD, and MADIN evidence was reviewed from pinned local `data/raw/` snapshots rather than live provider lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `francisella_tularensis_subsp_tularensis_ti0902` review.
