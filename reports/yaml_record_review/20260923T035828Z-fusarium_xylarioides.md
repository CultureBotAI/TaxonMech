# YAML Record Review: Fusarium xylarioides

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_xylarioides.yaml
- Started UTC: 2026-09-23T03:58:28Z
- Finished UTC: 2026-09-23T03:58:28Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:221167` |
| Label | `Fusarium xylarioides` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_xylarioides.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_verticillioides.yaml data/taxa/eukaryota/fusarium_virguliforme.yaml data/taxa/eukaryota/fusarium_xylarioides.yaml data/taxa/eukaryota/fusarium_zealandicum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with six organism assertions, six exact current native GOLD organisms with six linked native GOLD projects and six linked native analysis rows, seven exact NCBI type-material rows, 125 exact StrainInfo records carrying 131 exact deposit rows, no exact BacDive or NCBI merged-ID rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:221167`, `label: Fusarium xylarioides`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:43529`, which carries the same label, parent, rank, code, two exact synonyms, two related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:21009`, which records six retained direct organisms for `NCBITaxon:221167`; this agrees with `source_attestations[1].assertion_count: 6` and its organism assertion unit. The current native GOLD catalogs also contain six exact organisms, six linked projects, and six linked analyses for the same NCBI taxon ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:221167`. The YAML preserves exact synonyms `Gibberella xylarioides` and `Gibberella xylarioides (nom. inval.)`, and it preserves the two related synonyms from the NCBI row.

The retained GOLD aggregate supplies six organism assertions. The current native GOLD catalogs have exact organisms and matching projects for `Fusarium xylarioides` strains `IMI 127659i`, `IMI 392674`, `IMI 392254`, `IMI 392277`, `IMI 389563`, and `IMI 375908i`; all six projects also have native GOLD analysis rows linked through `AP PROJECT GOLD IDS`.

The NCBI type-material table has seven exact rows for the target, covering `CBS 258.52`, `CBS:258.52`, `NRRL 25486`, `NRRL 25486; CBS 258.52`, `NRRL-25486`, `NRRL25486`, and `NRRL:25486`. StrainInfo has 125 exact target records and 131 exact deposits. These side rows do not create generated local strain entries by themselves.

No side `data/raw/ncbi_merged_ids.tsv` row maps an old ID into `NCBITaxon:221167`, and no retained row in `data/raw/ncbitaxon_taxa.tsv` carries a retired ID for this target, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, two exact synonyms, two related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_xylarioides.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_xylarioides.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_xylarioides` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:221167` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
