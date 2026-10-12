# YAML Record Review: Mycobacteroides abscessus subsp. bolletii 2B-0626

## Target

- Record: `data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0626.yaml`
- Identifier: `NCBITaxon:1001708`
- Slug: `mycobacteroides_abscessus_subsp_bolletii_2b_0626`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:319705` (`Mycobacteroides abscessus subsp. bolletii`)

## Validation

- `just validate data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0626.yaml`: passed.
- `just validate-strict data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0626.yaml data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_1231.yaml data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0107.yaml data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0912_r.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001708` / `Mycobacteroides abscessus subsp. bolletii 2B-0626`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:319705` matches the pinned NCBI parent, `Mycobacteroides abscessus subsp. bolletii`.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Mycobacteriales`, `Mycobacteriaceae`, `Mycobacteroides`, `Mycobacteroides abscessus`, then `Mycobacteroides abscessus subsp. bolletii`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The NCBI, GOLD, and MADIN source attestations are keyed directly to `NCBITaxon:1001708`; their `source_label` values match the reviewed strain and their counts match `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, and the NCBI name row.

The GTDB attestation is different: `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Mycobacterium_abscessus` / `s__Mycobacterium_abscessus` to `NCBITaxon:1001708` with `skos:closeMatch` and `genome_count: 2184`. The same GTDB species row was also observed on many other `Mycobacterium abscessus` strain IDs, on the subspecies parent `NCBITaxon:319705`, and on the species parent `NCBITaxon:36809`.

## Completeness

The NCBI-derived synonyms preserve the `2B-0626` strain suffix and are consistent with the reviewed strain:

- `Mycobacterium abscessus subsp. bolletii 2B-0626`
- `Mycobacterium massiliense 2B-0626`

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections, which is expected for a named strain. The only questionable completeness item is the GTDB xref described below.

## Findings

### Major: Species-level GTDB evidence is attached to one NCBI strain

The `taxonomy_mappings` entry, `GTDB:s__Mycobacterium_abscessus` xref, GTDB `source_attestations` entry, and GTDB-derived `Mycobacterium abscessus` exact synonym all describe a GTDB species cluster with 2,184 genomes. The reviewed target is a single NCBI `STRAIN`, `Mycobacteroides abscessus subsp. bolletii 2B-0626`.

Treating `Mycobacterium abscessus` as an `EXACT_SYNONYM` of this strain and attributing the 2,184-genome GTDB species count to the strain overstates the evidence.

## Recommended Edits

- Route the `GTDB:s__Mycobacterium_abscessus` mapping and 2,184-genome count to the species-level `NCBITaxon:36809` record, or otherwise keep it off individual NCBI `STRAIN` records unless there is strain-specific GTDB evidence.
- Suppress the GTDB-derived exact synonym and `GTDB:s__Mycobacterium_abscessus` xref on `NCBITaxon:1001708`; keep the direct NCBITAXON, GOLD, and MADIN attestations.
- Add a regression check that prevents a GTDB `s__` cluster from being projected as an `EXACT_SYNONYM` or genome-count attestation onto a lower-rank NCBI strain target.

## Follow-up Checks

- After fixing the GTDB fan-out logic, re-check adjacent `Mycobacteroides abscessus` strain IDs that share `GTDB:s__Mycobacterium_abscessus`.
- Confirm that `NCBITaxon:36809` retains the species-level GTDB mapping and that duplicate mappings to `NCBITaxon:319705` or strain-level descendants are removed or downgraded consistently.

## Additional Notes

- The review used pinned local `data/raw/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `mycobacteroides_abscessus_subsp_bolletii_2b_0626` review.
