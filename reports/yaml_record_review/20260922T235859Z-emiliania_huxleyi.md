# YAML Record Review: Emiliania huxleyi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/emiliania_huxleyi.yaml
- Started UTC: 2026-09-22T23:58:59Z
- Finished UTC: 2026-09-22T23:58:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2903` |
| Label | `Emiliania huxleyi` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2902` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/emiliania_huxleyi.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/emericellopsis_stolkiae.yaml data/taxa/eukaryota/emiliania_huxleyi.yaml data/taxa/eukaryota/emmonsia_crescens.yaml data/taxa/eukaryota/encephalitozoon_cuniculi_ec1.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with eight organism assertions, eight exact native GOLD organisms, 28 matching native GOLD projects, one native GOLD analysis, four NCBI type-material rows, one NCBI merged-ID side row, no retained retired rows, 115 exact StrainInfo direct records carrying 126 matching deposit designations, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2903`, `label: Emiliania huxleyi`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2902`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:1984`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Emiliania` genus; the bounded scan checked all 9 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:28331`, which records eight retained direct organisms for `NCBITaxon:2903`; this agrees with `source_attestations[1].assertion_count: 8` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2903`. The YAML preserves NCBI's exact synonyms `Gephyrocapsa huxleyi` and `Pontosphaera huxleyi`, plus all three related synonyms; NCBI supplies no broad synonyms.

The four NCBI type-material rows preserve `RCC 1853` aliases as cultures from the epitype of the `Pontosphaera huxleyi` synonym. The NCBI merged-ID side inventory maps `NCBITaxon:2562826` to the current target, but it is not a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so the absent `replaces` field is consistent with the generated output.

The native GOLD catalogs contain eight exact organism rows for `Emiliania huxleyi` strains `CCMP 1516`, `CCMP 371`, `1516`, `374`, `379`, `CCMP 370`, and `PLY M219`, plus one exact row without a strain value. Expanding the exact organism IDs found 28 native projects: four primary `Emiliania huxleyi` projects and 24 `CCMP 1516` transcriptome or co-culture transcriptome projects. The analysis catalog contains one exact project-linked row for `Gp0002811`.

The exact StrainInfo side inventory has 115 direct records carrying 126 matching deposit designations, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/emiliania_huxleyi.yaml` plus `just validate-strict data/taxa/eukaryota/emiliania_huxleyi.yaml`.

## Additional Notes

The native GOLD organism, project, and analysis counts were expanded with exact lookups against `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, and `data/gold/analyses.jsonl.gz` to account for all rows beyond the bounded samples.
