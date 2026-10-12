# YAML Record Review: Eremothecium sinecaudum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/eremothecium_sinecaudum.yaml
- Started UTC: 2026-09-23T00:52:02Z
- Finished UTC: 2026-09-23T00:52:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45286` |
| Label | `Eremothecium sinecaudum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:33170` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/eremothecium_sinecaudum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/eremothecium_gossypii.yaml data/taxa/eukaryota/eremothecium_sinecaudum.yaml data/taxa/eukaryota/erysiphe_necator.yaml data/taxa/eukaryota/erysiphe_neolycopersici.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis row, 12 NCBI type-material rows, one NCBI merged-ID side row, two exact StrainInfo rows with six deposits, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45286`, `label: Eremothecium sinecaudum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:33170`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5525`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Eremothecium` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35910`, which records one retained direct organism for `NCBITaxon:45286`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45286`. The YAML preserves NCBI's three exact synonyms, `Eremothecium sinecaudum (Holley) Kurtzman`, `Holleya sinecauda`, and `Nematospora sinecauda`, plus its two related synonyms.

`data/raw/ncbi_merged_ids.tsv:79871` maps the old side-inventory ID `NCBITaxon:46676` to `NCBITaxon:45286`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The native GOLD catalogs contain one exact organism row, `Go0145100` for `Eremothecium sinecaudum ATCC 58844`, with one matching project, `Gp0150734`, and one linked native GOLD analysis row.

NCBI type-material evidence contributes 12 aliases for `Nematospora sinecauda`, including ATCC, BCRC, CBS, CCRC, DAOM, and NRRL variants. StrainInfo contains two exact target rows with six deposit designations for `Eremothecium sinecaudum`; those side rows do not produce BacDive-derived local strain children for this taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/eremothecium_sinecaudum.yaml` plus `just validate-strict data/taxa/eukaryota/eremothecium_sinecaudum.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
