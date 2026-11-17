# YAML Record Review: Colletotrichum navitas

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_navitas.yaml
- Started UTC: 2026-09-22T13:27:30Z
- Finished UTC: 2026-09-22T13:31:40Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:681940` |
| Label | `Colletotrichum navitas` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707348` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_navitas.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_navitas.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 10 retained organisms, seven native GOLD organisms, eight native GOLD projects, no native GOLD analyses, three NCBI type-material rows, one NCBI merged-ID side row, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:681940`, `label: Colletotrichum navitas`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707348`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:159982`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum graminicola species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41185`, which records 10 retained organisms for `NCBITaxon:681940`; this agrees with `source_attestations[1].assertion_count: 10`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:681940` with one name assertion. NCBI supplies the exact synonym `Colletotrichum navitus` and the related synonym present in the YAML.

The native GOLD snapshot has seven exact organism rows for this NCBI taxon: `9038-158a (CBS125086)`, `CN71`, `VF38`, `VF38c`, `VF7B`, `VS47`, and a second `VS47`-named record under `VF7b VS47`. Exact native project lookup found eight project rows, with two projects for `9038-158a`; none have linked native analysis rows.

The NCBI type-material side inventory has three exact rows for `Colletotrichum navitas`: `CBS 125086` and `CBS:125086` as holotype cultures and `9038-a` as type material. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:681940` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_navitas.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_navitas.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:1347396` into `NCBITaxon:681940`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry. The native GOLD JSONL catalog currently exposes seven exact organism rows for `NCBITaxon:681940`, while the retained aggregate workbook inventory reports 10 organisms.
