# YAML Record Review: Linnemannia zychae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/linnemannia_zychae.yaml
- Started UTC: 2026-09-23T13:03:46Z
- Finished UTC: 2026-09-23T13:03:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/linnemannia_zychae.yaml` denotes the exact NCBI species `Linnemannia zychae` as `NCBITaxon:979765`, rank `SPECIES`, under genus `NCBITaxon:2779861` (`Linnemannia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/linnemannia_zychae.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/linnemannia_sp.yaml data/taxa/eukaryota/linnemannia_zychae.yaml data/taxa/eukaryota/lipomyces_arxii.yaml data/taxa/eukaryota/lipomyces_chichibuensis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:204279` carries `NCBITaxon:979765`, label `Linnemannia zychae`, rank `SPECIES`, parent `NCBITaxon:2779861`, genetic code `1`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Linnemannia` genus.
- The record preserves `Mortierella zychae` as an exact synonym and the authorship-bearing `Linnemannia zychae` and `Mortierella zychae` names as related synonyms from NCBI.
- `curation/seed_scope.tsv:57062` contains this identifier with reason `attested rule: Linnemannia zychae, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:979765`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:45204`, whose aggregate count is `3` for `NCBITaxon:979765`.
- The native GOLD scan found three exact organisms for this NCBI ID: `Go0452990` for strain `NRRL 2592`, `Go0470754` for strain `PUST F9C`, and `Go0583314` for strain `FSU 9864`.
- The native GOLD projects scan found one project for each of those three exact GOLD organisms and no analyses linked through their project IDs.
- Exact StrainInfo scans found 14 direct rows and 14 deposit rows for this NCBI ID, including `CBS 109599`, `CBS 102879`, `CBS 316.52`, `CBS 531.81`, and `CBS 143.91` among the bounded samples, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:275955` through `275958` contain four type-material spellings for `Mortierella zychae`: `SZMC 11212`, `SZMC:11212`, `CBS 316.52`, and `CBS:316.52`. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:979765`, `just validate data/taxa/eukaryota/linnemannia_zychae.yaml`, and `just validate-strict data/taxa/eukaryota/linnemannia_zychae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `linnemannia_zychae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
