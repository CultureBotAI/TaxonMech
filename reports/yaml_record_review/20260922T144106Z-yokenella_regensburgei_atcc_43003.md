# YAML Record Review: Yokenella regensburgei ATCC 43003

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/yokenella_regensburgei_atcc_43003.yaml`
- Started UTC: 2026-09-22T14:39:40Z
- Finished UTC: 2026-09-22T14:41:06Z
- Verdict: needs curation

## Target

- Record: `data/taxa/bacteria/yokenella_regensburgei_atcc_43003.yaml`
- Identifier: `NCBITaxon:1002368`
- Slug: `yokenella_regensburgei_atcc_43003`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:158877` (`Yokenella regensburgei`)

## Validation

- `just validate data/taxa/bacteria/yokenella_regensburgei_atcc_43003.yaml`: passed.
- `just validate-strict data/taxa/bacteria/listeria_innocua_atcc_33091.yaml data/taxa/bacteria/leyella_stercorea_dsm_18206.yaml data/taxa/bacteria/yokenella_regensburgei_atcc_43003.yaml data/taxa/bacteria/clostridioides_difficile_70_100_2010.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The NCBI strain identity is exact for `NCBITaxon:1002368` / `Yokenella regensburgei ATCC 43003`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:158877` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadota`, `Gammaproteobacteria`, `Enterobacterales`, `Enterobacteriaceae`, `Yokenella`, then `Yokenella regensburgei`.
- NCBI exact synonyms `Yokenella regensburgei str. ATCC 43003` and `Yokenella regensburgei strain ATCC 43003` are both represented.
- The BacDive strain subrecord represents `bacdive:164881` and its ATCC, CDC, and JCM culture-collection deposits.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.
- The GTDB-derived close match and exact synonym need curation review because `GTDB:s__Yokenella_regensburgei`, a 21-genome species cluster that also maps to the parent species `NCBITaxon:158877`, is grafted directly onto the ATCC 43003 strain.

## Evidence

The local same-record evidence includes the NCBI row, one GTDB `skos:closeMatch` row, one BacDive strain, and one MADIN trait assertion keyed directly to `NCBITaxon:1002368`. The exact BacDive-strain search for `kgmicrobe.strain:bacdive_164881` also found the expected assemblies, genome records, related BioProject/BioSample/GOLD records, and StrainInfo deposit rows used by the reviewed `strains` block.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found no ATB, GOLD aggregate, LPSN, MediaDive, or BactoTraits source-attestation rows keyed to `NCBITaxon:1002368`. An exact GTDB ID search found `GTDB:s__Yokenella_regensburgei` mapped to both this strain and the parent species `NCBITaxon:158877`.

## Completeness

The record represents the direct NCBI, BacDive, GTDB, MADIN, assembly, genome, StrainInfo, and related-record rows found in the pinned local evidence. It has no `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence.

## Findings

- Major: a species-scale GTDB mapping is attached directly to the `Yokenella regensburgei ATCC 43003` strain seed. `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Yokenella_regensburgei` to `NCBITaxon:1002368` with `skos:closeMatch` and `genome_count: 21`, and the generator turns that row into a taxonomy mapping, a GTDB xref, and an `EXACT_SYNONYM` of `Yokenella regensburgei`. Owner: the GTDB mapping import behind `data/raw/gtdb_mappings.tsv` and the generated `data/taxa` emission of GTDB close-match synonyms.

## Recommended Edits

- Review whether the `GTDB:s__Yokenella_regensburgei` close match and its derived `Yokenella regensburgei` exact synonym should remain on this strain record, be represented only as a broader species-cluster relationship, or be moved to the `Yokenella regensburgei` species record or another aggregate that does not make one ATCC strain denote the whole GTDB species.

## Follow-up Checks

- After curation, rerun `just validate data/taxa/bacteria/yokenella_regensburgei_atcc_43003.yaml` and `just validate-strict data/taxa/bacteria/yokenella_regensburgei_atcc_43003.yaml`.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `yokenella_regensburgei_atcc_43003` review.
