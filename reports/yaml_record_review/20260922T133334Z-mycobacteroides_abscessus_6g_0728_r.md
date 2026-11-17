# YAML Record Review: Mycobacteroides abscessus 6G-0728-R

## Target

- Record: `data/taxa/bacteria/mycobacteroides_abscessus_6g_0728_r.yaml`
- Identifier: `NCBITaxon:1001737`
- Slug: `mycobacteroides_abscessus_6g_0728_r`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:36809` (`Mycobacteroides abscessus`)

## Validation

- `just validate data/taxa/bacteria/mycobacteroides_abscessus_6g_0728_r.yaml`: passed.
- `just validate-strict data/taxa/bacteria/mycobacteroides_abscessus_6g_0728_s.yaml data/taxa/bacteria/mycobacteroides_abscessus_6g_0728_r.yaml data/taxa/bacteria/mycobacteroides_abscessus_6g_1108.yaml data/taxa/bacteria/mycobacteroides_abscessus_6g_0212.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001737` / `Mycobacteroides abscessus 6G-0728-R`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:36809` matches the pinned NCBI parent, `Mycobacteroides abscessus`.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Mycobacteriales`, `Mycobacteriaceae`, `Mycobacteroides`, then `Mycobacteroides abscessus`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The NCBI and MADIN attestations are keyed directly to `NCBITaxon:1001737`; their labels and assertion counts match the reviewed raw rows. The GTDB evidence is the species-level `GTDB:s__Mycobacterium_abscessus` mapping to `NCBITaxon:1001737` with `skos:closeMatch` and `genome_count: 2184`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected NCBI, MADIN, and GTDB rows keyed to `NCBITaxon:1001737`, and no ATB, BacDive, GOLD, or strain-info rows keyed to this identifier.

## Completeness

The NCBI-derived `Mycobacterium abscessus 6G-0728-R` synonym preserves the strain suffix and is consistent with the reviewed strain.

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. The only questionable completeness item is the GTDB xref described below.

## Findings

### Major: Species-level GTDB evidence is attached to one NCBI strain

The `taxonomy_mappings` entry, `GTDB:s__Mycobacterium_abscessus` xref, GTDB `source_attestations` entry, and GTDB-derived `Mycobacterium abscessus` exact synonym all describe a GTDB species cluster with 2,184 genomes. The reviewed target is a single NCBI `STRAIN`, `Mycobacteroides abscessus 6G-0728-R`; treating the GTDB species label as an exact synonym of this strain overstates equivalence.

## Recommended Edits

- Route the `GTDB:s__Mycobacterium_abscessus` mapping and 2,184-genome count to the species-level `NCBITaxon:36809` record, or keep it off individual NCBI `STRAIN` records unless there is strain-specific GTDB evidence.
- Suppress the GTDB-derived exact synonym and `GTDB:s__Mycobacterium_abscessus` xref on `NCBITaxon:1001737`; keep the direct NCBITAXON and MADIN attestations.
- Add a regression check that prevents a GTDB `s__` cluster from being projected as an `EXACT_SYNONYM` or genome-count attestation onto a lower-rank NCBI strain target.

## Follow-up Checks

- Re-check adjacent `Mycobacteroides abscessus` strain IDs that share `GTDB:s__Mycobacterium_abscessus` after the GTDB fan-out is fixed.

## Additional Notes

- The review used pinned local `data/raw/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `mycobacteroides_abscessus_6g_0728_r` review.
