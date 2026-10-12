# YAML Record Review: Insectozyma bohioensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/insectozyma_bohioensis.yaml
- Started UTC: 2026-09-23T08:36:54Z
- Finished UTC: 2026-09-23T08:36:54Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/insectozyma_bohioensis.yaml` denotes `Insectozyma bohioensis` as `NCBITaxon:561986`, rank `SPECIES`, under parent `NCBITaxon:3712553` (`Insectozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/insectozyma_bohioensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/inocybe_lacera.yaml data/taxa/eukaryota/inosperma_lanatodiscum.yaml data/taxa/eukaryota/insectozyma_bohioensis.yaml data/taxa/eukaryota/insectozyma_chauliodis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:131870` carries `NCBITaxon:561986`, label `Insectozyma bohioensis`, rank `SPECIES`, parent `NCBITaxon:3712553`, genetic code `12`, exact synonym `Candida bohioensis S.-O. Suh, N. H. Nguyen & M. Blackwell, 2008`, and the three related synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:56039` contains this identifier with reason `attested rule: Insectozyma bohioensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has side old IDs `NCBITaxon:271360` and `NCBITaxon:271364` merged into this target, but no retained retired `ncbitaxon_taxa` row exists, so omitting `replaces` is expected.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38867`, whose aggregate count is `1` for `NCBITaxon:561986`.
- The current native GOLD organism scan found exact organism `Go0705489` for `Candida bohioensis NRRL Y-27737`, with project `Gp0831532`; no native analysis row joined to that project.
- Exact `data/raw/ncbi_type_material.tsv` rows 235652-235664 record 13 `Candida bohioensis` type-material designations for `ATCC MYA-4363`, `NRRL Y-27737`, and `CBS 9897` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:561986`, `just validate data/taxa/eukaryota/insectozyma_bohioensis.yaml`, and `just validate-strict data/taxa/eukaryota/insectozyma_bohioensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `insectozyma_bohioensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
