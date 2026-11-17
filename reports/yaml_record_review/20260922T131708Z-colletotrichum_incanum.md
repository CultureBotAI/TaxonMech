# YAML Record Review: Colletotrichum incanum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_incanum.yaml
- Started UTC: 2026-09-22T13:11:05Z
- Finished UTC: 2026-09-22T13:17:08Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1573173` |
| Label | `Colletotrichum incanum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707349` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_incanum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_incanum.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two native GOLD organism/project/analysis chains, nine NCBI type-material rows, one NCBI merged-ID side row, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1573173`, `label: Colletotrichum incanum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707349`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:405327`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum spaethianum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12673`, which records two retained organisms for `NCBITaxon:1573173`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1573173` with one name assertion. NCBI supplies both related synonyms present in the YAML and no exact synonyms.

The native GOLD snapshot has two exact organism rows for this NCBI taxon: `Go0144612` / `MAFF 238704` and `Go0373180` / `MAFF238712`. Both organisms have one native GOLD project and one analysis row, matching the two retained organism assertions in the aggregate inventory.

The NCBI type-material side inventory has nine exact rows for `Colletotrichum incanum`, covering `CBS 133485`, `IL6A`, `NRRL 62592`, and `BPI 884116` designations plus local colon-normalized aliases. Those rows support external holotype-culture and holotype relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1573173` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_incanum.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_incanum.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:1266904` into `NCBITaxon:1573173`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
