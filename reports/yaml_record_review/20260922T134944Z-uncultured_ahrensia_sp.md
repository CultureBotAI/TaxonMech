# YAML Record Review: uncultured Ahrensia sp.

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/uncultured_ahrensia_sp.yaml`
- Started UTC: 2026-09-22T13:49:44Z
- Finished UTC: 2026-09-22T13:51:26Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/uncultured_ahrensia_sp.yaml`
- Identifier: `NCBITaxon:1001867`
- Slug: `uncultured_ahrensia_sp`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1001866` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/uncultured_ahrensia_sp.yaml`: passed.
- `just validate-strict data/taxa/bacteria/uncultured_ahrensia_sp.yaml data/taxa/bacteria/vibrio_sp_c1.yaml data/taxa/bacteria/vibrio_sp_c5.yaml data/taxa/bacteria/agarivorans_sp_c6.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001867` / `uncultured Ahrensia sp.`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:1001866` matches the pinned NCBI parent, `environmental samples`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, `Ahrensiaceae`, `Ahrensia`, then `environmental samples`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI and GTDB attestations are keyed directly to `NCBITaxon:1001867`; their labels and assertion counts match the reviewed raw rows. The GTDB evidence is the species-level `GTDB:s__Oricola_sp002706335` close match with `genome_count: 9`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI and GTDB rows keyed to `NCBITaxon:1001867`, and no ATB, BacDive, GOLD, LPSN, MADIN, or strain-info rows keyed to this identifier.

## Completeness

The GTDB-derived `Oricola sp002706335` exact synonym and xref are present and preserve the only non-NCBI mapping for this species-rank record.

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_ahrensia_sp` review.
