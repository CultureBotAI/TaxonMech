# YAML Record Review: uncultured Mesoflavibacter sp.

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/uncultured_mesoflavibacter_sp.yaml`
- Started UTC: 2026-09-22T14:51:51Z
- Finished UTC: 2026-09-22T14:52:57Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/uncultured_mesoflavibacter_sp.yaml`
- Identifier: `NCBITaxon:1002544`
- Slug: `uncultured_mesoflavibacter_sp`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1002543` (`environmental samples`)

## Validation

- `just validate data/taxa/bacteria/uncultured_mesoflavibacter_sp.yaml`: passed.
- `just validate-strict data/taxa/bacteria/roseovarius_sp_ri7.yaml data/taxa/bacteria/ruegeria_sp_ri20.yaml data/taxa/bacteria/pseudoalteromonas_sp_ri21.yaml data/taxa/bacteria/uncultured_mesoflavibacter_sp.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002544` / `uncultured Mesoflavibacter sp.`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:1002543` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadati`, the `FCB group`, the `Bacteroidota/Chlorobiota group`, `Bacteroidota`, `Flavobacteriia`, `Flavobacteriales`, `Flavobacteriaceae`, `Mesoflavibacter`, then environmental samples.
- `taxonomy_mappings`, `synonyms`, `xrefs`, and the GTDB `source_attestations` row match `data/raw/gtdb_mappings.tsv` and `data/raw/gtdb_species.tsv`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The local same-record evidence includes the NCBI row and one GTDB `skos:closeMatch` row for `GTDB:s__Mesoflavibacter_sp037029465`; both are represented in the reviewed YAML.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found no ATB, BacDive, GOLD, LPSN, MADIN, MediaDive, BactoTraits, or strain-info rows keyed to `NCBITaxon:1002544`. An exact GTDB identifier search found the expected two-genome `GTDB:s__Mesoflavibacter_sp037029465` species row plus mapping rows from that GTDB cluster to both this record and `NCBITaxon:3107766` / `Mesoflavibacter sp. CH_XMU1404-2`.

## Completeness

The record represents the direct NCBI and GTDB rows found in the pinned local evidence. It has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections; none are required by the reviewed same-taxon evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `uncultured_mesoflavibacter_sp` review.
