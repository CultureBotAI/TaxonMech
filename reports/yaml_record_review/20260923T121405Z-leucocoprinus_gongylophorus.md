# YAML Record Review: Leucocoprinus gongylophorus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml
- Started UTC: 2026-09-23T12:14:05Z
- Finished UTC: 2026-09-23T12:14:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml` denotes the exact NCBI species `Leucocoprinus gongylophorus` as `NCBITaxon:79220`, rank `SPECIES`, under genus `NCBITaxon:34431` (`Leucocoprinus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml data/taxa/eukaryota/leucocoprinus_leucothites.yaml data/taxa/eukaryota/leucocoprinus_nympharum.yaml data/taxa/eukaryota/leucogyrophana_mollusca.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:11629` carries `NCBITaxon:79220`, label `Leucocoprinus gongylophorus`, rank `SPECIES`, parent `NCBITaxon:34431`, genetic code `1`, four exact synonyms, four related synonyms, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leucocoprinus` genus.
- `curation/seed_scope.tsv:53335` contains this identifier with reason `attested rule: Leucocoprinus gongylophorus, 2 sources incl. NCBI`.
- The side NCBI merge scan found old IDs `NCBITaxon:1258663` and `NCBITaxon:462204` retired into `NCBITaxon:79220`; an ignored-inclusive `rg --no-ignore --hidden` search found no retained rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:42775`, whose aggregate count is `10` for `NCBITaxon:79220`.
- The current native GOLD expansion found 8 exact organism rows, 11 exact projects, and 2 exact native analysis rows for this NCBI ID.
- Exact StrainInfo scans found 1 direct strain and 1 deposit row for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:264754` contains one `epitype` row for `Rozites gongylophorus`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:79220`, `just validate data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml`, and `just validate-strict data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leucocoprinus_gongylophorus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
