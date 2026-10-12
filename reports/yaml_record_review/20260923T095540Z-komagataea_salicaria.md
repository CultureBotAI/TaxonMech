# YAML Record Review: Komagataea salicaria

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataea_salicaria.yaml
- Started UTC: 2026-09-23T09:55:40Z
- Finished UTC: 2026-09-23T09:55:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/komagataea_salicaria.yaml` denotes the exact NCBI species `Komagataea salicaria` as `NCBITaxon:1337058`, rank `SPECIES`, under genus `NCBITaxon:3712926` (`Komagataea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataea_salicaria.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/komagataea_pratensis.yaml data/taxa/eukaryota/komagataea_qinlingensis.yaml data/taxa/eukaryota/komagataea_salicaria.yaml data/taxa/eukaryota/komagataea_wickerhamii.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:320403` carries `NCBITaxon:1337058`, label `Komagataea salicaria`, rank `SPECIES`, parent `NCBITaxon:3712926`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Komagataea`.
- `curation/seed_scope.tsv:59533` contains this identifier with reason `attested rule: Komagataea salicaria, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:85121` maps side-inventory old ID `NCBITaxon:53640` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:8173`, whose aggregate count is `1` for `NCBITaxon:1337058`.
- The current native GOLD scan found exact organism `Go0517085` for `Barnettozyma salicaria NRRL Y-6780`.
- Expanding that exact GOLD organism found project `Gp0441123` and the native linked analysis `Barnettozyma salicaria NRRL Y-6780` through `AP PROJECT GOLD IDS`.
- StrainInfo has 3 exact direct rows and 13 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 25 rows for `NCBITaxon:1337058` at lines 23824-23848, covering `ATCC 22308`, `BCRC 22179`, `CCRC 22179`, `IFO 1281`, `JCM 3653`, `NRRL Y-6780`, `UCD 61-344`, `VKM Y-1288`, `VKPM Y 120`, and `VKPM Y 975` culture-from-holotype variants plus `CBS 5456` holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1337058`, `just validate data/taxa/eukaryota/komagataea_salicaria.yaml`, and `just validate-strict data/taxa/eukaryota/komagataea_salicaria.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataea_salicaria` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
