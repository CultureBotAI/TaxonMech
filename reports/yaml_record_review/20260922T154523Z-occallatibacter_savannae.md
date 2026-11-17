# YAML Record Review: Occallatibacter savannae

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/occallatibacter_savannae.yaml`
- Started UTC: 2026-09-22T15:44:28Z
- Finished UTC: 2026-09-22T15:45:23Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/occallatibacter_savannae.yaml`
- Identifier: `NCBITaxon:1002691`
- Slug: `occallatibacter_savannae`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1742983` (`Occallatibacter`)

## Validation

- `just validate data/taxa/bacteria/occallatibacter_savannae.yaml`: passed.
- `just validate-strict data/taxa/bacteria/roseovarius_sp_iob_2.yaml data/taxa/bacteria/roseovarius_sp_iob_7.yaml data/taxa/bacteria/occallatibacter_riparius.yaml data/taxa/bacteria/occallatibacter_savannae.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002691` / `Occallatibacter savannae`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:1742983` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadati`, `Acidobacteriota`, `Terriglobia`, `Terriglobales`, `Acidobacteriaceae`, then `Occallatibacter`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The exact same-taxon source rows cover the seven source families named in `source_attestations`: NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, and BactoTraits.

- The NCBI row supplies two related synonyms and type-material rows for strain `A2-1c`, `DSM 25170`, and `LMG 26946`; the related synonyms and type-strain flag on `kgmicrobe.strain:bacdive_132353` are present in the YAML.
- The LPSN row for `lpsn:793732` is a correct species name, links `NCBITaxon:1002691`, designates `kgmicrobe.strain:DSM-25170` and `kgmicrobe.strain:LMG-26946`, and supplies the two DOIs, one PMID, and `INSDC:HQ995661`; the `nomenclature` entry carries those values.
- The GTDB row maps `GTDB:s__Telmatobacter_savannae` to this taxon with `skos:closeMatch` and 1 genome, matching the YAML `taxonomy_mappings`, GTDB xref, GTDB exact synonym, and GTDB source attestation.
- The BacDive row supplies one strain, matching `strain_count: 1`; the GOLD and StrainInfo related records are represented under the expected strain entry.
- The MediaDive, GOLD, and BactoTraits rows report assertion counts of 1 medium, 3 organisms, and 22 trait assertions, matching the corresponding `source_attestations`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected same-taxon rows and no unresolved same-taxon ATB, MADIN, or extra StrainInfo evidence outside the reviewed YAML.

## Completeness

The record carries the expected LPSN `nomenclature`, GTDB `taxonomy_mappings`, NCBI and GTDB `synonyms`, GTDB and LPSN `xrefs`, BacDive `strains`, and source attestations for all seven local source families. There are no `comments` or product-level sections. None are required by the reviewed local evidence.

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
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `occallatibacter_savannae` review.
