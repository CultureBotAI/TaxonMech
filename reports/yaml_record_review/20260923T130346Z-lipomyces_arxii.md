# YAML Record Review: Lipomyces arxii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_arxii.yaml
- Started UTC: 2026-09-23T13:03:46Z
- Finished UTC: 2026-09-23T13:03:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_arxii.yaml` denotes the exact NCBI species `Lipomyces arxii` as `NCBITaxon:56418`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_arxii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/linnemannia_sp.yaml data/taxa/eukaryota/linnemannia_zychae.yaml data/taxa/eukaryota/lipomyces_arxii.yaml data/taxa/eukaryota/lipomyces_chichibuensis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7092` carries `NCBITaxon:56418`, label `Lipomyces arxii`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, two exact synonyms, three related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves `Kawasakia arxii` and `Zygozyma arxii` as exact synonyms and the three authorship-bearing names as related synonyms from NCBI.
- `curation/seed_scope.tsv:52961` contains this identifier with reason `attested rule: Lipomyces arxii, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:56418`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38921`, whose aggregate count is `2` for `NCBITaxon:56418`.
- The native GOLD scan found two exact organisms for this NCBI ID: `Go0517143` for strain `NRRL Y-17921` and `Go0583975` for strain `UCDFST 12-163`.
- The native GOLD projects scan found four linked projects: two for `Go0517143` and two for `Go0583975`. The native GOLD analyses scan found two rows linked through projects `Gp0441181` and `Gp0780256`.
- Exact StrainInfo scans found one direct strain row and nine deposit rows for this NCBI ID, including `KCTC 7881`, `ATCC 76360`, `CBS 7333`, `CCRC 22233`, and `IFO 10914` among the bounded samples, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:235998` through `236014` contain 17 type-material spellings for `Zygozyma arxii`, spanning `ATCC 76360`, `BCRC:22233`, `CBS 7333`, `CCRC 22233`, `IFO 10914`, `NRRL Y-17921`, and colon or combined-designation variants. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:56418`, `just validate data/taxa/eukaryota/lipomyces_arxii.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_arxii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_arxii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
