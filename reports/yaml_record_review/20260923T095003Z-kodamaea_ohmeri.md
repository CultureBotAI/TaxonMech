# YAML Record Review: Kodamaea ohmeri

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kodamaea_ohmeri.yaml
- Started UTC: 2026-09-23T09:50:03Z
- Finished UTC: 2026-09-23T09:50:03Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kodamaea_ohmeri.yaml` denotes the exact NCBI species `Kodamaea ohmeri` as `NCBITaxon:34356`, rank `SPECIES`, under genus `NCBITaxon:77850` (`Kodamaea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kodamaea_ohmeri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kodamaea_neixiangensis.yaml data/taxa/eukaryota/kodamaea_nitidulidarum.yaml data/taxa/eukaryota/kodamaea_ohmeri.yaml data/taxa/eukaryota/kodamaea_plutei.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:3826` carries `NCBITaxon:34356`, label `Kodamaea ohmeri`, rank `SPECIES`, parent `NCBITaxon:77850`, genetic code `12`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kodamaea`.
- `curation/seed_scope.tsv:52269` contains this identifier with reason `attested rule: Kodamaea ohmeri, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old IDs `NCBITaxon:234556`, `NCBITaxon:271354`, and `NCBITaxon:34360`, but none are present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:32850`, whose aggregate count is `12` for `NCBITaxon:34356`.
- Complete exact native GOLD expansion found 12 organisms for `Kodamaea ohmeri`, including `NRRL Y-1932`, `148`, `ATCC 46053`, `CBS 5367`, `DSM 70815`, `IFO 1271`, `IFO 1375`, `NBRC 1271`, `NBRC 1375`, `Pi-0604`, `UWOPS01-666b4`, and `UWOPS05-228.2`.
- Expanding those exact GOLD organisms found projects `Gp0441083`, `Gp0443882`, `Gp0778383`, and `Gp0778384`; native linked analysis expansion found 4 rows through those projects.
- StrainInfo has 69 exact direct rows and 148 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 14 rows for `NCBITaxon:34356` at lines 188460-188473, covering `CBS 5367` and `NRRL Y-1932` culture-from-type-material variants plus `ATCC 46053`, `BCRC 22178`, `CCRC 22178`, `IFO 1271`, and `UCD 75-73` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:34356`, `just validate data/taxa/eukaryota/kodamaea_ohmeri.yaml`, and `just validate-strict data/taxa/eukaryota/kodamaea_ohmeri.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kodamaea_ohmeri` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
