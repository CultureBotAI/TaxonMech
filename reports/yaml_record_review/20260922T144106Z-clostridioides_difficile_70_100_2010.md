# YAML Record Review: Clostridioides difficile 70-100-2010

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/clostridioides_difficile_70_100_2010.yaml`
- Started UTC: 2026-09-22T14:39:40Z
- Finished UTC: 2026-09-22T14:41:06Z
- Verdict: needs curation

## Target

- Record: `data/taxa/bacteria/clostridioides_difficile_70_100_2010.yaml`
- Identifier: `NCBITaxon:1002369`
- Slug: `clostridioides_difficile_70_100_2010`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1496` (`Clostridioides difficile`)

## Validation

- `just validate data/taxa/bacteria/clostridioides_difficile_70_100_2010.yaml`: passed.
- `just validate-strict data/taxa/bacteria/listeria_innocua_atcc_33091.yaml data/taxa/bacteria/leyella_stercorea_dsm_18206.yaml data/taxa/bacteria/yokenella_regensburgei_atcc_43003.yaml data/taxa/bacteria/clostridioides_difficile_70_100_2010.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The NCBI strain identity is exact for `NCBITaxon:1002369` / `Clostridioides difficile 70-100-2010`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:1496` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillota`, `Clostridia`, `Peptostreptococcales`, `Peptostreptococcaceae`, `Clostridioides`, then `Clostridioides difficile`.
- The four NCBI exact synonyms for prior `Clostridium` and `Peptoclostridium` naming are represented.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.
- The GTDB-derived close match and exact synonym need curation review because `GTDB:s__Clostridioides_difficile`, a 3719-genome species cluster that also maps to the parent species `NCBITaxon:1496`, is grafted directly onto one 70-100-2010 strain.

## Evidence

The local exact-ID search found the NCBI row, one GTDB `skos:closeMatch` row, and one MADIN trait assertion keyed directly to `NCBITaxon:1002369`. The reviewed YAML carries those same source attestations plus the GTDB taxonomy mapping, GTDB xref, GTDB-derived exact synonym, and NCBI exact synonyms.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found no ATB, BacDive, GOLD, LPSN, MediaDive, BactoTraits, or strain-info rows keyed to this identifier. An exact GTDB ID search found `GTDB:s__Clostridioides_difficile` mapped to many NCBI taxa, including the parent species `NCBITaxon:1496`.

## Completeness

The record represents all direct local source rows keyed to `NCBITaxon:1002369`. It has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence.

## Findings

- Major: a species-scale GTDB mapping is attached directly to the `Clostridioides difficile 70-100-2010` strain seed. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Clostridioides_difficile` to `NCBITaxon:1002369` with `skos:closeMatch` and `genome_count: 3719`, and the generator turns that row into a taxonomy mapping, a GTDB xref, and an `EXACT_SYNONYM` of `Clostridioides difficile`. Owner: the GTDB mapping import behind `data/raw/gtdb_mappings.tsv` and the generated `data/taxa` emission of GTDB close-match synonyms.

## Recommended Edits

- Review whether the `GTDB:s__Clostridioides_difficile` close match and its derived `Clostridioides difficile` exact synonym should remain on this strain record, be represented only as a broader species-cluster relationship, or be moved to the `Clostridioides difficile` species record or another aggregate that does not make one clinical strain denote the whole 3719-genome GTDB species.

## Follow-up Checks

- After curation, rerun `just validate data/taxa/bacteria/clostridioides_difficile_70_100_2010.yaml` and `just validate-strict data/taxa/bacteria/clostridioides_difficile_70_100_2010.yaml`.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `clostridioides_difficile_70_100_2010` review.
