# YAML Record Review: Hyphopichia burtonii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyphopichia_burtonii.yaml
- Started UTC: 2026-09-23T07:51:02Z
- Finished UTC: 2026-09-23T07:51:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:717740` |
| Label | `Hyphopichia burtonii` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:507510` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Genetic Code | `12` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hyphopichia_burtonii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/hyphopichia_burtonii.yaml data/taxa/eukaryota/hyphopichia_buzzinii.yaml data/taxa/eukaryota/hyphopichia_fennica.yaml data/taxa/eukaryota/hyphopichia_homilentoma.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hyphopichia_burtonii.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:717740`, `label: Hyphopichia burtonii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:507510`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:169167`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyphopichia`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41926`, which records one retained direct organism for `NCBITaxon:717740`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, one linked project, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:717740`. `Endomycopsis burtonii` and `Pichia burtonii` are present in `data/raw/ncbitaxon_taxa.tsv:169167` as exact synonyms, and both authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0519852` organism for strain `makgeolli`, a linked `Gp0444016` project, and one native analysis linked by project ID `Gp0444016`.

NCBI carries 22 exact type-material rows for `Pichia burtonii` at `data/raw/ncbi_type_material.tsv:260199` through `data/raw/ncbi_type_material.tsv:260220`, spanning CBS 2352, NRRL Y-1933, ATCC 13169, BCRC/CCRC 22087, DBVPG 3789, IFO 10837, JCM 3708, KCTC 7661, MUCL 31899, and NCYC 439 spelling variants.

The raw StrainInfo JSONL contains 77 exact direct source records and 141 exact deposit matches for `NCBITaxon:717740`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:45500` to current `NCBITaxon:717740`, but no retained retired NCBI row has `retired_into: NCBITaxon:717740`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyphopichia_burtonii.yaml` plus `just validate-strict data/taxa/eukaryota/hyphopichia_burtonii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyphopichia_burtonii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
