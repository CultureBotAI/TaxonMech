# YAML Record Review: Lentinula lateritia

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lentinula_lateritia.yaml
- Started UTC: 2026-09-23T11:52:33Z
- Finished UTC: 2026-09-23T11:52:33Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lentinula_lateritia.yaml` denotes the exact NCBI species `Lentinula lateritia` as `NCBITaxon:40482`, rank `SPECIES`, under genus `NCBITaxon:5352` (`Lentinula`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lentinula_lateritia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lentinula_edodes.yaml data/taxa/eukaryota/lentinula_guzmanii.yaml data/taxa/eukaryota/lentinula_lateritia.yaml data/taxa/eukaryota/lentinula_novae_zelandiae.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4628` carries `NCBITaxon:40482`, label `Lentinula lateritia`, rank `SPECIES`, parent `NCBITaxon:5352`, genetic code `1`, exact synonym `Lentinus lateritius`, two related synonyms, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lentinula` genus.
- `curation/seed_scope.tsv:52440` contains this identifier with reason `attested rule: Lentinula lateritia, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:40482`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:34563`, whose aggregate count is `3` for `NCBITaxon:40482`.
- The current native GOLD scan found three exact organisms, four linked native GOLD projects, and two linked native GOLD analysis rows.
- Exact StrainInfo scans found one direct strain and one deposit row for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:204546` and `:204547` contain holotype spellings `K(M) 34272` and `K(M):34272` for `NCBITaxon:40482`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:40482`, `just validate data/taxa/eukaryota/lentinula_lateritia.yaml`, and `just validate-strict data/taxa/eukaryota/lentinula_lateritia.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lentinula_lateritia` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
