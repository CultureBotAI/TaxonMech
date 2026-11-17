# YAML Record Review: Lizanozyma spartinae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lizanozyma_spartinae.yaml
- Started UTC: 2026-09-23T13:23:42Z
- Finished UTC: 2026-09-23T13:23:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lizanozyma_spartinae.yaml` denotes the exact NCBI species `Lizanozyma spartinae` as `NCBITaxon:45513`, rank `SPECIES`, under genus `NCBITaxon:3712557` (`Lizanozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lizanozyma_spartinae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lithophyllospora_australis.yaml data/taxa/eukaryota/litonotus_pictus.yaml data/taxa/eukaryota/lizanozyma_gosingica.yaml data/taxa/eukaryota/lizanozyma_spartinae.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5581` carries `NCBITaxon:45513`, label `Lizanozyma spartinae`, rank `SPECIES`, parent `NCBITaxon:3712557`, genetic code `12`, three exact synonyms, three related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lizanozyma` genus.
- The record preserves the NCBI `Pichia`, `Scheffersomyces`, and `Yamadazyma` exact synonyms plus three authorship-bearing related synonyms.
- `curation/seed_scope.tsv:52627` contains this identifier with reason `attested rule: Lizanozyma spartinae, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:45513`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:36025`, whose aggregate count is `3` for `NCBITaxon:45513`.
- The native GOLD scan found one exact organism for this NCBI ID, `Go0672320`, for strain `ARV_011`; the aggregate GOLD row records a higher historical count than the current native exact scan.
- The native GOLD projects scan found one linked project, `Gp0763504`, and the native GOLD analyses scan found one row linked through that project ID.
- Exact StrainInfo scans found 22 direct strain rows and 50 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:214644` through `214659` contain 16 type-material spellings for `Pichia spartinae`, covering `ATCC 18866`, `CBS 6059`, `IFO 1827`, `NCYC 771`, and `NRRL Y-7688` as cultures from holotype plus `NRRL Y-7322` as holotype. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:45513`, `just validate data/taxa/eukaryota/lizanozyma_spartinae.yaml`, and `just validate-strict data/taxa/eukaryota/lizanozyma_spartinae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lizanozyma_spartinae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
