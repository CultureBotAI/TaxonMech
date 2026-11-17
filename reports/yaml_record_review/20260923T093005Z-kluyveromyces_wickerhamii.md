# YAML Record Review: Kluyveromyces wickerhamii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml
- Started UTC: 2026-09-23T09:30:05Z
- Finished UTC: 2026-09-23T09:30:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml` denotes the exact NCBI species `Kluyveromyces wickerhamii` as `NCBITaxon:51658`, rank `SPECIES`, under genus `NCBITaxon:4910` (`Kluyveromyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml data/taxa/eukaryota/knoxdaviesia_capensis.yaml data/taxa/eukaryota/knoxdaviesia_proteae.yaml data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6485` carries `NCBITaxon:51658`, label `Kluyveromyces wickerhamii`, rank `SPECIES`, parent `NCBITaxon:4910`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kluyveromyces`.
- `curation/seed_scope.tsv:52837` contains this identifier with reason `attested rule: Kluyveromyces wickerhamii, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:37626`, whose aggregate count is `1` for `NCBITaxon:51658`.
- The current native GOLD scan found exact organism `Go0705668` for `Kluyveromyces wickerhamii NRRL Y-8286`.
- Expanding that exact GOLD organism found project `Gp0831720`, with no native linked analysis rows.
- StrainInfo has 4 exact direct rows and 24 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 15 rows for `NCBITaxon:51658` at lines 226686-226700, covering `ATCC 24178`, `CBS 2745`, `DBVPG 6077`, `IFO 1675`, `NCYC 908`, `NRRL Y-8286`, and `UCD 54-210` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:51658`, `just validate data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml`, and `just validate-strict data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kluyveromyces_wickerhamii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
