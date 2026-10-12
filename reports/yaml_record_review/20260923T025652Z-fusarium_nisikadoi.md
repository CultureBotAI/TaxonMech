# YAML Record Review: Fusarium nisikadoi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_nisikadoi.yaml
- Started UTC: 2026-09-23T02:56:52Z
- Finished UTC: 2026-09-23T02:56:52Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:78863` |
| Label | `Fusarium nisikadoi` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1328894` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_nisikadoi.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_mori.yaml data/taxa/eukaryota/fusarium_neocosmosporiellum.yaml data/taxa/eukaryota/fusarium_newnesense.yaml data/taxa/eukaryota/fusarium_nisikadoi.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with two linked projects, no native GOLD analysis rows, no NCBI merged-ID side rows, three exact direct StrainInfo rows, eight StrainInfo deposit rows, ten NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:78863`, `label: Fusarium nisikadoi`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1328894`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:11533`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium nisikadoi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42754`, which records one retained direct organism for `NCBITaxon:78863`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs still contain the exact organism `Go0586050` and two linked projects for strain `NRRL 25179`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:78863`. The YAML preserves the one related author-qualified NCBI synonym, `Fusarium nisikadoi T. Aoki & Nirenberg, 1997`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs still contain the exact organism row `Go0586050` and two linked project rows; they do not contain a native GOLD analysis linked to either project.

No side-inventory NCBI old IDs merge into `NCBITaxon:78863`, so the YAML correctly has no generated `replaces` entry. StrainInfo contains three exact direct rows and eight exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has ten holotype or type-material aliases for the target in `typematerial.dmp`: `CBS 456.97`, `CBS:456.97`, `BBA 69015`, `BBA:69015`, `MAFF 237506`, `MAFF:237506`, `NRRL 25205`, `NRRL 25308`, `NRRL:25205`, and `NRRL:25308`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_nisikadoi.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_nisikadoi.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_nisikadoi` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked organism ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
