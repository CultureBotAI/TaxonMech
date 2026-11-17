# YAML Record Review: Fusarium algeriense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_algeriense.yaml
- Started UTC: 2026-09-23T02:08:30Z
- Finished UTC: 2026-09-23T02:08:30Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2050978` |
| Label | `Fusarium algeriense` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2109596` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_algeriense.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_albosuccineum.yaml data/taxa/eukaryota/fusarium_algeriense.yaml data/taxa/eukaryota/fusarium_ambrosium.yaml data/taxa/eukaryota/fusarium_anguioides.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two current native GOLD organism rows with two linked projects, two native GOLD analysis rows linked by project ID, six NCBI type-material rows, no NCBI merged-ID side rows, no exact BacDive rows, no StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2050978`, `label: Fusarium algeriense`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2109596`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:513894`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium burgessii species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:19524`, which records two retained direct organisms for `NCBITaxon:2050978`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2050978`. The YAML preserves both NCBI related synonyms: `Fusarium algeriense Laraba & O'Donnell, 2017` and `Fusarium sp. RP-2017a`.

No NCBI merged-ID side rows point to `NCBITaxon:2050978`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies two organism assertions; the current native GOLD catalogs still contain two exact organism rows, two linked project rows, and two linked analysis rows for the target NCBI taxon.

NCBI type-material rows 81131-81136 list six culture-from-holotype or holotype designations for `Fusarium algeriense`, covering CBS 142638, NRRL 66647, and BPI 910347 variants. No exact BacDive, StrainInfo, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_algeriense.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_algeriense.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
