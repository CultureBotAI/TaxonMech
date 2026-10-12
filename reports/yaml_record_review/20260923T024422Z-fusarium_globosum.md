# YAML Record Review: Fusarium globosum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_globosum.yaml
- Started UTC: 2026-09-23T02:44:22Z
- Finished UTC: 2026-09-23T02:44:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:78864` |
| Label | `Fusarium globosum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_globosum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_gaditjirri.yaml data/taxa/eukaryota/fusarium_globosum.yaml data/taxa/eukaryota/fusarium_graminearum.yaml data/taxa/eukaryota/fusarium_graminum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project, no native GOLD analysis rows, one NCBI merged-ID side row, six exact direct StrainInfo rows, 13 StrainInfo deposit rows, 14 NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:78864`, `label: Fusarium globosum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:11534`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42755`, which records one retained direct organism for `NCBITaxon:78864`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs still contain the exact organism `Go0098893` and linked project `Gp0098893` for strain `NRRL 26131`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:78864`. The YAML preserves exact synonym `Fusarium globosum var. globosum` and the one related author-qualified NCBI synonym, `Fusarium globosum Rheeder, Marasas & P.E. Nelson, 1996`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs still contain the exact organism row `Go0098893` and linked project row `Gp0098893`; they do not contain a native GOLD analysis linked to that project.

The `data/raw/ncbi_merged_ids.tsv` side inventory has one old ID, `NCBITaxon:1608284`, merged into `NCBITaxon:78864`. It is not retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance, so the YAML correctly has no generated `replaces` entry.

StrainInfo contains six exact direct rows and 13 exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has 14 type-material aliases for the target in `typematerial.dmp`: `CBS 428.97`, `CBS:428.97`, `DAOM 214966`, `DAOM:214966`, `FRC M-8014`, `FRC:M:8014`, `IMI 375330`, `IMI:375330`, `MRC 6647`, `MRC:6647`, `NRRL 26131`, `NRRL:26131`, `PREM 51878`, and `PREM:51878`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_globosum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_globosum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_globosum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked organism ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
