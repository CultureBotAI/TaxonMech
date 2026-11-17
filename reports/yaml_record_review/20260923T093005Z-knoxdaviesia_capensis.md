# YAML Record Review: Knoxdaviesia capensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/knoxdaviesia_capensis.yaml
- Started UTC: 2026-09-23T09:30:05Z
- Finished UTC: 2026-09-23T09:30:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/knoxdaviesia_capensis.yaml` denotes the exact NCBI species `Knoxdaviesia capensis` as `NCBITaxon:114771`, rank `SPECIES`, under genus `NCBITaxon:1215354` (`Knoxdaviesia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/knoxdaviesia_capensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml data/taxa/eukaryota/knoxdaviesia_capensis.yaml data/taxa/eukaryota/knoxdaviesia_proteae.yaml data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:20866` carries `NCBITaxon:114771`, label `Knoxdaviesia capensis`, rank `SPECIES`, parent `NCBITaxon:1215354`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Knoxdaviesia`.
- `curation/seed_scope.tsv:53804` contains this identifier with reason `attested rule: Knoxdaviesia capensis, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:1497318`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:3005`, whose aggregate count is `1` for `NCBITaxon:114771`.
- The current native GOLD scan found exact organism `Go0093999` for `Knoxdaviesia capensis H9`.
- Expanding that exact GOLD organism found project `Gp0093999` and a native linked analysis row for `Knoxdaviesia capensis H9`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 2 rows for `NCBITaxon:114771` at lines 9733-9734, covering `CMW 928` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:114771`, `just validate data/taxa/eukaryota/knoxdaviesia_capensis.yaml`, and `just validate-strict data/taxa/eukaryota/knoxdaviesia_capensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `knoxdaviesia_capensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
