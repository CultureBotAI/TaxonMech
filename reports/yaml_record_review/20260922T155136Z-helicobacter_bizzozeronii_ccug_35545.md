# YAML Record Review: Helicobacter bizzozeronii CCUG 35545

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/helicobacter_bizzozeronii_ccug_35545.yaml`
- Started UTC: 2026-09-22T15:50:32Z
- Finished UTC: 2026-09-22T15:51:36Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/helicobacter_bizzozeronii_ccug_35545.yaml`
- Identifier: `NCBITaxon:1002805`
- Slug: `helicobacter_bizzozeronii_ccug_35545`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:56877` (`Helicobacter bizzozeronii`)

## Validation

- `just validate data/taxa/bacteria/helicobacter_bizzozeronii_ccug_35545.yaml`: passed.
- `just validate-strict data/taxa/bacteria/helicobacter_bizzozeronii_ccug_35545.yaml data/taxa/bacteria/helicobacter_salomonis_o6a.yaml data/taxa/bacteria/solibacillus_silvestris_stlb046.yaml data/taxa/bacteria/bacillus_sp_8b2.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1002805` / `Helicobacter bizzozeronii CCUG 35545`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:56877` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadati`, `Campylobacterota`, `Epsilonproteobacteria`, `Campylobacterales`, `Helicobacteraceae`, `Helicobacter`, then `Helicobacter bizzozeronii`.
- The two NCBI exact synonyms in `data/raw/ncbitaxon_taxa.tsv` are present in `synonyms`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The exact same-taxon rows for `NCBITaxon:1002805` cover the NCBI, GTDB, BacDive, and MADIN source families named in `source_attestations`.

- The GTDB row maps `GTDB:s__Helicobacter_bizzozeronii` to this taxon with `skos:closeMatch` and 13 genomes, matching the YAML `taxonomy_mappings`, GTDB exact synonym, GTDB xref, and GTDB source attestation.
- The BacDive row supplies one strain, `kgmicrobe.strain:bacdive_135500`, with the `CCUG-35045`, `CCUG-35545`, and `CIP-105233` culture-collection deposits, matching `strain_count: 1` and the reviewed `strains` entry.
- A secondary exact scan for `kgmicrobe.strain:bacdive_135500` and its culture-collection identifiers found the expected GOLD, BV-BRC, GTDB, NCBI Assembly, and StrainInfo evidence rows that are nested under the strain entry; several `CIP-105233` and StrainInfo rows are filed under the parent species `NCBITaxon:56877` but join through the same BacDive strain.
- The MADIN row is keyed to `NCBITaxon:1002805` with assertion count 1, matching the MADIN `source_attestations` entry.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected same-taxon and linked strain rows and no ATB, MediaDive, or BactoTraits rows keyed to this identifier.

## Completeness

The record carries the expected GTDB `taxonomy_mappings`, NCBI and GTDB `synonyms`, GTDB `xrefs`, BacDive `strains`, and NCBI, GTDB, BacDive, and MADIN `source_attestations`. There are no `comments` or product-level sections. None are required by the reviewed same-taxon local evidence.

## Findings

No findings in this generated YAML relative to the pinned local source rows.

## Recommended Edits

- None.

## Follow-up Checks

- Review whether the upstream `GTDB:s__Helicobacter_bizzozeronii` `skos:closeMatch` rows should point at strain-level NCBI taxa. The same GTDB species also maps to the parent species `NCBITaxon:56877` and to sibling strain `NCBITaxon:1002804` in `data/raw/gtdb_mappings.tsv`.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `helicobacter_bizzozeronii_ccug_35545` review.
