# YAML Record Review: Ochrobactrum sp. 'Relman 1999'

## Target

- Record: `data/taxa/bacteria/ochrobactrum_sp_relman_1999.yaml`
- Identifier: `NCBITaxon:100180`
- Slug: `ochrobactrum_sp_relman_1999`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:239106` (`unclassified Ochrobactrum`)

## Validation

- `just validate data/taxa/bacteria/ochrobactrum_sp_relman_1999.yaml`: passed.
- `just validate-strict data/taxa/bacteria/ochrobactrum_sp_relman_1999.yaml data/taxa/bacteria/cupriavidus_agavae.yaml data/taxa/bacteria/variovorax_sp_fr1.yaml data/taxa/bacteria/clostridium_sp_fgh.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:100180` / `Ochrobactrum sp. 'Relman 1999'`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:239106` matches the pinned NCBI parent, `unclassified Ochrobactrum`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, `Brucellaceae`, `Brucella/Ochrobactrum group`, `Ochrobactrum`, then `unclassified Ochrobactrum`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:100180`; its label, synonym, and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:100180`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The NCBI-derived `Brucella-like bacillus 'Relman 1999'` exact synonym is present.

The record has no `taxonomy_mappings`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `ochrobactrum_sp_relman_1999` review.
