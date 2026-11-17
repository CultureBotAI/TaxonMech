# YAML Record Review: Listeria innocua ATCC 33091

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/listeria_innocua_atcc_33091.yaml`
- Started UTC: 2026-09-22T14:39:40Z
- Finished UTC: 2026-09-22T14:41:06Z
- Verdict: needs curation

## Target

- Record: `data/taxa/bacteria/listeria_innocua_atcc_33091.yaml`
- Identifier: `NCBITaxon:1002366`
- Slug: `listeria_innocua_atcc_33091`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1642` (`Listeria innocua`)

## Validation

- `just validate data/taxa/bacteria/listeria_innocua_atcc_33091.yaml`: passed.
- `just validate-strict data/taxa/bacteria/listeria_innocua_atcc_33091.yaml data/taxa/bacteria/leyella_stercorea_dsm_18206.yaml data/taxa/bacteria/yokenella_regensburgei_atcc_43003.yaml data/taxa/bacteria/clostridioides_difficile_70_100_2010.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The NCBI strain identity is exact for `NCBITaxon:1002366` / `Listeria innocua ATCC 33091`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:1642` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Bacillota`, `Bacilli`, `Caryophanales`, `Listeriaceae`, `Listeria`, then `Listeria innocua`.
- NCBI exact synonyms `Listeria innocua str. ATCC 33091` and `Listeria innocua strain ATCC 33091` are both represented.
- The BacDive strain subrecord represents `bacdive:136614` and its ATCC, CIP, and NCTC culture-collection deposits.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.
- The GTDB-derived close match and exact synonym need curation review because `GTDB:s__Listeria_innocua`, a 182-genome species cluster that also maps to the parent species `NCBITaxon:1642`, is grafted directly onto the ATCC 33091 strain.

## Evidence

The local same-record evidence includes the NCBI row, one GTDB `skos:closeMatch` row, one BacDive strain, and five MADIN trait assertions keyed directly to `NCBITaxon:1002366`. The exact BacDive-strain search for `kgmicrobe.strain:bacdive_136614` also found the expected assemblies, genome records, related BioProject/BioSample/GOLD records, and StrainInfo deposit rows used by the reviewed `strains` block.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found no ATB, GOLD aggregate, LPSN, MediaDive, or BactoTraits source-attestation rows keyed to `NCBITaxon:1002366`. An exact GTDB ID search found `GTDB:s__Listeria_innocua` mapped to multiple NCBI taxa, including the parent species `NCBITaxon:1642`.

## Completeness

The record represents the direct NCBI, BacDive, GTDB, MADIN, assembly, genome, StrainInfo, and related-record rows found in the pinned local evidence. It has no `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence.

## Findings

- Major: a species-scale GTDB mapping is attached directly to the `Listeria innocua ATCC 33091` strain seed. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Listeria_innocua` to `NCBITaxon:1002366` with `skos:closeMatch` and `genome_count: 182`, and the generator turns that row into a taxonomy mapping, a GTDB xref, and an `EXACT_SYNONYM` of `Listeria innocua`. Owner: the GTDB mapping import behind `data/raw/gtdb_mappings.tsv` and the generated `data/taxa` emission of GTDB close-match synonyms.

## Recommended Edits

- Review whether the `GTDB:s__Listeria_innocua` close match and its derived `Listeria innocua` exact synonym should remain on this strain record, be represented only as a broader species-cluster relationship, or be moved to the `Listeria innocua` species record or another aggregate that does not make one ATCC strain denote the whole GTDB species.

## Follow-up Checks

- After curation, rerun `just validate data/taxa/bacteria/listeria_innocua_atcc_33091.yaml` and `just validate-strict data/taxa/bacteria/listeria_innocua_atcc_33091.yaml`.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `listeria_innocua_atcc_33091` review.
