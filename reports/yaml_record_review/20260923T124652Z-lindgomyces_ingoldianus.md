# YAML Record Review: Lindgomyces ingoldianus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lindgomyces_ingoldianus.yaml
- Started UTC: 2026-09-23T12:46:52Z
- Finished UTC: 2026-09-23T12:46:52Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lindgomyces_ingoldianus.yaml` denotes the exact NCBI species `Lindgomyces ingoldianus` as `NCBITaxon:673940`, rank `SPECIES`, under genus `NCBITaxon:741162` (`Lindgomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lindgomyces_ingoldianus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lindgomyces_ingoldianus.yaml data/taxa/eukaryota/lindgomyces_madisonensis.yaml data/taxa/eukaryota/lindriella_thalassiae.yaml data/taxa/eukaryota/lineolata_rhizophorae.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:156572` carries `NCBITaxon:673940`, label `Lindgomyces ingoldianus`, rank `SPECIES`, parent `NCBITaxon:741162`, genetic code `1`, three exact synonyms, five related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lindgomyces` genus.
- `curation/seed_scope.tsv:56365` contains this identifier with reason `attested rule: Lindgomyces ingoldianus, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:673941` retired into `NCBITaxon:673940`; an ignored-inclusive `rg --no-ignore --hidden` search found no retained row for that old ID in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:41036`, whose aggregate count is `1` for `NCBITaxon:673940`.
- The current native GOLD scan found one exact organism row, two exact projects, and no native analysis rows for this NCBI ID.
- Exact StrainInfo scans found 2 direct strains and 2 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:253292` through `253295` contain four holotype-related spellings for `Massarina ingoldiana`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:673940`, `just validate data/taxa/eukaryota/lindgomyces_ingoldianus.yaml`, and `just validate-strict data/taxa/eukaryota/lindgomyces_ingoldianus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lindgomyces_ingoldianus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
