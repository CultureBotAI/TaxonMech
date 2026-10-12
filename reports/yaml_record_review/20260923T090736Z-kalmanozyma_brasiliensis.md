# YAML Record Review: Kalmanozyma brasiliensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kalmanozyma_brasiliensis.yaml
- Started UTC: 2026-09-23T09:07:36Z
- Finished UTC: 2026-09-23T09:07:36Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kalmanozyma_brasiliensis.yaml` denotes the exact NCBI species `Kalmanozyma brasiliensis` as `NCBITaxon:1392244`, rank `SPECIES`, under genus `NCBITaxon:1804794` (`Kalmanozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kalmanozyma_brasiliensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kalmanozyma_brasiliensis.yaml data/taxa/eukaryota/kappamyces_sp.yaml data/taxa/eukaryota/kappaphycus_alvarezii.yaml data/taxa/eukaryota/karenia_brevis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:341657` carries `NCBITaxon:1392244`, label `Kalmanozyma brasiliensis`, rank `SPECIES`, parent `NCBITaxon:1804794`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kalmanozyma`.
- `curation/seed_scope.tsv:59833` contains this identifier with reason `attested rule: Kalmanozyma brasiliensis, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:9280`, whose aggregate count is `1` for `NCBITaxon:1392244`.
- The current native GOLD scan found exact organism `Go0070930` for `Kalmanozyma brasiliensis GHG001` and project `Gp0070930`.
- The native GOLD analysis scan found one exact linked analysis, `Kalmanozyma brasiliensis GHG001`, through project `Gp0070930`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 8 rows for `NCBITaxon:1392244` at lines 28007-28014: `CBMAI 1606`, `CBS 13268`, and `UFMG-CM-Y307` cultures from holotype, plus `GHG001` holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1392244`, `just validate data/taxa/eukaryota/kalmanozyma_brasiliensis.yaml`, and `just validate-strict data/taxa/eukaryota/kalmanozyma_brasiliensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kalmanozyma_brasiliensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
