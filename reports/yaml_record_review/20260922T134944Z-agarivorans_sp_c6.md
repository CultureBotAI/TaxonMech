# YAML Record Review: Agarivorans sp. C6

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/agarivorans_sp_c6.yaml`
- Started UTC: 2026-09-22T13:49:44Z
- Finished UTC: 2026-09-22T13:51:26Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/agarivorans_sp_c6.yaml`
- Identifier: `NCBITaxon:1001885`
- Slug: `agarivorans_sp_c6`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2636026` (`unclassified Agarivorans`)

## Validation

- `just validate data/taxa/bacteria/agarivorans_sp_c6.yaml`: passed.
- `just validate-strict data/taxa/bacteria/uncultured_ahrensia_sp.yaml data/taxa/bacteria/vibrio_sp_c1.yaml data/taxa/bacteria/vibrio_sp_c5.yaml data/taxa/bacteria/agarivorans_sp_c6.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001885` / `Agarivorans sp. C6`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:2636026` matches the pinned NCBI parent, `unclassified Agarivorans`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Gammaproteobacteria`, `Alteromonadales`, `Alteromonadaceae`, `Agarivorans`, then `unclassified Agarivorans`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The only exact same-taxon source row is the NCBI row for `NCBITaxon:1001885`; its label and parentage match the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI row keyed to `NCBITaxon:1001885`, and no ATB, BacDive, GOLD, GTDB, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The record has no `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `agarivorans_sp_c6` review.
