# YAML Record Review: Kazachstania africana

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kazachstania_africana.yaml
- Started UTC: 2026-09-23T09:10:43Z
- Finished UTC: 2026-09-23T09:10:43Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kazachstania_africana.yaml` denotes the exact NCBI species `Kazachstania africana` as `NCBITaxon:432096`, rank `SPECIES`, under genus `NCBITaxon:71245` (`Kazachstania`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kazachstania_africana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/karlodinium_veneficum.yaml data/taxa/eukaryota/kavinia_alboviridis.yaml data/taxa/eukaryota/kavinia_himantia.yaml data/taxa/eukaryota/kazachstania_africana.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:95498` carries `NCBITaxon:432096`, label `Kazachstania africana`, rank `SPECIES`, parent `NCBITaxon:71245`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kazachstania`.
- `curation/seed_scope.tsv:55633` contains this identifier with reason `attested rule: Kazachstania africana, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:51618`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:35327`, whose aggregate count is `6` for `NCBITaxon:432096`.
- The current native GOLD scan found exact organisms `Go0608117`, `Go0608118`, `Go0608119`, `Go0608120`, `Go0608121`, and `Go0608122` for `Kluyveromyces africanus` strains `ATCC 22294`, `DSM 70290`, `IFO 1671`, `Ky-0104`, `NBRC 1671`, and `NRRL Y-8276`.
- Expanding those exact GOLD organisms found project `Gp0831712`, with no native linked analysis rows.
- StrainInfo has 8 exact direct rows and 27 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 14 type-material rows for `NCBITaxon:432096` at lines 209676-209689, covering `ATCC 22294`, `BCRC 22015`, `CBS 2517`, `CCRC 22015`, `IFO 1671`, `NRRL Y-8276`, and `UCD 57-16` spelling variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:432096`, `just validate data/taxa/eukaryota/kazachstania_africana.yaml`, and `just validate-strict data/taxa/eukaryota/kazachstania_africana.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kazachstania_africana` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
