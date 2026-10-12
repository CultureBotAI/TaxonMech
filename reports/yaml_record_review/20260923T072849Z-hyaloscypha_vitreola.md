# YAML Record Review: Hyaloscypha vitreola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyaloscypha_vitreola.yaml
- Started UTC: 2026-09-23T07:28:49Z
- Finished UTC: 2026-09-23T07:28:49Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:585615` |
| Label | `Hyaloscypha vitreola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:47747` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hyaloscypha_vitreola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hyaloscypha_vitreola.yaml data/taxa/eukaryota/hydnangium_carneum.yaml data/taxa/eukaryota/hydnangium_sp.yaml data/taxa/eukaryota/hydnomerulius_pinastri_md_312.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no current native GOLD organism, project, or analysis rows filed directly under this NCBI taxon ID, no exact NCBI type-material rows, no side NCBI merged-ID rows, two exact direct StrainInfo source records, two exact StrainInfo deposit matches, no final StrainInfo overlay rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:585615`, `label: Hyaloscypha vitreola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:47747`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:138780`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyaloscypha`; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39503`, which records one retained direct organism for `NCBITaxon:585615`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:585615`. `Peziza vitreola` is present in `data/raw/ncbitaxon_taxa.tsv:138780` as an exact synonym, and both authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs no longer file an organism, project, or analysis directly under `ORGANISM NCBI TAX ID` 585615.

The raw StrainInfo JSONL contains two exact direct source records and two exact deposit matches for `NCBITaxon:585615`, but the maintained StrainInfo overlay tables have no exact `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for this taxon. Those source-side StrainInfo matches therefore do not contradict the generated `strain_count: 0` or the absence of a `STRAININFO` source attestation.

No exact NCBI type-material row, side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyaloscypha_vitreola.yaml` plus `just validate-strict data/taxa/eukaryota/hyaloscypha_vitreola.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyaloscypha_vitreola` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; no current native GOLD organism, project, or analysis rows are exact for `ORGANISM NCBI TAX ID` 585615.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
