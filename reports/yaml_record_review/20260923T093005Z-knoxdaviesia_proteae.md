# YAML Record Review: Knoxdaviesia proteae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/knoxdaviesia_proteae.yaml
- Started UTC: 2026-09-23T09:30:05Z
- Finished UTC: 2026-09-23T09:30:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/knoxdaviesia_proteae.yaml` denotes the exact NCBI species `Knoxdaviesia proteae` as `NCBITaxon:1215355`, rank `SPECIES`, under genus `NCBITaxon:1215354` (`Knoxdaviesia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/knoxdaviesia_proteae.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml data/taxa/eukaryota/knoxdaviesia_capensis.yaml data/taxa/eukaryota/knoxdaviesia_proteae.yaml data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:275095` carries `NCBITaxon:1215355`, label `Knoxdaviesia proteae`, rank `SPECIES`, parent `NCBITaxon:1215354`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Knoxdaviesia`.
- `curation/seed_scope.tsv:58435` contains this identifier with reason `attested rule: Knoxdaviesia proteae, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:5156`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:5133`, whose aggregate count is `2` for `NCBITaxon:1215355`.
- The current native GOLD scan found 2 exact organisms for `Knoxdaviesia proteae`: `Go0109833` for `SB2.3` and `Go0385018` for `CMW40885`.
- Expanding those exact GOLD organisms found projects `Gp0110284` and `Gp0236214`; the native linked analysis expansion found one analysis row through `Gp0110284` for `Knoxdaviesia proteae SB2.3`.
- StrainInfo has 8 exact direct rows and 8 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:1215355` at lines 14317-14322, covering `CBS 486.88`, `CMW 738`, and `PREM 48924` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1215355`, `just validate data/taxa/eukaryota/knoxdaviesia_proteae.yaml`, and `just validate-strict data/taxa/eukaryota/knoxdaviesia_proteae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `knoxdaviesia_proteae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
