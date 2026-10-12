# YAML Record Review: Lipomyces spencermartinsiae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml
- Started UTC: 2026-09-23T13:17:35Z
- Finished UTC: 2026-09-23T13:17:35Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml` denotes the exact NCBI species `Lipomyces spencermartinsiae` as `NCBITaxon:56873`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml data/taxa/eukaryota/lipomyces_starkeyi.yaml data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml data/taxa/eukaryota/lipomyces_tetrasporus.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7207` carries `NCBITaxon:56873`, label `Lipomyces spencermartinsiae`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, two exact synonyms, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves `Lipomyces kononenkoae subsp. spencermartinsiae` and `Lipomyces spencer-martinsiae` as exact synonyms and two authorship-bearing names as related synonyms from NCBI.
- `curation/seed_scope.tsv:52972` contains this identifier with reason `attested rule: Lipomyces spencermartinsiae, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:56422` for `NCBITaxon:56873`, but it was not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`; this matches the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39061`, whose aggregate count is `2` for `NCBITaxon:56873`.
- The native GOLD scan found two exact organisms for this NCBI ID: `Go0705183` for strain `NBRC 10376` and `Go0705615` for strain `NRRL Y-7042`.
- The native GOLD projects scan found one linked project for each exact GOLD organism and no analyses linked through their project IDs.
- Exact StrainInfo scans found five direct strain rows and 15 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:236638` through `236645` contain eight exact rows for `Lipomyces kononenkoae subsp. spencermartinsiae`, including four `NRRL Y-7042` rows marked as not considered type plus `CBS 5608` and `NBRC 107660` type-material spellings. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:56873`, `just validate data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_spencermartinsiae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
