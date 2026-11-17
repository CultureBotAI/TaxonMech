# YAML Record Review: Hypomontagnella monticulosa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypomontagnella_monticulosa.yaml
- Started UTC: 2026-09-23T07:57:21Z
- Finished UTC: 2026-09-23T07:57:21Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2487000` |
| Label | `Hypomontagnella monticulosa` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:2652702` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hypomontagnella_monticulosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hypocrella_siamensis.yaml data/taxa/eukaryota/hypomontagnella_monticulosa.yaml data/taxa/eukaryota/hypomontagnella_submonticulosa.yaml data/taxa/eukaryota/hypomyces_albidus.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hypomontagnella_monticulosa.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2487000`, `label: Hypomontagnella monticulosa`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2652702`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:526319`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hypomontagnella`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:22362`, which records one retained direct organism for `NCBITaxon:2487000`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs contain one exact organism and two linked projects, with no linked native analyses in the local snapshot.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2487000`. `Hypoxylon monticulosum` is present in `data/raw/ncbitaxon_taxa.tsv:526319` as an exact synonym, and all four other names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0454029` organism for strain `FL0542` and linked `Gp0322175` and `Gp0345656` projects; the scan found no linked native analysis rows.

NCBI carries six exact type-material rows for `Hypoxylon monticulosum` at `data/raw/ncbi_type_material.tsv:96444` through `data/raw/ncbi_type_material.tsv:96449`, all culture-from-epitype spelling variants around `BCCM/MUCL 54604` and `MUCL 54604`.

The raw StrainInfo JSONL contains seven exact direct source records and eight exact deposit matches for `NCBITaxon:2487000`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:1180951`, `NCBITaxon:1794843`, and `NCBITaxon:326669` to current `NCBITaxon:2487000`, but no retained retired NCBI row has `retired_into: NCBITaxon:2487000`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hypomontagnella_monticulosa.yaml` plus `just validate-strict data/taxa/eukaryota/hypomontagnella_monticulosa.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hypomontagnella_monticulosa` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID, but native GOLD rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
