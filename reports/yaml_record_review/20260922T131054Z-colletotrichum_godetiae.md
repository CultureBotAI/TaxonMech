# YAML Record Review: Colletotrichum godetiae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_godetiae.yaml
- Started UTC: 2026-09-22T13:06:00Z
- Finished UTC: 2026-09-22T13:10:54Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1209918` |
| Label | `Colletotrichum godetiae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707335` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_godetiae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_godetiae.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 10 retained organisms, 10 native GOLD organism rows, 11 native GOLD project rows, one native GOLD analysis, nine NCBI type-material rows, one NCBI merged-ID side row, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1209918`, `label: Colletotrichum godetiae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707335`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:273657`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum acutatum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:4976`, which records 10 retained organisms for `NCBITaxon:1209918`; this agrees with `source_attestations[1].assertion_count: 10`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1209918` with one name assertion. NCBI supplies the exact synonym `Colletotrichum clavatum` and both related synonyms present in the YAML.

The native GOLD snapshot has 10 exact organism rows for this NCBI taxon: `CBS 126527`, `CBS 193.32`, `CBS129951`, `IMI 367466`, `RB008`, `RB009`, `RB010`, `RB093`, `RB168`, and `C184`. Those rows support 11 native GOLD project rows; the `C184` project also has an analysis row.

The NCBI type-material side inventory has nine exact rows for this taxon: seven `Colletotrichum clavatum` holotype or holotype-culture designations and two `Colletotrichum godetiae` `CBS 133.44` designations. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including nine exact deposit matches and nine direct species matches. Because no generated rows exist for `NCBITaxon:1209918` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1209918` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_godetiae.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_godetiae.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:1190820` into `NCBITaxon:1209918`, but this is only a side-inventory old ID; no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
