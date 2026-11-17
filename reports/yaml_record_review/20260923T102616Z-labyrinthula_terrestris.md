# YAML Record Review: Labyrinthula terrestris

- Repository: TaxonMech
- Record: data/taxa/eukaryota/labyrinthula_terrestris.yaml
- Started UTC: 2026-09-23T10:26:16Z
- Finished UTC: 2026-09-23T10:26:16Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/labyrinthula_terrestris.yaml` denotes the exact NCBI species `Labyrinthula terrestris` as `NCBITaxon:382652`, rank `SPECIES`, under genus `NCBITaxon:35133` (`Labyrinthula`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/labyrinthula_terrestris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kwoniella_dendrophila_cbs_6074.yaml data/taxa/eukaryota/kwoniella_sp_b9012.yaml data/taxa/eukaryota/labyrinthula_terrestris.yaml data/taxa/eukaryota/lacazia_loboi.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:80408` carries `NCBITaxon:382652`, label `Labyrinthula terrestris`, rank `SPECIES`, parent `NCBITaxon:35133`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 10 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Labyrinthula`.
- `curation/seed_scope.tsv:55448` contains this identifier with reason `attested rule: Labyrinthula terrestris, 2 sources incl. NCBI`.
- The local NCBI merge side inventory has no old IDs for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33934`, whose aggregate count is `2` for `NCBITaxon:382652`.
- The current native GOLD scan found exact organism `Go0008775` for `Labyrinthula terrestris ATCC MYA-3074`, with no native linked project or analysis rows.
- Exact StrainInfo scans found one direct strain and one deposit for this taxon; exact BacDive and generated raw strain-table scans found no corresponding local BacDive-derived strain rows to overlay.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 rows for `NCBITaxon:382652` at lines 199973-199976, covering `ATCC MYA-3074` culture-from-holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:382652`, `just validate data/taxa/eukaryota/labyrinthula_terrestris.yaml`, and `just validate-strict data/taxa/eukaryota/labyrinthula_terrestris.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `labyrinthula_terrestris` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact rows are side evidence only and can differ from the retained aggregate used to generate source attestations.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
