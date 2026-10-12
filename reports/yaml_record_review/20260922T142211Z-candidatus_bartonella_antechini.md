# YAML Record Review: Candidatus Bartonella antechini

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/candidatus_bartonella_antechini.yaml`
- Started UTC: 2026-09-22T14:21:13Z
- Finished UTC: 2026-09-22T14:22:11Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/candidatus_bartonella_antechini.yaml`
- Identifier: `NCBITaxon:1002233`
- Slug: `candidatus_bartonella_antechini`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:773` (`Bartonella`)

## Validation

- `just validate data/taxa/bacteria/candidatus_bartonella_antechini.yaml`: passed.
- `just validate-strict data/taxa/bacteria/oenothera_biennis_yellows_phytoplasma.yaml data/taxa/bacteria/candidatus_bartonella_antechini.yaml data/taxa/bacteria/scorzonera_hispanica_yellows_phytoplasma.yaml data/taxa/bacteria/pseudomonas_sp_aw1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002233` / `Candidatus Bartonella antechini`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, `rank`, `parent_taxon: NCBITaxon:773`, and the two NCBI synonyms match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, `Bartonellaceae`, then `Bartonella`.
- `Bartonella antechini` is represented as an exact synonym, while `"Candidatus Bartonella antechini" Kaewmangkol et al. 2011` is represented as a related synonym.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1002233`; its label, parentage, and synonym fields match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1002233`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The record includes the NCBI exact and related synonyms. It has no `taxonomy_mappings`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `candidatus_bartonella_antechini` review.
