# YAML Record Review: Colletotrichum fructicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_fructicola.yaml
- Started UTC: 2026-09-22T12:59:45Z
- Finished UTC: 2026-09-22T13:03:35Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:690256` |
| Label | `Colletotrichum fructicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707338` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_fructicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_fructicola.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two native GOLD organism/project/analysis chains, nine NCBI type-material rows, three NCBI merged-ID side rows, exact StrainInfo species/deposit rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:690256`, `label: Colletotrichum fructicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707338`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:162083`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum gloeosporioides species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41394`, which records two retained organisms for `NCBITaxon:690256`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:690256` with one name assertion. NCBI supplies the exact synonym `Colletotrichum ignotum` and all five related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has two exact organism/project/analysis chains for this NCBI taxon: `15060` / `Go0454954` / `Gp0323280` and `1104-7` / `Go0454995` / `Gp0323321`.

The NCBI type-material side inventory has nine exact rows for this species: alternative `ICMP 18581`, `MFLU 090228`, `BPDI16`, and synonymous `Colletotrichum ignotum` `E886` designations. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including 24 exact deposit matches and 24 direct species matches. Because no generated rows exist for `NCBITaxon:690256` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:690256` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_fructicola.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_fructicola.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:638931`, `NCBITaxon:702520`, and `NCBITaxon:912114` into `NCBITaxon:690256`, but these are only side-inventory old IDs; no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` generated `replaces` entries.
