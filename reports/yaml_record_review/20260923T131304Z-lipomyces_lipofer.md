# YAML Record Review: Lipomyces lipofer

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_lipofer.yaml
- Started UTC: 2026-09-23T13:13:04Z
- Finished UTC: 2026-09-23T13:13:04Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_lipofer.yaml` denotes the exact NCBI species `Lipomyces lipofer` as `NCBITaxon:36043`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_lipofer.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lipomyces_lipofer.yaml data/taxa/eukaryota/lipomyces_mesembrius.yaml data/taxa/eukaryota/lipomyces_oligophaga.yaml data/taxa/eukaryota/lipomyces_orientalis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4049` carries `NCBITaxon:36043`, label `Lipomyces lipofer`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, four exact synonyms, three related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves `Cryptococcus lipoferus`, the authorship-bearing `Lipomyces lipofer` name, `Torula lipofera`, and `Waltomyces lipofer` as exact synonyms plus three authorship-bearing names as related synonyms from NCBI.
- `curation/seed_scope.tsv:52317` contains this identifier with reason `attested rule: Lipomyces lipofer, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:36043`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33264`, whose aggregate count is `6` for `NCBITaxon:36043`.
- The full native GOLD organism scan found six exact organisms for this NCBI ID: `Go0517139`, `Go0608137`, `Go0608138`, `Go0608139`, `Go0608140`, and `Go0608141`.
- The native GOLD projects scan found one linked project, `Gp0441177`, for `Go0517139`. The native GOLD analyses scan found one row linked through that project ID.
- Exact StrainInfo scans found 16 direct strain rows and 63 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:193833` through `193853` contain 21 type-material spellings for `Lipomyces lipofer`, spanning `ATCC 32031`, `CBS 944`, `IFO 1288`, `JCM 3769`, `MUCL 39416`, `NCYC 2591`, `NRRL Y-11555`, `NRRL Y-2542`, and `VKM Y-218` variants. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:36043`, `just validate data/taxa/eukaryota/lipomyces_lipofer.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_lipofer.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_lipofer` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
