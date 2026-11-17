# YAML Record Review: Climacocystis borealis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/climacocystis_borealis.yaml
- Started UTC: 2026-09-22T11:17:28Z
- Finished UTC: 2026-09-22T11:23:24Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:239101` |
| Label | `Climacocystis borealis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:202692` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/climacocystis_borealis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/climacocystis_borealis.yaml` | Passed; the strict validator scanned one file and reported 0 files with errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism with two projects, no NCBI type-material rows, exact StrainInfo entries, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:239101`, `label: Climacocystis borealis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:202692`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:46941`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Climacocystis`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:21966` records one organism for `NCBITaxon:239101`, and the native GOLD chain includes organism `Go0115660` plus projects `Gp0119921` and `Gp0119922`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:239101` with one name assertion. NCBI supplies the exact synonym `Polyporus borealis` and the two related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

StrainInfo has 11 exact species-level entries with 11 deposits. Because no generated rows exist for `NCBITaxon:239101` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:239101` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/climacocystis_borealis.yaml` plus `just validate-strict data/taxa/eukaryota/climacocystis_borealis.yaml`.

## Additional Notes

The native GOLD snapshot has no exact analysis rows for projects `Gp0119921` and `Gp0119922`; that is consistent with the YAML, which only records the aggregate organism-level GOLD source attestation.
