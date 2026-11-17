# YAML Record Review: Lachnellula subtilissima

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lachnellula_subtilissima.yaml
- Started UTC: 2026-09-23T10:48:36Z
- Finished UTC: 2026-09-23T10:48:36Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lachnellula_subtilissima.yaml` denotes the exact NCBI species `Lachnellula subtilissima` as `NCBITaxon:602034`, rank `SPECIES`, under genus `NCBITaxon:47830` (`Lachnellula`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lachnellula_subtilissima.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lachnellula_subtilissima.yaml data/taxa/eukaryota/lachnellula_suecica.yaml data/taxa/eukaryota/lachnellula_willkommii.yaml data/taxa/eukaryota/lachnum_nothofagi.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:142206` carries `NCBITaxon:602034`, label `Lachnellula subtilissima`, rank `SPECIES`, parent `NCBITaxon:47830`, genetic code `1`, exact synonym `Peziza subtilissima`, and the related synonyms retained in the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lachnellula`.
- `curation/seed_scope.tsv:56150` contains this identifier with reason `attested rule: Lachnellula subtilissima, 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39779`, whose aggregate count is `2` for `NCBITaxon:602034`.
- The current native GOLD scan found exact organisms `Go0368428` and `Go0632188` for `Lachnellula subtilissima` strains `CBS 196.66` and `CBS 197.66`.
- Expanding those exact GOLD organisms found projects `Gp0209603`, `Gp0325202`, and `Gp0646025`, plus two native analysis rows linked through `Gp0209603` and `Gp0646025`.
- Exact StrainInfo scans found 2 direct strains and 2 deposits for this taxon; exact BacDive and generated StrainInfo overlay scans found no corresponding local BacDive-derived rows to emit.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:602034` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:602034`, `just validate data/taxa/eukaryota/lachnellula_subtilissima.yaml`, and `just validate-strict data/taxa/eukaryota/lachnellula_subtilissima.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lachnellula_subtilissima` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
