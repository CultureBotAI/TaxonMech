# YAML Record Review: [Emmonsia] crescens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/emmonsia_crescens.yaml
- Started UTC: 2026-09-22T23:58:59Z
- Finished UTC: 2026-09-22T23:58:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:73230` |
| Label | `[Emmonsia] crescens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1955773` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/emmonsia_crescens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/emericellopsis_stolkiae.yaml data/taxa/eukaryota/emiliania_huxleyi.yaml data/taxa/eukaryota/emmonsia_crescens.yaml data/taxa/eukaryota/encephalitozoon_cuniculi_ec1.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one current native GOLD organism/project row, no native GOLD analyses, six NCBI type-material rows, two NCBI merged-ID side rows, no retained retired rows, 28 exact StrainInfo direct records carrying 40 matching deposit designations, two exact StrainInfo related-record rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:73230`, `label: [Emmonsia] crescens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1955773`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:10278`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Emergomyces` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42055`, which records two retained direct organisms for `NCBITaxon:73230`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:73230`. The YAML preserves all five exact synonyms and all four related synonyms filed for this NCBI row, spanning the `Ajellomyces`, `Chrysosporium`, `Emergomyces`, and `Emmonsia` names; NCBI supplies no broad synonyms.

The six NCBI type-material rows preserve `ATCC 13704`, `CBS 177.60`, and `UAMH 3008` aliases as type material for `Emmonsia crescens`. The NCBI merged-ID side inventory maps `NCBITaxon:1247875` and `NCBITaxon:1809711` to the current target, but neither is a retained retired row in `data/raw/ncbitaxon_taxa.tsv`, so the absent `replaces` field is consistent with the generated output.

The native GOLD catalogs contain one current exact organism row, `Go0096780` for `Emmonsia crescens UAMH4076`, with one matching project, `Gp0096780`, and no matching native GOLD analysis rows. The exact StrainInfo side inventory has 28 direct records carrying 40 matching deposit designations; two `data/straininfo/related_records.tsv.gz` rows map `ATCC 13704` evidence to `kgmicrobe.strain:bacdive_144769`, but `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and the maintained final strain tables have no exact rows for `NCBITaxon:73230`, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, five NCBI exact synonyms, four NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv` or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/emmonsia_crescens.yaml` plus `just validate-strict data/taxa/eukaryota/emmonsia_crescens.yaml`.

## Additional Notes

The NCBI type-material sample was expanded with an exact `NCBITaxon:73230` lookup in `data/raw/ncbi_type_material.tsv` to account for all six designations. The retained GOLD aggregate count can differ from the current exact native GOLD JSONL rows; in this snapshot, the aggregate retained table carries two organism assertions while the native organism JSONL has one exact row.
