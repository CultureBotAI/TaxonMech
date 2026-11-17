# YAML Record Review: Leucocoprinus nympharum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leucocoprinus_nympharum.yaml
- Started UTC: 2026-09-23T12:14:05Z
- Finished UTC: 2026-09-23T12:14:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leucocoprinus_nympharum.yaml` denotes the exact NCBI species `Leucocoprinus nympharum` as `NCBITaxon:201220`, rank `SPECIES`, under genus `NCBITaxon:34431` (`Leucocoprinus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leucocoprinus_nympharum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml data/taxa/eukaryota/leucocoprinus_leucothites.yaml data/taxa/eukaryota/leucocoprinus_nympharum.yaml data/taxa/eukaryota/leucogyrophana_mollusca.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:39781` carries `NCBITaxon:201220`, label `Leucocoprinus nympharum`, rank `SPECIES`, parent `NCBITaxon:34431`, genetic code `1`, exact synonyms `Agaricus nympharum` and `Leucoagaricus nympharum`, three related synonyms, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leucocoprinus` genus.
- `curation/seed_scope.tsv:54454` contains this identifier with reason `attested rule: Leucocoprinus nympharum, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:18582`, whose aggregate count is `1` for `NCBITaxon:201220`.
- The current native GOLD scan found no exact organism, project, or analysis rows for this NCBI ID.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- The NCBI type-material scan found 0 rows for this taxon, matching the absence of type-material-specific output in the generated record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:201220`, `just validate data/taxa/eukaryota/leucocoprinus_nympharum.yaml`, and `just validate-strict data/taxa/eukaryota/leucocoprinus_nympharum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leucocoprinus_nympharum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
