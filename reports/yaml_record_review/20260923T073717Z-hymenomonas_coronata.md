# YAML Record Review: Hymenomonas coronata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hymenomonas_coronata.yaml
- Started UTC: 2026-09-23T07:37:17Z
- Finished UTC: 2026-09-23T07:37:17Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:418937` |
| Label | `Hymenomonas coronata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:418936` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hymenomonas_coronata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hymenomonas_coronata.yaml data/taxa/eukaryota/hymenopellis_radicata.yaml data/taxa/eukaryota/hymenopellis_raphanipes.yaml data/taxa/eukaryota/hymenoscyphus_albidus.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no current native GOLD organism, project, or analysis rows filed directly under this NCBI taxon ID, no exact NCBI type-material rows, no side NCBI merged-ID rows, three exact direct StrainInfo source records, three exact StrainInfo deposit matches, no final StrainInfo overlay rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:418937`, `label: Hymenomonas coronata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:418936`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:91787`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hymenomonas`; the bounded scan checked all 9 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34996`, which records one retained direct organism for `NCBITaxon:418937`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:418937`. `Hymenomonas coronata Mills, 1975` is present in `data/raw/ncbitaxon_taxa.tsv:91787` as a related synonym, and the source row has no exact synonyms to omit.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs no longer file an organism, project, or analysis directly under `ORGANISM NCBI TAX ID` 418937.

The raw StrainInfo JSONL contains three exact direct source records and three exact deposit matches for `NCBITaxon:418937`, but the maintained StrainInfo overlay tables have no exact rows for this taxon. No exact NCBI type-material row, side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hymenomonas_coronata.yaml` plus `just validate-strict data/taxa/eukaryota/hymenomonas_coronata.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hymenomonas_coronata` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; no current native GOLD organism, project, or analysis rows are exact for `ORGANISM NCBI TAX ID` 418937.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
