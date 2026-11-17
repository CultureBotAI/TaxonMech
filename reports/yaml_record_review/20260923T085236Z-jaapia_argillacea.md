# YAML Record Review: Jaapia argillacea

- Repository: TaxonMech
- Record: data/taxa/eukaryota/jaapia_argillacea.yaml
- Started UTC: 2026-09-23T08:52:36Z
- Finished UTC: 2026-09-23T08:52:36Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/jaapia_argillacea.yaml` denotes the exact NCBI species `Jaapia argillacea` as `NCBITaxon:202697`, rank `SPECIES`, under genus `NCBITaxon:202696` (`Jaapia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/jaapia_argillacea.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/jaapia_argillacea.yaml data/taxa/eukaryota/jackrogersella_minutella.yaml data/taxa/eukaryota/jahnula_aquatica.yaml data/taxa/eukaryota/jamesozyma_gamospora.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:39989` carries `NCBITaxon:202697`, label `Jaapia argillacea`, rank `SPECIES`, genetic code `1`, and the NCBI synonym retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Jaapia`.
- `curation/seed_scope.tsv:54465` contains this identifier with reason `attested rule: Jaapia argillacea, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:19076`, whose aggregate count is `1` for `NCBITaxon:202697`.
- The current native GOLD scan found exact organism `Go0012165` for `Jaapia argillacea MUCL 33604`.
- Expanding that exact GOLD organism found projects `Gp0009596`, `Gp0012165`, `Gp0667027`, `Gp0667028`, `Gp0667029`, `Gp0667031`, and `Gp0667032`.
- The native GOLD analysis scan found one exact linked analysis, `Jaapia argillacea MUCL 33604`, through project `Gp0012165`.
- StrainInfo has 5 exact direct/deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 2 rows, `CBS 252.74` and `CBS:252.74`, both marked as reference material.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:202697`, `just validate data/taxa/eukaryota/jaapia_argillacea.yaml`, and `just validate-strict data/taxa/eukaryota/jaapia_argillacea.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `jaapia_argillacea` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
