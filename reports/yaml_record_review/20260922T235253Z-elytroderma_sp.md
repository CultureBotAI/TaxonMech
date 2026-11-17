# YAML Record Review: Elytroderma sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/elytroderma_sp.yaml
- Started UTC: 2026-09-22T23:52:53Z
- Finished UTC: 2026-09-22T23:52:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2490632` |
| Label | `Elytroderma sp.` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2685069` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/elytroderma_sp.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/elytroderma_deformans.yaml data/taxa/eukaryota/elytroderma_sp.yaml data/taxa/eukaryota/emergomyces_africanus.yaml data/taxa/eukaryota/emergomyces_orientalis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism, one matching native GOLD project, no native GOLD analyses, no NCBI type-material or merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2490632`, `label: Elytroderma sp.`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2685069`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:526732`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `unclassified Elytroderma` parent; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:22472`, which records one retained direct organism for `NCBITaxon:2490632`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2490632`. NCBI supplies no exact, broad, or related synonyms and no old-ID side rows for this target, matching the absent `synonyms` and `replaces` fields in the YAML.

The native GOLD catalogs contain one exact organism row, `Go0511039` for `Elytroderma sp. PPCA2-2M`, with one matching project, `Gp0401093` for `Elytroderma sp. strain PPCA2-2M Standard Draft`. The analysis catalog contains no matching project or organism rows.

No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/elytroderma_sp.yaml` plus `just validate-strict data/taxa/eukaryota/elytroderma_sp.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row.
