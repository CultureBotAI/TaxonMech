# YAML Record Review: [Lipomyces] yamanashiensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_yamanashiensis.yaml
- Started UTC: 2026-09-23T13:20:52Z
- Finished UTC: 2026-09-23T13:20:52Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_yamanashiensis.yaml` denotes the exact NCBI species `[Lipomyces] yamanashiensis` as `NCBITaxon:1930691`, rank `SPECIES`, under genus `NCBITaxon:54096` (`Myxozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_yamanashiensis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lipomyces_yamadae.yaml data/taxa/eukaryota/lipomyces_yamanashiensis.yaml data/taxa/eukaryota/lipomyces_yarrowii.yaml data/taxa/eukaryota/lithodesmium_intricatum.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:496264` carries `NCBITaxon:1930691`, label `[Lipomyces] yamanashiensis`, rank `SPECIES`, parent `NCBITaxon:54096`, genetic code `1`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Myxozyma` genus.
- The record preserves `Lipomyces yamanashiensis` as an exact synonym and `Lipomyces sp. YAM` plus the authorship-bearing `Lipomyces yamanashiensis` name as related synonyms from NCBI.
- `curation/seed_scope.tsv:61645` contains this identifier with reason `attested rule: [Lipomyces] yamanashiensis, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:1930691`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:17699`, whose aggregate count is `1` for `NCBITaxon:1930691`.
- The native GOLD scan found one exact organism for this NCBI ID, `Go0705110`, for strain `CBS 14748`.
- The native GOLD projects scan found one linked project, `Gp0831132`, and no analyses linked through that project ID.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:72462` through `72466` contain five type-material spellings for `Lipomyces yamanashiensis`, covering `CBS 14748` as culture from holotype, `NBRC 110621` as holotype, and `No313` as type material. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1930691`, `just validate data/taxa/eukaryota/lipomyces_yamanashiensis.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_yamanashiensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_yamanashiensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- `lithodesmium_intricatum` was skipped during this batch because an existing exact pass report at `reports/yaml_record_review/20260922T161721Z-lithodesmium_intricatum.md` already has all required sections.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
