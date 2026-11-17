# YAML Record Review: Insectozyma chauliodis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/insectozyma_chauliodis.yaml
- Started UTC: 2026-09-23T08:36:54Z
- Finished UTC: 2026-09-23T08:36:54Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/insectozyma_chauliodis.yaml` denotes `Insectozyma chauliodis` as `NCBITaxon:391825`, rank `SPECIES`, under parent `NCBITaxon:3712553` (`Insectozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/insectozyma_chauliodis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/inocybe_lacera.yaml data/taxa/eukaryota/inosperma_lanatodiscum.yaml data/taxa/eukaryota/insectozyma_bohioensis.yaml data/taxa/eukaryota/insectozyma_chauliodis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:83041` carries `NCBITaxon:391825`, label `Insectozyma chauliodis`, rank `SPECIES`, parent `NCBITaxon:3712553`, genetic code `12`, exact synonym `Candida chauliodis N.H. Nguyen, S.O. Suh & M. Blackw., 2008`, and the two related synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:55480` contains this identifier with reason `attested rule: Insectozyma chauliodis, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:34122`, whose aggregate count is `1` for `NCBITaxon:391825`.
- The current native GOLD organism scan found exact organism `Go0705504` for `Candida chauliodis NRRL Y-27909`, with project `Gp0831547`; no native analysis row joined to that project.
- Exact `data/raw/ncbi_type_material.tsv` rows 201574-201587 record 14 `Candida chauliodis` type-material designations for `ATCC MYA-4356`, `CBS 10157`, `IY 03-5-30-1-C`, and `NRRL Y-27909` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:391825`, `just validate data/taxa/eukaryota/insectozyma_chauliodis.yaml`, and `just validate-strict data/taxa/eukaryota/insectozyma_chauliodis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `insectozyma_chauliodis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
