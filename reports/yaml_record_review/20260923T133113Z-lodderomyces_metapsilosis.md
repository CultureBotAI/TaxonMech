# YAML Record Review: Lodderomyces metapsilosis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lodderomyces_metapsilosis.yaml
- Started UTC: 2026-09-23T13:31:13Z
- Finished UTC: 2026-09-23T13:31:13Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lodderomyces_metapsilosis.yaml` denotes the exact NCBI species `Lodderomyces metapsilosis` as `NCBITaxon:273372`, rank `SPECIES`, under genus `NCBITaxon:36913` (`Lodderomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lodderomyces_metapsilosis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_beijingensis.yaml data/taxa/eukaryota/lodderomyces_elongisporus.yaml data/taxa/eukaryota/lodderomyces_jiufengensis.yaml data/taxa/eukaryota/lodderomyces_metapsilosis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:56421` carries `NCBITaxon:273372`, label `Lodderomyces metapsilosis`, rank `SPECIES`, parent `NCBITaxon:36913`, genetic code `12`, two exact synonyms, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lodderomyces` genus.
- The record preserves `Candida metapsilosis` and `Candida parapsilosis group III` as exact synonyms and both authorship-bearing names as related synonyms from NCBI.
- `curation/seed_scope.tsv:54929` contains this identifier with reason `attested rule: Lodderomyces metapsilosis, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:273372`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:25490`, whose aggregate count is `2` for `NCBITaxon:273372`.
- The native GOLD scan found two exact organisms for this NCBI ID: `Go0631664` for strain `BP57` and `Go0705542` for strain `NRRL Y-48470`.
- The native GOLD projects scan found one linked project for each exact GOLD organism, and the native GOLD analyses scan found one row linked through project `Gp0645204`.
- Exact StrainInfo scans found 11 direct strain rows and 14 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:115348` through `115357` contain 10 type-material spellings for `Candida metapsilosis`, covering `CBS 10907` and `NRRL Y-48470` as cultures from holotype plus `ATCC 96144` as holotype. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:273372`, `just validate data/taxa/eukaryota/lodderomyces_metapsilosis.yaml`, and `just validate-strict data/taxa/eukaryota/lodderomyces_metapsilosis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lodderomyces_metapsilosis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- `lodderomyces_beijingensis` was skipped during this batch because an existing exact pass report at `reports/yaml_record_review/20260922T003036Z-lodderomyces_beijingensis.md` already has all required sections.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
