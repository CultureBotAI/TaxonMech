# YAML Record Review: Lipomyces yarrowii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_yarrowii.yaml
- Started UTC: 2026-09-23T13:20:52Z
- Finished UTC: 2026-09-23T13:20:52Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_yarrowii.yaml` denotes the exact NCBI species `Lipomyces yarrowii` as `NCBITaxon:1125752`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_yarrowii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lipomyces_yamadae.yaml data/taxa/eukaryota/lipomyces_yamanashiensis.yaml data/taxa/eukaryota/lipomyces_yarrowii.yaml data/taxa/eukaryota/lithodesmium_intricatum.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:244151` carries `NCBITaxon:1125752`, label `Lipomyces yarrowii`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves `Lipomyces Cluster A strain A1` as an exact synonym and `Lipomyces sp. 'CBS7557'` plus the authorship-bearing `Lipomyces yarrowii` name as related synonyms from NCBI.
- `curation/seed_scope.tsv:57761` contains this identifier with reason `attested rule: Lipomyces yarrowii, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:56814` for `NCBITaxon:1125752`, but it was not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`; this matches the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:2511`, whose aggregate count is `1` for `NCBITaxon:1125752`.
- The native GOLD scan found one exact organism for this NCBI ID, `Go0583996`, for strain `CBS 7557`.
- The native GOLD projects scan found one linked transcriptome project, `Gp0595916`, and no analyses linked through that project ID.
- Exact StrainInfo scans found one direct strain row and five deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:7823` through `7826` contain four type-material spellings for `Lipomyces yarrowii`, covering `CBS 7557` as culture from type material and `MUCL 39422` as type material. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:1125752`, `just validate data/taxa/eukaryota/lipomyces_yarrowii.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_yarrowii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_yarrowii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- `lithodesmium_intricatum` was skipped during this batch because an existing exact pass report at `reports/yaml_record_review/20260922T161721Z-lithodesmium_intricatum.md` already has all required sections.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
