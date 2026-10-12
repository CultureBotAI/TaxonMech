# YAML Record Review: Leptospira interrogans serovar Copenhageni str. 2006007831

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/leptospira_interrogans_serovar_copenhageni_str_2006007831.yaml`
- Started UTC: 2026-09-22T13:59:43Z
- Finished UTC: 2026-09-22T14:01:17Z
- Verdict: needs curation

## Target

- Record: `data/taxa/bacteria/leptospira_interrogans_serovar_copenhageni_str_2006007831.yaml`
- Identifier: `NCBITaxon:1001986`
- Slug: `leptospira_interrogans_serovar_copenhageni_str_2006007831`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:44275` (`Leptospira interrogans serovar Copenhageni`)

## Validation

- `just validate data/taxa/bacteria/leptospira_interrogans_serovar_copenhageni_str_2006007831.yaml`: passed.
- `just validate-strict data/taxa/bacteria/leptospira_interrogans_serovar_copenhageni_str_2006007831.yaml data/taxa/bacteria/leptospira_interrogans_serovar_copenhageni_str_2001025091.yaml data/taxa/bacteria/escherichia_coli_pcn009.yaml data/taxa/bacteria/escherichia_coli_pcn033.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001986` / `Leptospira interrogans serovar Copenhageni str. 2006007831`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:44275` matches the pinned NCBI parent, `Leptospira interrogans serovar Copenhageni`.
- The lineage stays within Bacteria through `Spirochaetota`, `Leptospiria`, `Leptospirales`, `Leptospiraceae`, `Leptospira`, `Leptospira interrogans`, then `Leptospira interrogans serovar Copenhageni`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The NCBI, GOLD, and MADIN attestations are keyed directly to `NCBITaxon:1001986`; their labels and assertion counts match the reviewed raw rows. The GTDB evidence is the species-level `GTDB:s__Leptospira_interrogans` mapping to `NCBITaxon:1001986` with `skos:closeMatch` and `genome_count: 556`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI, MADIN, GOLD, and GTDB rows keyed to `NCBITaxon:1001986`, and no ATB, BacDive, LPSN, or strain-info rows keyed to this identifier.

## Completeness

The NCBI-derived `Leptospira interrogans serovar Copenhageni strain 2006007831` synonym preserves the strain identifier and is consistent with the reviewed strain.

The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. The only questionable completeness item is the GTDB xref described below.

## Findings

### Major: Species-level GTDB evidence is attached to one NCBI strain

The `taxonomy_mappings` entry, `GTDB:s__Leptospira_interrogans` xref, GTDB `source_attestations` entry, and GTDB-derived `Leptospira interrogans` exact synonym all describe a GTDB species cluster with 556 genomes. The reviewed target is a single NCBI `STRAIN`, `Leptospira interrogans serovar Copenhageni str. 2006007831`; treating the GTDB species label as an exact synonym of this strain overstates equivalence.

## Recommended Edits

- Route the `GTDB:s__Leptospira_interrogans` mapping and 556-genome count to the species-level `NCBITaxon:173` record, or keep it off individual NCBI `STRAIN` records unless there is strain-specific GTDB evidence.
- Suppress the GTDB-derived exact synonym and `GTDB:s__Leptospira_interrogans` xref on `NCBITaxon:1001986`; keep the direct NCBITAXON, GOLD, and MADIN attestations.
- Add a regression check that prevents a GTDB `s__` cluster from being projected as an `EXACT_SYNONYM` or genome-count attestation onto a lower-rank NCBI strain target.

## Follow-up Checks

- Re-check adjacent `Leptospira interrogans` strain IDs that share `GTDB:s__Leptospira_interrogans` after the GTDB fan-out is fixed.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `leptospira_interrogans_serovar_copenhageni_str_2006007831` review.
