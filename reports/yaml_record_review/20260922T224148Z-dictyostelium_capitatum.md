# YAML Record Review: Dictyostelium capitatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dictyostelium_capitatum.yaml
- Started UTC: 2026-09-22T22:41:48Z
- Finished UTC: 2026-09-22T22:41:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:361071` |
| Label | `Dictyostelium capitatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5782` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dictyostelium_capitatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dictyocoela_muelleri.yaml data/taxa/eukaryota/dictyocoela_roeselum.yaml data/taxa/eukaryota/dictyostelium_capitatum.yaml data/taxa/eukaryota/dictyostelium_citrinum.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to one project and one analysis, no exact NCBI type-material rows, one exact StrainInfo direct record carrying one matching deposit designation, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:361071`, `label: Dictyostelium capitatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5782`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:75083`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dictyostelium` genus; the bounded scan checked all ten lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:33288`, which records one retained direct organism for `NCBITaxon:361071`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:361071`. The YAML carries the single related synonym filed for this row; NCBI supplies no exact or broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0572131` for `Dictyostelium capitatum 91HO50`; one project, `Gp0546644`, under that organism; and one analysis named `Dictyostelium capitatum 91HO50` that links back through `AP PROJECT GOLD IDS`.

The exact StrainInfo side inventory has one direct record and one matching `ATCC 56229` deposit designation for `NCBITaxon:361071`, but it is not present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dictyostelium_capitatum.yaml` plus `just validate-strict data/taxa/eukaryota/dictyostelium_capitatum.yaml`.

## Additional Notes

The bounded scan found no side-inventory `data/raw/ncbi_merged_ids.tsv` mappings into `NCBITaxon:361071`.
