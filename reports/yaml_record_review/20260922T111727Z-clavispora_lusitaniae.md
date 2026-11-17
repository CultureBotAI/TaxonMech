# YAML Record Review: Clavispora lusitaniae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clavispora_lusitaniae.yaml
- Started UTC: 2026-09-22T11:11:06Z
- Finished UTC: 2026-09-22T11:17:27Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:36911` |
| Label | `Clavispora lusitaniae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:36910` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clavispora_lusitaniae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clavispora_lusitaniae.yaml` | Passed; the strict validator scanned one file and reported 0 files with errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, 15 exact native GOLD organisms joined to 16 projects and 11 analyses, 18 NCBI type-material rows, exact StrainInfo entries, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:36911`, `label: Clavispora lusitaniae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:36910`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:4184`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clavispora`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:33540`, which records 18 organisms for `NCBITaxon:36911`. A complete native GOLD join found 15 exact organism rows, 16 projects, and 11 linked analyses in the current local JSONL snapshot.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:36911` with one name assertion. NCBI supplies the three exact synonyms and four related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has 18 exact rows for this species, covering cultures from type material `CBS 6936` and `NRRL Y-11827` plus normalized type-material designations such as `ATCC 38533`, `BCRC 21387`, `IFO 10059`, `IGC 4093`, `JCM 7533`, and `MUCL 46195`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has 156 exact species-level entries with 216 deposits. Because no generated rows exist for `NCBITaxon:36911` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:36911` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clavispora_lusitaniae.yaml` plus `just validate-strict data/taxa/eukaryota/clavispora_lusitaniae.yaml`.

## Additional Notes

The retained aggregate GOLD table reports 18 organisms while exact joins over the local native GOLD JSONL snapshot currently find 15 organism IDs. That difference is confined to supporting inventories; the YAML only asserts one aggregate `GOLD` source attestation with the retained count.

`data/raw/ncbi_merged_ids.tsv` records old IDs `NCBITaxon:206410` and `NCBITaxon:5484` as merged into `NCBITaxon:36911`; no retained old-ID row exists for this target, so the generated YAML correctly omits `replaces`.
