# YAML Record Review: Streptomyces coelicolor A3(2)

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/streptomyces_coelicolor_a3_2.yaml`
- Started UTC: 2026-09-22T14:25:04Z
- Finished UTC: 2026-09-22T14:26:57Z
- Verdict: needs curation

## Target

- Record: `data/taxa/bacteria/streptomyces_coelicolor_a3_2.yaml`
- Identifier: `NCBITaxon:100226`
- Slug: `streptomyces_coelicolor_a3_2`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1902` (`Streptomyces coelicolor`)

## Validation

- `just validate data/taxa/bacteria/streptomyces_coelicolor_a3_2.yaml`: passed.
- `just validate-strict data/taxa/bacteria/serratia_sp_pt19.yaml data/taxa/bacteria/austwickia_chelonae.yaml data/taxa/bacteria/streptomyces_coelicolor_a3_2.yaml data/taxa/bacteria/bradyrhizobium_sp_pe2_6.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The NCBI strain identity is exact for `NCBITaxon:100226` / `Streptomyces coelicolor A3(2)`.

- `identifier`, `label`, `rank: STRAIN`, `genetic_code: 11`, and `parent_taxon: NCBITaxon:1902` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Kitasatosporales`, `Streptomycetaceae`, `Streptomyces`, `Streptomyces albidoflavus group`, then `Streptomyces coelicolor`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The same-taxon NCBI row is keyed to the strain `NCBITaxon:100226`, but `data/raw/gtdb_mappings.tsv` also maps `GTDB:s__Streptomyces_violaceoruber` to this strain with `skos:closeMatch` and `genome_count: 182`. A gitignore-independent exact search for that GTDB species found it maps to many NCBI taxa, including the parent species `Streptomyces coelicolor` as `skos:broadMatch` and LPSN species `NCBITaxon:1935` as `skos:broadMatch`.

The local exact-ID search also found 17 GOLD organism assertions and 7 MADIN trait assertions keyed directly to `NCBITaxon:100226`. The reviewed YAML carries those source attestations, plus the GTDB taxonomy mapping, GTDB xref, and GTDB exact synonym.

## Completeness

The local evidence keyed directly to `NCBITaxon:100226` is represented. The record has no `strains`, `related_records`, `causal_graphs`, or product-level sections.

## Findings

- Needs curation: species-scale GTDB evidence is attached directly to the `Streptomyces coelicolor A3(2)` strain seed. `GTDB:s__Streptomyces_violaceoruber` has 182 genomes and maps onto many NCBI taxa, so its use as a `skos:closeMatch`, `xrefs` entry, and exact synonym on a strain record needs curator review.

## Recommended Edits

- Review whether the GTDB species mapping, GTDB-derived exact synonym, 17 GOLD organism assertions, and 7 MADIN trait assertions keyed to `NCBITaxon:100226` should remain on this strain record or be moved to a species-level aggregate or descendant strain record that does not conflate one NCBI strain with a broad GTDB species cluster.

## Follow-up Checks

- After curation, rerun `just validate data/taxa/bacteria/streptomyces_coelicolor_a3_2.yaml` and `just validate-strict data/taxa/bacteria/streptomyces_coelicolor_a3_2.yaml`.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `streptomyces_coelicolor_a3_2` review.
