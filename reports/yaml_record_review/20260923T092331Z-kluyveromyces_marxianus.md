# YAML Record Review: Kluyveromyces marxianus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kluyveromyces_marxianus.yaml
- Started UTC: 2026-09-23T09:23:31Z
- Finished UTC: 2026-09-23T09:23:31Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kluyveromyces_marxianus.yaml` denotes the exact NCBI species `Kluyveromyces marxianus` as `NCBITaxon:4911`, rank `SPECIES`, under genus `NCBITaxon:4910` (`Kluyveromyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kluyveromyces_marxianus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kluyveromyces_aestuarii.yaml data/taxa/eukaryota/kluyveromyces_dobzhanskii.yaml data/taxa/eukaryota/kluyveromyces_lactis.yaml data/taxa/eukaryota/kluyveromyces_marxianus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2136` carries `NCBITaxon:4911`, label `Kluyveromyces marxianus`, rank `SPECIES`, parent `NCBITaxon:4910`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kluyveromyces`.
- `curation/seed_scope.tsv:51873` contains this identifier with reason `attested rule: Kluyveromyces marxianus, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old IDs `NCBITaxon:1219278`, `NCBITaxon:1859946`, and `NCBITaxon:39396`, but none are present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:37106`, whose aggregate count is `304` for `NCBITaxon:4911`.
- The current native GOLD scan found 282 unique exact organisms for `NCBITaxon:4911`; complete expansion found 295 projects linked to those exact organism IDs.
- The native GOLD analysis expansion found 9 exact linked analyses through the exact project IDs, including projects for `DMB1`, `IIPE453`, `NBRC 1777`, `UFS-Y2791`, `B0399`, `CBS4857`, `SB-72`, `SB-154`, and `NRRL Y-6860`.
- StrainInfo has 301 exact direct rows and 553 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 18 rows for `NCBITaxon:4911` at lines 222879-222896, covering `CBS 712` and `NRRL Y-8281` cultures from type material plus `BCRC 21499`, `CCRC 21499`, `DBVPG 6165`, `IFO 10005`, `IGC 3886`, `MUCL 46196`, and `UCD 55-82` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:4911`, `just validate data/taxa/eukaryota/kluyveromyces_marxianus.yaml`, and `just validate-strict data/taxa/eukaryota/kluyveromyces_marxianus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kluyveromyces_marxianus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
