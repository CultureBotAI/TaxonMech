# YAML Record Review: Fusarium falciforme

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_falciforme.yaml
- Started UTC: 2026-09-23T02:36:42Z
- Finished UTC: 2026-09-23T02:36:42Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:195108` |
| Label | `Fusarium falciforme` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_falciforme.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fusarium_equiseti.yaml data/taxa/eukaryota/fusarium_euwallaceae.yaml data/taxa/eukaryota/fusarium_falciforme.yaml data/taxa/eukaryota/fusarium_flagelliforme.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three organism assertions, forty-six NCBI merged-ID side rows, nineteen exact direct StrainInfo rows, twenty-three StrainInfo deposit rows, six NCBI type-material rows, no exact native GOLD organism rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:195108`, `label: Fusarium falciforme`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:38779`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17930`, which records three retained direct organisms for `NCBITaxon:195108`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:195108`. The YAML preserves three exact synonyms, `Acremonium falciforme`, `Cephalosporium falciforme`, and `Neocosmospora falciformis`, plus the extensive NCBI related-synonym set covering historical combinations and FRC/FSSC provisional names.

The `data/raw/ncbi_merged_ids.tsv` side inventory has forty-six old IDs merged into `NCBITaxon:195108`; none are retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies three organism assertions. The current native GOLD catalogs have no exact organism, project, or analysis rows for the target NCBI taxon; this is consistent with GOLD being carried only through the retained aggregate source for this generated record.

StrainInfo contains nineteen exact direct rows and twenty-three exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has six type-material aliases for the target in `typematerial.dmp`: `CBS 475.67`, `CBS:475.67`, `IHM 939`, `IHM:939`, `IMI 268681`, and `IMI:268681`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI related and exact synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_falciforme.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_falciforme.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; current native GOLD evidence is side evidence only and does not create generated child strains without BacDive-derived local strain inventory entries.
