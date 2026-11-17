# YAML Record Review: Lichtheimia corymbifera

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lichtheimia_corymbifera.yaml
- Started UTC: 2026-09-23T12:26:26Z
- Finished UTC: 2026-09-23T12:26:26Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lichtheimia_corymbifera.yaml` denotes the exact NCBI species `Lichtheimia corymbifera` as `NCBITaxon:42458`, rank `SPECIES`, under genus `NCBITaxon:688353` (`Lichtheimia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lichtheimia_corymbifera.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lichenoconium_lecanorae.yaml data/taxa/eukaryota/lichenostigmatales_sp.yaml data/taxa/eukaryota/lichtheimia_blakesleeana.yaml data/taxa/eukaryota/lichtheimia_corymbifera.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5010` carries `NCBITaxon:42458`, label `Lichtheimia corymbifera`, rank `SPECIES`, parent `NCBITaxon:688353`, genetic code `1`, four exact synonyms, four related synonyms, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lichtheimia` genus.
- `curation/seed_scope.tsv:52523` contains this identifier with reason `attested rule: Lichtheimia corymbifera, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:2231641` retired into `NCBITaxon:42458`; an ignored-inclusive `rg --no-ignore --hidden` search found no retained row for that old ID in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:35145`, whose aggregate count is `30` for `NCBITaxon:42458`.
- The current native GOLD expansion found 29 exact organism rows, 29 exact projects, and two native analysis rows linked through `AP PROJECT GOLD IDS`.
- Exact StrainInfo scans found 154 direct strains and 228 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:208589` and `208590` contain two culture-from-neotype spellings for `Mucor corymbifer`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:42458`, `just validate data/taxa/eukaryota/lichtheimia_corymbifera.yaml`, and `just validate-strict data/taxa/eukaryota/lichtheimia_corymbifera.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lichtheimia_corymbifera` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
