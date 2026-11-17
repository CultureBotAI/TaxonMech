# YAML Record Review: Lipomyces chichibuensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_chichibuensis.yaml
- Started UTC: 2026-09-23T13:03:46Z
- Finished UTC: 2026-09-23T13:03:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_chichibuensis.yaml` denotes the exact NCBI species `Lipomyces chichibuensis` as `NCBITaxon:1546026`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_chichibuensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/linnemannia_sp.yaml data/taxa/eukaryota/linnemannia_zychae.yaml data/taxa/eukaryota/lipomyces_arxii.yaml data/taxa/eukaryota/lipomyces_chichibuensis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:398406` carries `NCBITaxon:1546026`, label `Lipomyces chichibuensis`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, four related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves the two authorship-bearing `Lipomyces chichibuensis` names and two `Lipomyces sp. NBRC` strain labels as related synonyms from NCBI.
- `curation/seed_scope.tsv:60439` contains this identifier with reason `attested rule: Lipomyces chichibuensis, 2 sources incl. NCBI`.
- The side NCBI merge scan found old IDs `NCBITaxon:1352825` and `NCBITaxon:1352826` for `NCBITaxon:1546026`, but neither was present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`; this matches the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:12326`, whose aggregate count is `1` for `NCBITaxon:1546026`.
- The native GOLD scan found one exact organism for this NCBI ID, `Go0583976`, for strain `CBS 12929`.
- The native GOLD projects scan found two projects for `Go0583976`, `Gp0588869` and `Gp0595892`, and no analyses linked through those project IDs.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:41237` through `41242` contain six type-material spellings for `Lipomyces chichibuensis`, covering `CBS 12929` and `NBRC 109582` as cultures from holotype and `CB08-2` as the holotype with colon variants. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1546026`, `just validate data/taxa/eukaryota/lipomyces_chichibuensis.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_chichibuensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_chichibuensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
