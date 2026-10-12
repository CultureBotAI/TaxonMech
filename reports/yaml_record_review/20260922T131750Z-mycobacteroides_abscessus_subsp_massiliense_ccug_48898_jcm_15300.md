# YAML Record Review: Mycobacteroides abscessus subsp. massiliense CCUG 48898 = JCM 15300

## Target

- Record: `data/taxa/bacteria/mycobacteroides_abscessus_subsp_massiliense_ccug_48898_jcm_15300.yaml`
- Identifier: `NCBITaxon:1001714`
- Slug: `mycobacteroides_abscessus_subsp_massiliense_ccug_48898_jcm_15300`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1962118` (`Mycobacteroides abscessus subsp. massiliense`)

## Validation

- `just validate data/taxa/bacteria/mycobacteroides_abscessus_subsp_massiliense_ccug_48898_jcm_15300.yaml`: passed.
- `just validate-strict data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0912_s.yaml data/taxa/bacteria/mycobacteroides_abscessus_subsp_bolletii_2b_0307.yaml data/taxa/bacteria/mycobacteroides_abscessus_subsp_massiliense_ccug_48898_jcm_15300.yaml data/taxa/bacteria/mycobacteroides_abscessus_3a_0122_r.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001714` / `Mycobacteroides abscessus subsp. massiliense CCUG 48898 = JCM 15300`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:1962118` matches the pinned NCBI parent, `Mycobacteroides abscessus subsp. massiliense`.
- The lineage stays within Bacteria through `Actinomycetota`, `Actinomycetes`, `Mycobacteriales`, `Mycobacteriaceae`, `Mycobacteroides`, `Mycobacteroides abscessus`, then `Mycobacteroides abscessus subsp. massiliense`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The NCBI, GOLD, and MADIN attestations are keyed directly to `NCBITaxon:1001714`; their labels match the reviewed strain and their assertion counts match the NCBI, GOLD, and MADIN rows. GOLD contributes five organism assertions for this culture-collection strain. The GTDB evidence is the species-level `GTDB:s__Mycobacterium_abscessus` mapping to `NCBITaxon:1001714` with `skos:closeMatch` and `genome_count: 2184`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected NCBI, GOLD, MADIN, GTDB, and same-strain assembly/related rows keyed to `NCBITaxon:1001714`.

## Completeness

The NCBI-derived synonyms retain the `CCUG 48898`, `JCM 15300`, or combined `CCUG 48898 = JCM 15300` strain designations and are consistent with the reviewed strain.

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. The strain-specific assembly and related rows in `data/raw/strain_*` are all keyed to the same NCBI identifier; they do not alter the taxon identity finding here. The questionable item is the species-level GTDB xref described below.

## Findings

### Major: Species-level GTDB evidence is attached to one NCBI strain

The `taxonomy_mappings` entry, `GTDB:s__Mycobacterium_abscessus` xref, GTDB `source_attestations` entry, and GTDB-derived `Mycobacterium abscessus` exact synonym all describe a GTDB species cluster with 2,184 genomes. The reviewed target is a single NCBI `STRAIN`, `Mycobacteroides abscessus subsp. massiliense CCUG 48898 = JCM 15300`; treating the GTDB species label as an exact synonym of this strain overstates equivalence.

## Recommended Edits

- Route the `GTDB:s__Mycobacterium_abscessus` mapping and 2,184-genome count to the species-level `NCBITaxon:36809` record, or keep it off individual NCBI `STRAIN` records unless there is strain-specific GTDB evidence.
- Suppress the GTDB-derived exact synonym and `GTDB:s__Mycobacterium_abscessus` xref on `NCBITaxon:1001714`; keep the direct NCBITAXON, GOLD, and MADIN attestations.
- Add a regression check that prevents a GTDB `s__` cluster from being projected as an `EXACT_SYNONYM` or genome-count attestation onto a lower-rank NCBI strain target.

## Follow-up Checks

- Re-check adjacent `Mycobacteroides abscessus` strain IDs that share `GTDB:s__Mycobacterium_abscessus` after the GTDB fan-out is fixed.

## Additional Notes

- The review used pinned local `data/raw/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `mycobacteroides_abscessus_subsp_massiliense_ccug_48898_jcm_15300` review.
