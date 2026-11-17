# YAML Record Review: Hypomyces chrysospermus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypomyces_chrysospermus.yaml
- Started UTC: 2026-09-23T08:01:02Z
- Finished UTC: 2026-09-23T08:01:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5131` |
| Label | `Hypomyces chrysospermus` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:5130` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hypomyces_chrysospermus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hypomyces_armeniacus.yaml data/taxa/eukaryota/hypomyces_aurantius.yaml data/taxa/eukaryota/hypomyces_chlorinigenus.yaml data/taxa/eukaryota/hypomyces_chrysospermus.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hypomyces_chrysospermus.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5131`, `label: Hypomyces chrysospermus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5130`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2251`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hypomyces`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37558`, which records two retained direct organisms for `NCBITaxon:5131`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs have no exact organism, project, or analysis rows for this taxon.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5131`. `Sepedonium chrysospermum` is present in `data/raw/ncbitaxon_taxa.tsv:2251` as an exact synonym, and the authorship-bearing `Hypomyces chrysospermus` name in the YAML is present as a related synonym.

The retained GOLD aggregate supplies two organism assertions, although the current native GOLD catalogs do not have exact `ORGANISM NCBI TAX ID: 5131` rows or linked projects/analyses in the local snapshot.

The raw StrainInfo JSONL contains 52 exact direct source records and 67 exact deposit matches for `NCBITaxon:5131`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:74843` and `NCBITaxon:74844` to current `NCBITaxon:5131`, but no retained retired NCBI row has `retired_into: NCBITaxon:5131`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hypomyces_chrysospermus.yaml` plus `just validate-strict data/taxa/eukaryota/hypomyces_chrysospermus.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hypomyces_chrysospermus` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`, which can differ from the current native GOLD organism, project, and analysis rows. Native GOLD evidence creates generated child strains only after joining to BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
