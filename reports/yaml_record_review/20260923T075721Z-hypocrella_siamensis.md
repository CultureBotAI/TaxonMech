# YAML Record Review: Hypocrella siamensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypocrella_siamensis.yaml
- Started UTC: 2026-09-23T07:57:21Z
- Finished UTC: 2026-09-23T07:57:21Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:696354` |
| Label | `Hypocrella siamensis` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:42305` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hypocrella_siamensis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/hypocrella_siamensis.yaml data/taxa/eukaryota/hypomontagnella_monticulosa.yaml data/taxa/eukaryota/hypomontagnella_submonticulosa.yaml data/taxa/eukaryota/hypomyces_albidus.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hypocrella_siamensis.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:696354`, `label: Hypocrella siamensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:42305`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:163226`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hypocrella`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41507`, which records one retained direct organism for `NCBITaxon:696354`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, one linked project, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:696354`. `Aschersonia badia` is present in `data/raw/ncbitaxon_taxa.tsv:163226` as an exact synonym, and the authorship-bearing `Hypocrella siamensis` name in the YAML is present as a related synonym.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0091946` organism for `MTCC 10142`, a linked `Gp0091946` project, and one native analysis linked by project ID `Gp0091946`.

NCBI carries five exact type-material rows for `Hypocrella siamensis` at `data/raw/ncbi_type_material.tsv:257952` through `data/raw/ncbi_type_material.tsv:257956`, spanning BCC 8407 culture-from-holotype and BBH 14102 holotype spelling variants.

The raw StrainInfo JSONL contains five exact direct source records and five exact deposit matches for `NCBITaxon:696354`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:153671` to current `NCBITaxon:696354`, but no retained retired NCBI row has `retired_into: NCBITaxon:696354`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hypocrella_siamensis.yaml` plus `just validate-strict data/taxa/eukaryota/hypocrella_siamensis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hypocrella_siamensis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
