# YAML Record Review: Lipomyces kononenkoae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_kononenkoae.yaml
- Started UTC: 2026-09-23T13:08:27Z
- Finished UTC: 2026-09-23T13:08:27Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_kononenkoae.yaml` denotes the exact NCBI species `Lipomyces kononenkoae` as `NCBITaxon:34357`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_kononenkoae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lipomyces_doorenjongii.yaml data/taxa/eukaryota/lipomyces_japonicus.yaml data/taxa/eukaryota/lipomyces_kockii.yaml data/taxa/eukaryota/lipomyces_kononenkoae.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:3827` carries `NCBITaxon:34357`, label `Lipomyces kononenkoae`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, one exact synonym, one related synonym, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves `Lipomyces kononenkoae subsp. kononenkoae` as an exact synonym and the authorship-bearing name as a related synonym from NCBI.
- `curation/seed_scope.tsv:52270` contains this identifier with reason `attested rule: Lipomyces kononenkoae, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:56421` for `NCBITaxon:34357`, but it was not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`; this matches the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:32851`, whose aggregate count is `3` for `NCBITaxon:34357`.
- The full native GOLD organism scan found three exact organisms for this NCBI ID: `Go0517140` for strain `NRRL Y-11553`, `Go0583989` for strain `CBS 7786`, and `Go0705602` for strain `NRRL Y-63818`.
- The full native GOLD projects scan found six linked projects, including three for `Go0517140`, two for `Go0583989`, and one for `Go0705602`.
- The native GOLD analyses scan found one row linked through project `Gp0441178`.
- Exact StrainInfo scans found nine direct strain rows and 33 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:188474` through `188486` contain 13 exact rows for `Lipomyces kononenkoae`, covering `CBS 2514`, `NBRC 107661`, and several `NRRL Y-63818` cultures from holotype plus `NRRL Y-11553` spellings marked as not considered type. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:34357`, `just validate data/taxa/eukaryota/lipomyces_kononenkoae.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_kononenkoae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_kononenkoae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
