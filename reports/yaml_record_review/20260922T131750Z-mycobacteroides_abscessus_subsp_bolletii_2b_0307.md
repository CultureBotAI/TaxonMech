# YAML Record Review: Mycobacteroides abscessus subsp. bolletii 2B-0307

## Target

- Record: `data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0307.yaml`
- Identifier: `NCBITaxon:1001713`
- Slug: `mycobacteroides_abscessus_subsp_bolletii_2b_0307`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:319705` (`Mycobacteroides abscessus subsp. bolletii`)

## Validation

- `just validate data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0307.yaml`: passed.
- `just validate-strict data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0912_s.yaml data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0307.yaml data/taxa/bacteria/mycobacteroides_abscessus_subsp_massiliense_ccug_48898_jcm_15300.yaml data/taxa/bacteria/mycobacteroides_abscessus_3a_0122_r.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001713` / `Mycobacteroides abscessus subsp. bolletii 2B-0307`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:319705` matches the pinned NCBI parent, `Mycobacteroides abscessus subsp. bolletii`.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Mycobacteriales`, `Mycobacteriaceae`, `Mycobacteroides`, `Mycobacteroides abscessus`, then `Mycobacteroides abscessus subsp. bolletii`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The NCBI, GOLD, and MADIN attestations are keyed directly to `NCBITaxon:1001713`; their labels and assertion counts match the reviewed raw rows. The GTDB evidence is the species-level `GTDB:s__Mycobacterium_abscessus` mapping to `NCBITaxon:1001713` with `skos:closeMatch` and `genome_count: 2184`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected NCBI, GOLD, MADIN, and GTDB rows keyed to `NCBITaxon:1001713`, and no ATB, BacDive, or strain-info rows keyed to this identifier.

## Completeness

The NCBI-derived synonyms preserve the `2B-0307` strain suffix and are consistent with the reviewed strain:

- `Mycobacterium abscessus subsp. bolletii 2B-0307`
- `Mycobacterium massiliense 2B-0307`

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. The only questionable completeness item is the GTDB xref described below.

## Findings

### Major: Species-level GTDB evidence is attached to one NCBI strain

The `taxonomy_mappings` entry, `GTDB:s__Mycobacterium_abscessus` xref, GTDB `source_attestations` entry, and GTDB-derived `Mycobacterium abscessus` exact synonym all describe a GTDB species cluster with 2,184 genomes. The reviewed target is a single NCBI `STRAIN`, `Mycobacteroides abscessus subsp. bolletii 2B-0307`; treating the GTDB species label as an exact synonym of this strain overstates equivalence.

## Recommended Edits

- Route the `GTDB:s__Mycobacterium_abscessus` mapping and 2,184-genome count to the species-level `NCBITaxon:36809` record, or keep it off individual NCBI `STRAIN` records unless there is strain-specific GTDB evidence.
- Suppress the GTDB-derived exact synonym and `GTDB:s__Mycobacterium_abscessus` xref on `NCBITaxon:1001713`; keep the direct NCBITAXON, GOLD, and MADIN attestations.
- Add a regression check that prevents a GTDB `s__` cluster from being projected as an `EXACT_SYNONYM` or genome-count attestation onto a lower-rank NCBI strain target.

## Follow-up Checks

- Re-check adjacent `Mycobacteroides abscessus` strain IDs that share `GTDB:s__Mycobacterium_abscessus` after the GTDB fan-out is fixed.

## Additional Notes

- The review used pinned local `data/raw/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `mycobacteroides_abscessus_subsp_bolletii_2b_0307` review.
