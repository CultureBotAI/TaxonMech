# YAML Record Review: Laxitextum bicolor

- Repository: TaxonMech
- Record: data/taxa/eukaryota/laxitextum_bicolor.yaml
- Started UTC: 2026-09-23T11:21:42Z
- Finished UTC: 2026-09-23T11:21:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/laxitextum_bicolor.yaml` denotes the exact NCBI species `Laxitextum bicolor` as `NCBITaxon:68771`, rank `SPECIES`, under genus `NCBITaxon:68770` (`Laxitextum`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/laxitextum_bicolor.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml data/taxa/eukaryota/laurencia_pacifica.yaml data/taxa/eukaryota/laxitextum_bicolor.yaml data/taxa/eukaryota/leccinellum_crocipodium.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:9413` carries `NCBITaxon:68771`, label `Laxitextum bicolor`, rank `SPECIES`, parent `NCBITaxon:68770`, genetic code `1`, exact synonym `Thelephora bicolor`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Laxitextum`.
- `curation/seed_scope.tsv:53168` contains this identifier with reason `attested rule: Laxitextum bicolor, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:68771`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:41346`, whose aggregate count is `1` for `NCBITaxon:68771`.
- The current native GOLD scan found exact organism `Go0357141` for `Laxitextum bicolor CBS 258.73`, projects `Gp0191685` and `Gp0306507`, and one native analysis row linked through `Gp0191685`.
- Exact StrainInfo scans found 42 direct strains and 44 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:68771` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:68771`, `just validate data/taxa/eukaryota/laxitextum_bicolor.yaml`, and `just validate-strict data/taxa/eukaryota/laxitextum_bicolor.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `laxitextum_bicolor` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
