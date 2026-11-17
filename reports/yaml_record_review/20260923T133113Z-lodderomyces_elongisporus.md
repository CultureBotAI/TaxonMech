# YAML Record Review: Lodderomyces elongisporus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lodderomyces_elongisporus.yaml
- Started UTC: 2026-09-23T13:31:13Z
- Finished UTC: 2026-09-23T13:31:13Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lodderomyces_elongisporus.yaml` denotes the exact NCBI species `Lodderomyces elongisporus` as `NCBITaxon:36914`, rank `SPECIES`, under genus `NCBITaxon:36913` (`Lodderomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lodderomyces_elongisporus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_beijingensis.yaml data/taxa/eukaryota/lodderomyces_elongisporus.yaml data/taxa/eukaryota/lodderomyces_jiufengensis.yaml data/taxa/eukaryota/lodderomyces_metapsilosis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4187` carries `NCBITaxon:36914`, label `Lodderomyces elongisporus`, rank `SPECIES`, parent `NCBITaxon:36913`, genetic code `12`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lodderomyces` genus.
- The record preserves `Saccharomyces elongisporus` as an exact synonym and both authorship-bearing names as related synonyms from NCBI.
- `curation/seed_scope.tsv:52361` contains this identifier with reason `attested rule: Lodderomyces elongisporus, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:36914`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33542`, whose aggregate count is `1` for `NCBITaxon:36914`.
- The native GOLD scan found one exact organism for this NCBI ID, `Go0657879`, for strain `PH4014`.
- The native GOLD projects scan found one linked project, `Gp0702147`, and the native GOLD analyses scan found one row linked through that project ID.
- Exact StrainInfo scans found 23 direct strain rows and 52 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:196229` through `196246` contain 18 type-material spellings for `Saccharomyces elongisporus`, spanning `ATCC 11503`, `CBS 2605`, `NRRL YB-4239`, `BCRC:21390`, `CCRC 21390`, `DBVPG 6183`, `IFO 1676`, `JCM 1781`, and `NCYC 2649` variants. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:36914`, `just validate data/taxa/eukaryota/lodderomyces_elongisporus.yaml`, and `just validate-strict data/taxa/eukaryota/lodderomyces_elongisporus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lodderomyces_elongisporus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- `lodderomyces_beijingensis` was skipped during this batch because an existing exact pass report at `reports/yaml_record_review/20260922T003036Z-lodderomyces_beijingensis.md` already has all required sections.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
