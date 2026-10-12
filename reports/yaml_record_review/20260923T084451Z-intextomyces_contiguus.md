# YAML Record Review: Intextomyces contiguus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/intextomyces_contiguus.yaml
- Started UTC: 2026-09-23T08:44:51Z
- Finished UTC: 2026-09-23T08:44:51Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/intextomyces_contiguus.yaml` denotes `Intextomyces contiguus` as `NCBITaxon:2789333`, rank `SPECIES`, under parent `NCBITaxon:2494167` (`Intextomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/intextomyces_contiguus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/intextomyces_contiguus.yaml data/taxa/eukaryota/ionaspis_alba.yaml data/taxa/eukaryota/irpex_flavus.yaml data/taxa/eukaryota/irpex_lacteus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:555404` carries `NCBITaxon:2789333`, label `Intextomyces contiguus`, rank `SPECIES`, parent `NCBITaxon:2494167`, genetic code `1`, exact synonym `Corticium calceum * contiguum`, and the two related synonyms emitted in YAML.
- The 11 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:63239` contains this identifier with reason `attested rule: Intextomyces contiguus, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:26583`, whose aggregate count is `2` for `NCBITaxon:2789333`.
- The current native GOLD organism scan found `Go0511048` and `Go0515931`, both for `Intextomyces contiguus OMC1699`, with projects `Gp0401102` and `Gp0436689`; no native analysis row joined to those projects.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:2789333`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2789333`, `just validate data/taxa/eukaryota/intextomyces_contiguus.yaml`, and `just validate-strict data/taxa/eukaryota/intextomyces_contiguus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `intextomyces_contiguus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
