# YAML Record Review: Fusarium inflexum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_inflexum.yaml
- Started UTC: 2026-09-23T02:46:53Z
- Finished UTC: 2026-09-23T02:46:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:42671` |
| Label | `Fusarium inflexum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171631` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_inflexum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_heterosporum.yaml data/taxa/eukaryota/fusarium_hostae.yaml data/taxa/eukaryota/fusarium_illudens.yaml data/taxa/eukaryota/fusarium_inflexum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two current native GOLD organism rows, no native GOLD project or analysis rows, no NCBI merged-ID side rows, five exact direct StrainInfo rows, 11 StrainInfo deposit rows, 14 NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:42671`, `label: Fusarium inflexum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171631`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5021`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium oxysporum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35205`, which records two retained direct organisms for `NCBITaxon:42671`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs still contain exact organism rows for strains `CBS 716.74` and `DSM 63203`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:42671`. The YAML preserves the one related author-qualified NCBI synonym, `Fusarium inflexum R. Schneid., 1975`.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD organism catalog still contains exact rows `Go0608035` and `Go0608036`; the current native GOLD project and analysis catalogs do not contain linked rows for either organism.

No side-inventory NCBI old IDs merge into `NCBITaxon:42671`, so the YAML correctly has no generated `replaces` entry. StrainInfo contains five exact direct rows and 11 exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has 14 type-material aliases for the target in `typematerial.dmp`: `ATCC 32213`, `ATCC:32213`, `BBA 63203`, `BBA:63203`, `CBS 716.74`, `CBS:716.74`, `DAOM 225130`, `DAOM:225130`, `DSM 63203`, `DSM:63203`, `IMI 375336`, `IMI:375336`, `NRRL 20433`, and `NRRL:20433`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact native GOLD project or analysis rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_inflexum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_inflexum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_inflexum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism rows are exact by NCBI taxon ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
