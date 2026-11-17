# YAML Record Review: Lipomyces tetrasporus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_tetrasporus.yaml
- Started UTC: 2026-09-23T13:17:35Z
- Finished UTC: 2026-09-23T13:17:35Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_tetrasporus.yaml` denotes the exact NCBI species `Lipomyces tetrasporus` as `NCBITaxon:54092`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_tetrasporus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml data/taxa/eukaryota/lipomyces_starkeyi.yaml data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml data/taxa/eukaryota/lipomyces_tetrasporus.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6836` carries `NCBITaxon:54092`, label `Lipomyces tetrasporus`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, one exact synonym, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves the authorship-bearing `Lipomyces tetrasporus` name as an exact synonym from NCBI.
- `curation/seed_scope.tsv:52907` contains this identifier with reason `attested rule: Lipomyces tetrasporus, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:54092`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38297`, whose aggregate count is `14` for `NCBITaxon:54092`.
- The full native GOLD organism scan found 14 exact organisms for this NCBI ID, including `Go0530002`, `Go0530004`, `Go0583982`, `Go0583994`, `Go0584000`, and nine `Go0608142` through `Go0608150` organisms.
- The full native GOLD projects scan found 10 linked projects across those exact GOLD organisms, and a project-ID scan of the native GOLD analyses table found no linked analyses.
- Exact StrainInfo scans found 53 direct strain rows and 118 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:231385` through `231399` contain 15 type-material spellings for `Lipomyces tetrasporus`, spanning `CBS 5910`, `ATCC 32372`, `IFO 10391`, `JCM 6000`, `MUCL 39417`, `NCYC 1437`, and `NRRL Y-11562` variants. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:54092`, `just validate data/taxa/eukaryota/lipomyces_tetrasporus.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_tetrasporus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_tetrasporus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
