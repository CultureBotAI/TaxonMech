# YAML Record Review: Nitrosarchaeum koreense MY1

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/archaea/nitrosarchaeum_koreense_my1.yaml`
- Started UTC: 2026-09-22T14:02:18Z
- Finished UTC: 2026-09-22T14:04:00Z
- Verdict: needs curation

## Target

- Record: `data/taxa/archaea/nitrosarchaeum_koreense_my1.yaml`
- Identifier: `NCBITaxon:1001994`
- Slug: `nitrosarchaeum_koreense_my1`
- Rank: `STRAIN`
- Domain: `ARCHAEA`
- Parent: `NCBITaxon:1088740` (`Nitrosarchaeum koreense`)

## Validation

- `just validate data/taxa/archaea/nitrosarchaeum_koreense_my1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/escherichia_coli_pcn042.yaml data/taxa/bacteria/escherichia_coli_pcn079.yaml data/taxa/bacteria/escherichia_coli_pcn097.yaml data/taxa/archaea/nitrosarchaeum_koreense_my1.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001994` / `Nitrosarchaeum koreense MY1`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:1088740` matches the pinned NCBI parent, `Nitrosarchaeum koreense`.
- The lineage stays within Archaea through `Thermoproteati`, `Nitrososphaerota`, `Nitrososphaeria`, `Nitrosopumilales`, `Nitrosopumilaceae`, `Nitrosarchaeum`, then `Nitrosarchaeum koreense`.
- `grounding_status: EXACT` is correct for the NCBI strain seed itself.

## Evidence

The NCBI, GOLD, and MADIN attestations are keyed directly to `NCBITaxon:1001994`; their labels and assertion counts match the reviewed raw rows. The GTDB evidence is the species-level `GTDB:s__Nitrosarchaeum_koreense` mapping to `NCBITaxon:1001994` with `skos:closeMatch` and `genome_count: 2`.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI, MADIN, GOLD, and GTDB rows keyed to `NCBITaxon:1001994`, BacDive-derived assembly and genome inventory rows for `kgmicrobe.strain:bacdive_159828`, and no ATB, LPSN, or strain-info rows keyed to this identifier.

## Completeness

The NCBI-derived `Candidatus Nitrosoarchaeum koreensis MY1` and `Nitrosopumilus sp. MY1` synonyms preserve the strain identifier and are consistent with the reviewed strain.

The BacDive strain row for `kgmicrobe.strain:bacdive_159828` is keyed to the parent species `NCBITaxon:1088740`, while only its downstream assembly and genome inventory rows carry this strain's `NCBITaxon:1001994` identifier. The record has no `strains`, `equivalent_identifiers`, `comments`, or product-level sections. The only questionable completeness item is the GTDB xref described below.

## Findings

### Major: Species-level GTDB evidence is attached to one NCBI strain

The `taxonomy_mappings` entry, `GTDB:s__Nitrosarchaeum_koreense` xref, GTDB `source_attestations` entry, and GTDB-derived `Nitrosarchaeum koreense` exact synonym all describe a GTDB species cluster with two genomes. The reviewed target is a single NCBI `STRAIN`, `Nitrosarchaeum koreense MY1`; treating the GTDB species label as an exact synonym of this strain overstates equivalence.

## Recommended Edits

- Route the `GTDB:s__Nitrosarchaeum_koreense` mapping and two-genome count to the species-level `NCBITaxon:1088740` record, or keep it off individual NCBI `STRAIN` records unless there is strain-specific GTDB evidence.
- Suppress the GTDB-derived exact synonym and `GTDB:s__Nitrosarchaeum_koreense` xref on `NCBITaxon:1001994`; keep the direct NCBITAXON, GOLD, and MADIN attestations.
- Add a regression check that prevents a GTDB `s__` cluster from being projected as an `EXACT_SYNONYM` or genome-count attestation onto a lower-rank NCBI strain target.

## Follow-up Checks

- Re-check adjacent `Nitrosarchaeum koreense` strain IDs that share `GTDB:s__Nitrosarchaeum_koreense` after the GTDB fan-out is fixed.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- The broad `find data/taxa -maxdepth 2 -name 'nitrosarchaeum_koreense_my1.yaml'` lookup was interrupted after the Archaea path was resolved directly.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `nitrosarchaeum_koreense_my1` review.
