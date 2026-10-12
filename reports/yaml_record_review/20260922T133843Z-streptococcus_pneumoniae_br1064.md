# YAML Record Review: Streptococcus pneumoniae BR1064

## Target

- Record: `data/taxa/bacteria/streptococcus_pneumoniae_br1064.yaml`
- Identifier: `NCBITaxon:1001746`
- Slug: `streptococcus_pneumoniae_br1064`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1313` (`Streptococcus pneumoniae`)

## Validation

- `just validate data/taxa/bacteria/streptococcus_pneumoniae_br1064.yaml`: passed.
- `just validate-strict data/taxa/bacteria/streptococcus_pneumoniae_07ar0125.yaml data/taxa/bacteria/streptococcus_pneumoniae_br1064.yaml data/taxa/bacteria/streptococcus_pneumoniae_nd6012.yaml data/taxa/bacteria/papillibacter_cinnamivorans.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001746` / `Streptococcus pneumoniae BR1064`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:1313` matches the pinned NCBI parent, `Streptococcus pneumoniae`.
- The lineage stays within Bacteria through `Bacillota`, `Bacilli`, `Lactobacillales`, `Streptococcaceae`, `Streptococcus`, then `Streptococcus pneumoniae`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The NCBI, GOLD, and MADIN attestations are keyed directly to `NCBITaxon:1001746`; their labels and assertion counts match the reviewed raw rows. The GTDB evidence is the species-level `GTDB:s__Streptococcus_pneumoniae` mapping to `NCBITaxon:1001746` with `skos:closeMatch` and `genome_count: 9634`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI, GOLD, MADIN, and GTDB rows keyed to `NCBITaxon:1001746`, and no ATB, BacDive, LPSN, or strain-info rows keyed to this identifier.

## Completeness

The NCBI-derived `Streptococcus pneumoniae str. BR1064` and `Streptococcus pneumoniae strain BR1064` synonyms preserve the strain identifier and are consistent with the reviewed strain.

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. The only questionable completeness item is the GTDB xref described below.

## Findings

### Major: Species-level GTDB evidence is attached to one NCBI strain

The `taxonomy_mappings` entry, `GTDB:s__Streptococcus_pneumoniae` xref, GTDB `source_attestations` entry, and GTDB-derived `Streptococcus pneumoniae` exact synonym all describe a GTDB species cluster with 9,634 genomes. The reviewed target is a single NCBI `STRAIN`, `Streptococcus pneumoniae BR1064`; treating the GTDB species label as an exact synonym of this strain overstates equivalence.

## Recommended Edits

- Route the `GTDB:s__Streptococcus_pneumoniae` mapping and 9,634-genome count to the species-level `NCBITaxon:1313` record, or keep it off individual NCBI `STRAIN` records unless there is strain-specific GTDB evidence.
- Suppress the GTDB-derived exact synonym and `GTDB:s__Streptococcus_pneumoniae` xref on `NCBITaxon:1001746`; keep the direct NCBITAXON, GOLD, and MADIN attestations.
- Add a regression check that prevents a GTDB `s__` cluster from being projected as an `EXACT_SYNONYM` or genome-count attestation onto a lower-rank NCBI strain target.

## Follow-up Checks

- Re-check adjacent `Streptococcus pneumoniae` strain IDs that share `GTDB:s__Streptococcus_pneumoniae` after the GTDB fan-out is fixed.

## Additional Notes

- The review used pinned local `data/raw/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `streptococcus_pneumoniae_br1064` review.
