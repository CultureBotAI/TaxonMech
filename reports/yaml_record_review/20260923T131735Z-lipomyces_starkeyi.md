# YAML Record Review: Lipomyces starkeyi

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_starkeyi.yaml
- Started UTC: 2026-09-23T13:17:35Z
- Finished UTC: 2026-09-23T13:17:35Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_starkeyi.yaml` denotes the exact NCBI species `Lipomyces starkeyi` as `NCBITaxon:29829`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD records filed directly under this taxon.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_starkeyi.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml data/taxa/eukaryota/lipomyces_starkeyi.yaml data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml data/taxa/eukaryota/lipomyces_tetrasporus.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:3270` carries `NCBITaxon:29829`, label `Lipomyces starkeyi`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, one related synonym, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves the authorship-bearing `Lipomyces starkeyi` related synonym from NCBI.
- `curation/seed_scope.tsv:52206` contains this identifier with reason `attested rule: Lipomyces starkeyi, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:29829`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:29831`, whose aggregate count is `13` for `NCBITaxon:29829`.
- The full native GOLD organism scan found 12 exact organisms filed directly under this NCBI ID. The GOLD source attestation intentionally counts only direct rows here and does not gather the `Lipomyces starkeyi NRRL Y-11557` descendant taxon.
- The full native GOLD projects scan found 25 linked projects across those exact GOLD organisms, and a project-ID scan of the native GOLD analyses table found no linked analyses.
- Exact StrainInfo scans found 60 direct strain rows and 126 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:151904` through `151919` contain 16 cultures from holotype for `Lipomyces starkeyi`, spanning `BCRC:21522`, `CBS 1807`, `CCRC 21522`, `JCM 5995`, `MUCL 39418`, `NRRL Y-11557`, and `NRRL Y-1388` variants. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:29829`, `just validate data/taxa/eukaryota/lipomyces_starkeyi.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_starkeyi.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_starkeyi` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
