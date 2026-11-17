# YAML Record Review: Lichtheimia hyalospora

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lichtheimia_hyalospora.yaml
- Started UTC: 2026-09-23T12:31:10Z
- Finished UTC: 2026-09-23T12:31:10Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lichtheimia_hyalospora.yaml` denotes the exact NCBI species `Lichtheimia hyalospora` as `NCBITaxon:420593`, rank `SPECIES`, under genus `NCBITaxon:688353` (`Lichtheimia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lichtheimia_hyalospora.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lichtheimia_hyalospora.yaml data/taxa/eukaryota/lichtheimia_ramosa.yaml data/taxa/eukaryota/lichtheimia_ramosa_b5792.yaml data/taxa/eukaryota/lichtheimia_sphaerocystis.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:92254` carries `NCBITaxon:420593`, label `Lichtheimia hyalospora`, rank `SPECIES`, parent `NCBITaxon:688353`, genetic code `1`, three exact synonyms, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lichtheimia` genus.
- `curation/seed_scope.tsv:55603` contains this identifier with reason `attested rule: Lichtheimia hyalospora, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:420593`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:35055`, whose aggregate count is `4` for `NCBITaxon:420593`.
- The current native GOLD expansion found three exact organism rows, four exact projects, and one native analysis row linked through `AP PROJECT GOLD IDS`.
- Exact StrainInfo scans found 6 direct strains and 15 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:207860` through `207863` contain four culture-from-neotype spellings for `Tieghemella hyalospora`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:420593`, `just validate data/taxa/eukaryota/lichtheimia_hyalospora.yaml`, and `just validate-strict data/taxa/eukaryota/lichtheimia_hyalospora.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lichtheimia_hyalospora` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
