# YAML Record Review: Methylovorus menthalis

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/methylovorus_menthalis.yaml`
- Started UTC: 2026-09-22T14:18:42Z
- Finished UTC: 2026-09-22T14:20:17Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/methylovorus_menthalis.yaml`
- Identifier: `NCBITaxon:1002227`
- Slug: `methylovorus_menthalis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:81682` (`Methylovorus`)

## Validation

- `just validate data/taxa/bacteria/methylovorus_menthalis.yaml`: passed.
- `just validate-strict data/taxa/bacteria/methylovorus_menthalis.yaml data/taxa/bacteria/exiguobacterium_sp_niu_k2.yaml data/taxa/bacteria/exiguobacterium_sp_niu_k4.yaml data/taxa/bacteria/staphylococcus_sp_niu_k1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002227` / `Methylovorus menthalis`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, `rank`, and `parent_taxon: NCBITaxon:81682` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadota`, `Betaproteobacteria`, `Nitrosomonadales`, `Methylophilaceae`, then `Methylovorus`.
- The `LPSN` name entry, `GTDB:s__Methylovorus_menthalis` mapping, and NCBI synonyms are all represented in `nomenclature`, `taxonomy_mappings`, `synonyms`, and `xrefs`.
- `grounding_status: EXACT` is correct for this exact species seed.

## Evidence

The exact `rg --no-ignore --hidden` scan over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected seven-source seed for `Methylovorus menthalis`: NCBI Taxonomy, LPSN, GTDB, BacDive, MediaDive, GOLD, and BactoTraits.

The reviewed YAML carries the expected BacDive strain `bacdive:7246`, culture collection IDs `CCUG-61695`, `DSM-24715`, and `VKM-B-2663`, VKM B-2663 assembly/genome rows from BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly, ATB assembly `atb.assembly:202505.SAMN22209864`, GOLD analysis/organism/project related records, BioProject/BioSample links, and StrainInfo links for the CCUG and DSM deposits.

## Completeness

The record includes nomenclature, `skos:closeMatch` GTDB mapping, cross-references, NCBI synonyms, the type-strain BacDive row, assembly/genome links, ATB evidence, related records, and the 7 source attestations present in the pinned local evidence. No missing same-taxon evidence was found.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `methylovorus_menthalis` review.
