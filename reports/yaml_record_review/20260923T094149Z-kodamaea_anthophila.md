# YAML Record Review: Kodamaea anthophila

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kodamaea_anthophila.yaml
- Started UTC: 2026-09-23T09:41:49Z
- Finished UTC: 2026-09-23T09:41:49Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kodamaea_anthophila.yaml` denotes the exact NCBI species `Kodamaea anthophila` as `NCBITaxon:77851`, rank `SPECIES`, under genus `NCBITaxon:77850` (`Kodamaea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kodamaea_anthophila.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kodamaea_anthophila.yaml data/taxa/eukaryota/kodamaea_arcana.yaml data/taxa/eukaryota/kodamaea_derodonti.yaml data/taxa/eukaryota/kodamaea_fukazawae.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:11336` carries `NCBITaxon:77851`, label `Kodamaea anthophila`, rank `SPECIES`, parent `NCBITaxon:77850`, genetic code `12`, and the NCBI synonym retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kodamaea`.
- `curation/seed_scope.tsv:53313` contains this identifier with reason `attested rule: Kodamaea anthophila, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:42699`, whose aggregate count is `3` for `NCBITaxon:77851`.
- The current native GOLD scan found 3 exact organisms for `Kodamaea anthophila`: `Go0676582`, `Go0676583`, and `Go0705421`.
- Expanding those exact GOLD organisms found projects `Gp0778381`, `Gp0778382`, and `Gp0831464`; native linked analysis expansion found 2 rows for the `UWOPS95-602.1` and `UWOPS91-893.2` projects.
- StrainInfo has 3 exact direct rows and 10 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 10 rows for `NCBITaxon:77851` at lines 264220-264229, covering `CBS 8494`, `NRRL Y-27355`, and `UFMG95-602.1` culture-from-holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:77851`, `just validate data/taxa/eukaryota/kodamaea_anthophila.yaml`, and `just validate-strict data/taxa/eukaryota/kodamaea_anthophila.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kodamaea_anthophila` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
