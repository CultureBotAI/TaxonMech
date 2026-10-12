# YAML Record Review: Lipomyces kockii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_kockii.yaml
- Started UTC: 2026-09-23T13:08:27Z
- Finished UTC: 2026-09-23T13:08:27Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_kockii.yaml` denotes the exact NCBI species `Lipomyces kockii` as `NCBITaxon:383835`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_kockii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lipomyces_doorenjongii.yaml data/taxa/eukaryota/lipomyces_japonicus.yaml data/taxa/eukaryota/lipomyces_kockii.yaml data/taxa/eukaryota/lipomyces_kononenkoae.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:80591` carries `NCBITaxon:383835`, label `Lipomyces kockii`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves `Lipomyces starkeyi g` as an exact synonym and `Lipomyces kockii Van der Walt & M.T. Sm., 1999` plus `Lipomyces sp. 'CBS7729'` as related synonyms from NCBI.
- `curation/seed_scope.tsv:55451` contains this identifier with reason `attested rule: Lipomyces kockii, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:56876` for `NCBITaxon:383835`, but it was not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`; this matches the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33969`, whose aggregate count is `1` for `NCBITaxon:383835`.
- The native GOLD scan found one exact organism for this NCBI ID, `Go0705436`, for strain `NRRL Y-27505`, and one linked project, `Gp0831479`.
- The native GOLD analyses scan found no rows linked through the exact project ID.
- Exact StrainInfo scans found six direct strain rows and 11 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:200484` through `200490` contain seven type-material spellings for `Lipomyces kockii`, covering `CBS 7729` as culture from holotype and `MUCL 39421` plus `NRRL Y-27505` as type material. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:383835`, `just validate data/taxa/eukaryota/lipomyces_kockii.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_kockii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_kockii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
