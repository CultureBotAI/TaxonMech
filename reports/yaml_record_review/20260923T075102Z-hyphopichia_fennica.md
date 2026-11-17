# YAML Record Review: Hyphopichia fennica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyphopichia_fennica.yaml
- Started UTC: 2026-09-23T07:51:02Z
- Finished UTC: 2026-09-23T07:51:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45548` |
| Label | `Hyphopichia fennica` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:507510` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Genetic Code | `12` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hyphopichia_fennica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hyphopichia_burtonii.yaml data/taxa/eukaryota/hyphopichia_buzzinii.yaml data/taxa/eukaryota/hyphopichia_fennica.yaml data/taxa/eukaryota/hyphopichia_homilentoma.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hyphopichia_fennica.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45548`, `label: Hyphopichia fennica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:507510`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:5602`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyphopichia`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36057`, which records one retained direct organism for `NCBITaxon:45548`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs contain one exact organism and one linked project, with no linked native analyses in the local snapshot.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45548`. `Candida fennica` and `Trichosporon fennicum` are present in `data/raw/ncbitaxon_taxa.tsv:5602` as exact synonyms, and all three authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0705631` organism for `NRRL Y-7505` and a linked `Gp0831678` project; the scan found no linked native analysis rows.

NCBI carries 14 exact type-material rows for `Trichosporon fennicum` at `data/raw/ncbi_type_material.tsv:215102` through `data/raw/ncbi_type_material.tsv:215115`, spanning ATCC 18895, BCRC/CCRC 21769, CBS 5928, IFO 10276, JCM 9849, and NRRL Y-7505 spelling variants.

The raw StrainInfo JSONL contains six exact direct source records and 19 exact deposit matches for `NCBITaxon:45548`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:208265` to current `NCBITaxon:45548`, but no retained retired NCBI row has `retired_into: NCBITaxon:45548`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyphopichia_fennica.yaml` plus `just validate-strict data/taxa/eukaryota/hyphopichia_fennica.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyphopichia_fennica` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID, but native GOLD rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
