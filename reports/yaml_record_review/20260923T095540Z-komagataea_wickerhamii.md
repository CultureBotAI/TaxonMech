# YAML Record Review: Komagataea wickerhamii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataea_wickerhamii.yaml
- Started UTC: 2026-09-23T09:55:40Z
- Finished UTC: 2026-09-23T09:55:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/komagataea_wickerhamii.yaml` denotes the exact NCBI species `Komagataea wickerhamii` as `NCBITaxon:36032`, rank `SPECIES`, under genus `NCBITaxon:3712926` (`Komagataea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataea_wickerhamii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/komagataea_pratensis.yaml data/taxa/eukaryota/komagataea_qinlingensis.yaml data/taxa/eukaryota/komagataea_salicaria.yaml data/taxa/eukaryota/komagataea_wickerhamii.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4042` carries `NCBITaxon:36032`, label `Komagataea wickerhamii`, rank `SPECIES`, parent `NCBITaxon:3712926`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Komagataea`.
- `curation/seed_scope.tsv:52311` contains this identifier with reason `attested rule: Komagataea wickerhamii, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33255`, whose aggregate count is `1` for `NCBITaxon:36032`.
- The current native GOLD scan found exact organism `Go0705382` for `Barnettozyma wickerhamii NRRL Y-2435`.
- Expanding that exact GOLD organism found project `Gp0831424`, with no native linked analysis rows.
- StrainInfo has 9 exact direct rows and 25 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 11 rows for `NCBITaxon:36032` at lines 193728-193738, covering `ATCC 24215`, `BCRC 22438`, `CCRC 22438`, and `IFO 1278` culture-from-holotype variants plus `NRRL Y-2435` holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:36032`, `just validate data/taxa/eukaryota/komagataea_wickerhamii.yaml`, and `just validate-strict data/taxa/eukaryota/komagataea_wickerhamii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataea_wickerhamii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
