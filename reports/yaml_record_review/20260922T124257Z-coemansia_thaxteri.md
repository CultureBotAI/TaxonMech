# YAML Record Review: Coemansia thaxteri

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coemansia_thaxteri.yaml
- Started UTC: 2026-09-22T12:39:30Z
- Finished UTC: 2026-09-22T12:42:57Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2663907` |
| Label | `Coemansia thaxteri` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4863` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coemansia_thaxteri.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coemansia_thaxteri.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, two current native GOLD organism/project chains, no NCBI type-material rows, no native GOLD analyses, no BacDive or StrainInfo exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2663907`, `label: Coemansia thaxteri`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4863`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:541624`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coemansia`; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:24473`, which records three retained organisms for `NCBITaxon:2663907`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2663907` with one name assertion. NCBI supplies the related synonym `Coemansia thaxteri Linder, 1943` present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has two exact organism/project pairs for this NCBI taxon: `IMI 214463` / `Go0515239` / `Gp0436007` and `IMI 214461` / `Go0537797` / `Gp0487804`. No native GOLD analysis rows are currently linked to those projects.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:2663907` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, `data/straininfo/related_records.tsv.gz`, or the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coemansia_thaxteri.yaml` plus `just validate-strict data/taxa/eukaryota/coemansia_thaxteri.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:2663907`.

The retained GOLD aggregate count is three, while the current local native GOLD JSONL snapshot exposes two exact organism/project chains; the generated source attestation follows the retained aggregate row.
