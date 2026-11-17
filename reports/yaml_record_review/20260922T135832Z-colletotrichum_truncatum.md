# YAML Record Review: Colletotrichum truncatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_truncatum.yaml
- Started UTC: 2026-09-22T13:53:16Z
- Finished UTC: 2026-09-22T13:58:32Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5467` |
| Label | `Colletotrichum truncatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707339` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_truncatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_truncatum.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism/project/analysis chain, three NCBI type-material rows, four NCBI merged-ID side rows, 83 exact StrainInfo side deposits, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5467`, `label: Colletotrichum truncatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707339`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2422`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum truncatum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38449`, which records one retained organism for `NCBITaxon:5467`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5467`. NCBI supplies all five exact synonyms and all seven related synonyms present in the YAML.

The native GOLD snapshot has one exact organism row for this NCBI taxon, `Go0455386` / `Colletotrichum truncatum MTCC 3414`, with project `Gp0323713` / `Colletotrichum truncatum MTCC 3414` and one linked analysis row; this agrees with the retained aggregate count.

The NCBI type-material side inventory has three exact rows for the same NCBI taxon: `ICMP:17929` for `Vermicularia capsici`, plus `CBS 151.35` and `CBS:151.35` for `Vermicularia truncata`. Those rows support external type-material relationships for synonyms of the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The exact StrainInfo side inventory has 83 deposits and 68 direct DOI records for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:5467` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_truncatum.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_truncatum.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` has four side-inventory old IDs that now map into `NCBITaxon:5467`: `NCBITaxon:1365447`, `NCBITaxon:1365448`, `NCBITaxon:51633`, and `NCBITaxon:5456`. The retained retired-row inventory is empty for this target, so the absence of `replaces` values in the YAML is expected.
