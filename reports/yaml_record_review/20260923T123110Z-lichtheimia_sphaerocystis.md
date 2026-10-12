# YAML Record Review: Lichtheimia sphaerocystis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lichtheimia_sphaerocystis.yaml
- Started UTC: 2026-09-23T12:31:10Z
- Finished UTC: 2026-09-23T12:31:10Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lichtheimia_sphaerocystis.yaml` denotes the exact NCBI species `Lichtheimia sphaerocystis` as `NCBITaxon:688662`, rank `SPECIES`, under genus `NCBITaxon:688353` (`Lichtheimia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lichtheimia_sphaerocystis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lichtheimia_hyalospora.yaml data/taxa/eukaryota/lichtheimia_ramosa.yaml data/taxa/eukaryota/lichtheimia_ramosa_b5792.yaml data/taxa/eukaryota/lichtheimia_sphaerocystis.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:161759` carries `NCBITaxon:688662`, label `Lichtheimia sphaerocystis`, rank `SPECIES`, parent `NCBITaxon:688353`, genetic code `1`, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lichtheimia` genus.
- `curation/seed_scope.tsv:56398` contains this identifier with reason `attested rule: Lichtheimia sphaerocystis, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:688662`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:41372`, whose aggregate count is `1` for `NCBITaxon:688662`.
- The current native GOLD expansion found one exact organism row and one exact project, with no native analysis rows for this NCBI ID.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID, and the generated raw strain and StrainInfo overlay tables likewise have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:256992` through `256995` contain four culture-from-type-material spellings for `Lichtheimia sphaerocystis`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:688662`, `just validate data/taxa/eukaryota/lichtheimia_sphaerocystis.yaml`, and `just validate-strict data/taxa/eukaryota/lichtheimia_sphaerocystis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lichtheimia_sphaerocystis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
