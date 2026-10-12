# YAML Record Review: Collybiopsis luxurians FD-317 M1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/collybiopsis_luxurians_fd_317_m1.yaml
- Started UTC: 2026-09-22T14:03:23Z
- Finished UTC: 2026-09-22T14:08:11Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:944289` |
| Label | `Collybiopsis luxurians FD-317 M1` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2773346` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/collybiopsis_luxurians_fd_317_m1.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/collybiopsis_luxurians_fd_317_m1.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organism rows with three projects and one linked analysis, no NCBI type-material rows, no NCBI merged-ID side rows, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:944289`, `label: Collybiopsis luxurians FD-317 M1`, `rank: STRAIN`, `parent_taxon: NCBITaxon:2773346`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:201678`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Collybiopsis luxurians` species; the bounded scan checked all 15 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:44989`, which records two retained organisms for `NCBITaxon:944289`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:944289`. NCBI supplies no generated synonym rows for this strain record, which agrees with the empty YAML synonym set.

The native GOLD snapshot has two exact organism rows for this NCBI taxon, `Go0009594` / `Gymnopus luxurians` and `Go0010138` / `Gymnopus luxurians FD-317 M1`; they link to three projects, including `Gp0010138` / `Gymnopus luxurians FD-317 M1`, and one analysis row. This agrees with the retained aggregate count.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded strain identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, an intentionally empty synonym set, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:944289`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/collybiopsis_luxurians_fd_317_m1.yaml` plus `just validate-strict data/taxa/eukaryota/collybiopsis_luxurians_fd_317_m1.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:944289`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
