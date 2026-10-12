# YAML Record Review: Lindgomyces carolinensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lindgomyces_carolinensis.yaml
- Started UTC: 2026-09-23T12:42:29Z
- Finished UTC: 2026-09-23T12:42:29Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lindgomyces_carolinensis.yaml` denotes the exact NCBI species `Lindgomyces carolinensis` as `NCBITaxon:1972648`, rank `SPECIES`, under genus `NCBITaxon:741162` (`Lindgomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lindgomyces_carolinensis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/linderina_macrospora.yaml data/taxa/eukaryota/linderina_pennispora.yaml data/taxa/eukaryota/lindgomyces_carolinensis.yaml data/taxa/eukaryota/lindgomyces_cigarospora.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:506267` carries `NCBITaxon:1972648`, label `Lindgomyces carolinensis`, rank `SPECIES`, parent `NCBITaxon:741162`, genetic code `1`, one related synonym, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lindgomyces` genus.
- `curation/seed_scope.tsv:61780` contains this identifier with reason `attested rule: Lindgomyces carolinensis, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:1972648`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:18218`, whose aggregate count is `2` for `NCBITaxon:1972648`.
- The current native GOLD scan found two exact organism rows, with no linked project or analysis rows in the compressed GOLD files.
- Exact StrainInfo scans found one direct strain and one deposit row for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:75902` and `75903` contain two culture-from-holotype spellings for `Lindgomyces carolinensis`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:1972648`, `just validate data/taxa/eukaryota/lindgomyces_carolinensis.yaml`, and `just validate-strict data/taxa/eukaryota/lindgomyces_carolinensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lindgomyces_carolinensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
