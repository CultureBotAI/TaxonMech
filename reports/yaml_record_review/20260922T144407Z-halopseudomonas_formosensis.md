# YAML Record Review: Halopseudomonas formosensis

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/halopseudomonas_formosensis.yaml`
- Started UTC: 2026-09-22T14:42:07Z
- Finished UTC: 2026-09-22T14:44:07Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/halopseudomonas_formosensis.yaml`
- Identifier: `NCBITaxon:1002526`
- Slug: `halopseudomonas_formosensis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2901189` (`Halopseudomonas`)

## Validation

- `just validate data/taxa/bacteria/halopseudomonas_formosensis.yaml`: passed.
- `just validate-strict data/taxa/bacteria/planktothricoides_raciborskii_chab3331.yaml data/taxa/bacteria/pseudanabaena_sp_dqh15.yaml data/taxa/bacteria/halopseudomonas_formosensis.yaml data/taxa/bacteria/streptomyces_sp_ca1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The species identity is exact for `NCBITaxon:1002526` / `Halopseudomonas formosensis`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:2901189` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadota`, `Gammaproteobacteria`, `Pseudomonadales`, `Pseudomonadaceae`, then `Halopseudomonas`.
- The LPSN nomenclature block for `lpsn:22477` agrees with the reviewed species name, marks it as validly published, legitimate, and correct, carries the expected JCM type-strain designation, and links `GTDB:s__Halopseudomonas_formosensis`.
- The NCBI and LPSN synonyms cover prior `Pseudomonas formosensis` and `Neopseudomonas formosensis` names.
- `GTDB:s__Halopseudomonas_formosensis` is a close match with a note that LPSN links this GTDB species to the taxon's name.
- The BacDive strain subrecord represents the type strain `bacdive:133985`, designation `CC-CY503`, and the BCRC and JCM culture-collection deposits.
- `grounding_status: EXACT` is correct for the NCBI species seed.

## Evidence

The local exact-ID search found the NCBI row, the LPSN row, one GTDB `skos:closeMatch` row, one BacDive type strain, one GOLD organism, eight MADIN trait assertions, six NCBI type-material rows, the expected StrainInfo rows, and the expected ATB links keyed to `NCBITaxon:1002526`. The exact BacDive-strain search for `kgmicrobe.strain:bacdive_133985` also found the assemblies, genome records, related BioProject/BioSample/GOLD records, StrainInfo deposits, and ATB genome links used by the reviewed `strains` block.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found no MediaDive or BactoTraits source-attestation rows keyed to `NCBITaxon:1002526`.

## Completeness

The record represents the direct NCBI, LPSN, BacDive, GTDB, GOLD, MADIN, assembly, genome, StrainInfo, ATB, NCBI type-material, and related-record rows found in the pinned local evidence. It has no `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `halopseudomonas_formosensis` review.
