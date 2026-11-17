# YAML Record Review: Lachnellula suecica

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lachnellula_suecica.yaml
- Started UTC: 2026-09-23T10:48:36Z
- Finished UTC: 2026-09-23T10:48:36Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lachnellula_suecica.yaml` denotes the exact NCBI species `Lachnellula suecica` as `NCBITaxon:602035`, rank `SPECIES`, under genus `NCBITaxon:47830` (`Lachnellula`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lachnellula_suecica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lachnellula_subtilissima.yaml data/taxa/eukaryota/lachnellula_suecica.yaml data/taxa/eukaryota/lachnellula_willkommii.yaml data/taxa/eukaryota/lachnum_nothofagi.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:142207` carries `NCBITaxon:602035`, label `Lachnellula suecica`, rank `SPECIES`, parent `NCBITaxon:47830`, genetic code `1`, exact synonym `Pithya suecica`, and the related synonyms retained in the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lachnellula`.
- `curation/seed_scope.tsv:56151` contains this identifier with reason `attested rule: Lachnellula suecica, 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39780`, whose aggregate count is `1` for `NCBITaxon:602035`.
- The current native GOLD scan found exact organism `Go0631628` for `Lachnellula suecica CBS 268.59`.
- Expanding that exact GOLD organism found project `Gp0645164` and one native analysis row linked through that project ID.
- Exact StrainInfo scans found 2 direct strains and 2 deposits for this taxon; exact BacDive and generated StrainInfo overlay scans found no corresponding local BacDive-derived rows to emit.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:602035` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:602035`, `just validate data/taxa/eukaryota/lachnellula_suecica.yaml`, and `just validate-strict data/taxa/eukaryota/lachnellula_suecica.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lachnellula_suecica` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
