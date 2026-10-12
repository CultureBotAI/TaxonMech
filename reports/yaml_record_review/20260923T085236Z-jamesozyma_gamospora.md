# YAML Record Review: Jamesozyma gamospora

- Repository: TaxonMech
- Record: data/taxa/eukaryota/jamesozyma_gamospora.yaml
- Started UTC: 2026-09-23T08:52:36Z
- Finished UTC: 2026-09-23T08:52:36Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/jamesozyma_gamospora.yaml` denotes the exact NCBI species `Jamesozyma gamospora` as `NCBITaxon:308752`, rank `SPECIES`, under genus `NCBITaxon:3162961` (`Jamesozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/jamesozyma_gamospora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/jaapia_argillacea.yaml data/taxa/eukaryota/jackrogersella_minutella.yaml data/taxa/eukaryota/jahnula_aquatica.yaml data/taxa/eukaryota/jamesozyma_gamospora.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:63151` carries `NCBITaxon:308752`, label `Jamesozyma gamospora`, rank `SPECIES`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Jamesozyma`.
- `curation/seed_scope.tsv:55117` contains this identifier with reason `attested rule: Jamesozyma gamospora, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:200336`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:31244`, whose aggregate count is `1` for `NCBITaxon:308752`.
- The current native GOLD scan found exact organism `Go0705569` for `Jamesozyma gamospora NRRL Y-48841`.
- Expanding that exact GOLD organism found project `Gp0831612`, with no native linked analysis rows.
- StrainInfo has 7 exact direct/deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 7 rows: `NBRC 11056` and `NBRC:11056` as cultures from holotype, plus `CBS 10328`, `CBS:10328`, `NRRL Y-48841`, `NRRL:Y-48841`, and `NRRL:Y:48841` as type material.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:308752`, `just validate data/taxa/eukaryota/jamesozyma_gamospora.yaml`, and `just validate-strict data/taxa/eukaryota/jamesozyma_gamospora.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `jamesozyma_gamospora` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
