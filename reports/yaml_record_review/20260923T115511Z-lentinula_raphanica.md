# YAML Record Review: Lentinula raphanica

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lentinula_raphanica.yaml
- Started UTC: 2026-09-23T11:55:11Z
- Finished UTC: 2026-09-23T11:55:11Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lentinula_raphanica.yaml` denotes the exact NCBI species `Lentinula raphanica` as `NCBITaxon:153919`, rank `SPECIES`, under genus `NCBITaxon:5352` (`Lentinula`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lentinula_raphanica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lentinula_raphanica.yaml data/taxa/eukaryota/lentinus_brumalis.yaml data/taxa/eukaryota/lentinus_crinitus.yaml data/taxa/eukaryota/lentinus_levis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:32071` carries `NCBITaxon:153919`, label `Lentinula raphanica`, rank `SPECIES`, parent `NCBITaxon:5352`, genetic code `1`, exact synonym `Armillaria raphanica`, two related synonyms, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lentinula` genus.
- `curation/seed_scope.tsv:54099` contains this identifier with reason `attested rule: Lentinula raphanica, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:153919`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:12250`, whose aggregate count is `6` for `NCBITaxon:153919`.
- A complete current native GOLD pass found six exact organism rows, eleven exact linked project rows, and three exact linked analysis rows for this NCBI ID.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:40740` and `:40741` contain lectotype spellings `TENN 16075` and `TENN:16075` for `NCBITaxon:153919`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:153919`, `just validate data/taxa/eukaryota/lentinula_raphanica.yaml`, and `just validate-strict data/taxa/eukaryota/lentinula_raphanica.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lentinula_raphanica` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
