# YAML Record Review: Inosperma lanatodiscum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/inosperma_lanatodiscum.yaml
- Started UTC: 2026-09-23T08:36:54Z
- Finished UTC: 2026-09-23T08:36:54Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/inosperma_lanatodiscum.yaml` denotes `Inosperma lanatodiscum` as `NCBITaxon:239124`, rank `SPECIES`, under parent `NCBITaxon:2708298` (`Inosperma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/inosperma_lanatodiscum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/inocybe_lacera.yaml data/taxa/eukaryota/inosperma_lanatodiscum.yaml data/taxa/eukaryota/insectozyma_bohioensis.yaml data/taxa/eukaryota/insectozyma_chauliodis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:46949` carries `NCBITaxon:239124`, label `Inosperma lanatodiscum`, rank `SPECIES`, parent `NCBITaxon:2708298`, genetic code `1`, exact synonym `Inocybe lanatodisca`, and the two related authority-bearing synonyms emitted in YAML.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:54692` contains this identifier with reason `attested rule: Inosperma lanatodiscum, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:21968`, whose aggregate count is `1` for `NCBITaxon:239124`.
- The current native GOLD organism scan found exact organism `Go0532374` for `Inocybe lanatodisca 2018PMI007`, with projects `Gp0478824` and `Gp0484075`; no native analysis row joined to those projects.
- Exact `data/raw/ncbi_type_material.tsv` rows record `MICH11069` and `MICH:11069` as holotype designations, plus `F0004525C` and `F:0004525C` as type-material designations, under synonym label `Inocybe lanatodisca`.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:239124`, `just validate data/taxa/eukaryota/inosperma_lanatodiscum.yaml`, and `just validate-strict data/taxa/eukaryota/inosperma_lanatodiscum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `inosperma_lanatodiscum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
