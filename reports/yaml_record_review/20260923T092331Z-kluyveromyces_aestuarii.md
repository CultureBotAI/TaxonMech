# YAML Record Review: Kluyveromyces aestuarii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kluyveromyces_aestuarii.yaml
- Started UTC: 2026-09-23T09:23:31Z
- Finished UTC: 2026-09-23T09:23:31Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kluyveromyces_aestuarii.yaml` denotes the exact NCBI species `Kluyveromyces aestuarii` as `NCBITaxon:33165`, rank `SPECIES`, under genus `NCBITaxon:4910` (`Kluyveromyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kluyveromyces_aestuarii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kluyveromyces_aestuarii.yaml data/taxa/eukaryota/kluyveromyces_dobzhanskii.yaml data/taxa/eukaryota/kluyveromyces_lactis.yaml data/taxa/eukaryota/kluyveromyces_marxianus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:3545` carries `NCBITaxon:33165`, label `Kluyveromyces aestuarii`, rank `SPECIES`, parent `NCBITaxon:4910`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kluyveromyces`.
- `curation/seed_scope.tsv:52251` contains this identifier with reason `attested rule: Kluyveromyces aestuarii, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:32324`, whose aggregate count is `1` for `NCBITaxon:33165`.
- The current native GOLD scan found exact organism `Go0517148` for `Kluyveromyces aestuarii NRRL YB-4510` and project `Gp0441186`.
- The native GOLD analysis scan found one exact linked analysis, `Kluyveromyces aestuarii NRRL YB-4510`, through project `Gp0441186`.
- StrainInfo has 12 exact direct rows and 38 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 16 type-material rows for `NCBITaxon:33165` at lines 178930-178945, covering `ATCC 18862`, `BCRC 22014`, `CBS 4438`, `CCRC 22014`, `DBVPG 6307`, `IFO 10597`, `NRRL YB-4510`, and `UCD 61-29` spelling variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:33165`, `just validate data/taxa/eukaryota/kluyveromyces_aestuarii.yaml`, and `just validate-strict data/taxa/eukaryota/kluyveromyces_aestuarii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kluyveromyces_aestuarii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
