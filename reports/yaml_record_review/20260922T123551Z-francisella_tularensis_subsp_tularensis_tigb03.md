# YAML Record Review: Francisella tularensis subsp. tularensis TIGB03

## Target

- Record: `data/taxa/bacteria/francisella_tularensis_subsp_tularensis_tigb03.yaml`
- Identifier: `NCBITaxon:1001542`
- Slug: `francisella_tularensis_subsp_tularensis_tigb03`
- Rank: `NO_RANK`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1001534` (`Francisella tularensis subsp. tularensis TI0902`)

## Validation

- `just validate data/taxa/bacteria/francisella_tularensis_subsp_tularensis_tigb03.yaml`: passed.
- `just validate-strict data/taxa/bacteria/francisella_tularensis_subsp_tularensis_tigb03.yaml data/taxa/bacteria/alcaligenes_sp_f1.yaml data/taxa/bacteria/pseudomonas_sp_cm1_a2.yaml data/taxa/bacteria/pseudomonas_sp_v6.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001542` / `Francisella tularensis subsp. tularensis TIGB03`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, rank `NO_RANK`, parent `NCBITaxon:1001534`, and genetic code `11` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.
- The NCBI lineage places this no-rank strain child under `Francisella tularensis`, `Francisella tularensis subsp. tularensis`, and `Francisella tularensis subsp. tularensis TI0902`.

## Evidence

Four source attestations are backed by local source rows keyed to `NCBITaxon:1001542`:

- `NCBITAXON`: 1 name assertion.
- `GTDB`: `GTDB:s__Francisella_tularensis`, `skos:closeMatch`, 937 genomes.
- `GOLD`: 1 organism assertion.
- `MADIN`: 1 trait assertion.

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001542` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, and `madin_taxa.tsv` rows, and no ATB, BacDive, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record includes the expected NCBI synonyms, GTDB cross-reference, `taxonomy_mappings` entry, and four source attestations. `strain_count: 0` is consistent with the absence of child strain rows in the reviewed local source footprint.

## Findings

- Major: the GTDB mapping is species-level but is emitted onto a no-rank NCBI child beneath a strain. `GTDB:s__Francisella_tularensis` and synonym text `Francisella tularensis` both describe the species, while `NCBITaxon:1001542` is a no-rank child of the `Francisella tularensis subsp. tularensis TI0902` strain. Treating `Francisella tularensis` as an `EXACT_SYNONYM` here overstates equivalence, and the 937-genome GTDB assertion reads as evidence for this one child record rather than for the species cluster.

## Recommended Edits

- Route the `GTDB:s__Francisella_tularensis` mapping and 937-genome count to the species-level target, `NCBITaxon:263`, or suppress/downgrade the GTDB mapping and synonym when a GTDB species maps to an NCBI `NO_RANK` node below strain rank.
- Add a regression check that rejects `EXACT_SYNONYM` emission when the synonym is generated from a GTDB species mapping onto an NCBI descendant below the species.

## Follow-up Checks

- After the GTDB rank-mismatch handling is changed, re-run seeding and confirm this no-rank strain child no longer carries a species-level `GTDB:s__Francisella_tularensis` exact synonym or 937-genome species assertion.

## Additional Notes

- The NCBI, GTDB, GOLD, and MADIN evidence was reviewed from pinned local `data/raw/` snapshots rather than live provider lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `francisella_tularensis_subsp_tularensis_tigb03` review.
