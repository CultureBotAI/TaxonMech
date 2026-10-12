# YAML Record Review: Clavispora phyllophila

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clavispora_phyllophila.yaml
- Started UTC: 2026-09-22T11:11:06Z
- Finished UTC: 2026-09-22T11:17:27Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1212665` |
| Label | `Clavispora phyllophila` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:36910` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clavispora_phyllophila.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clavispora_phyllophila.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism/project chain, 11 NCBI type-material rows, no final raw strain rows, no StrainInfo exact rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1212665`, `label: Clavispora phyllophila`, `rank: SPECIES`, `parent_taxon: NCBITaxon:36910`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:274409`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clavispora`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:5065` records one organism for `NCBITaxon:1212665`, and the native GOLD chain includes organism `Go0705059` and project `Gp0831079` for taxon `1212665`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1212665` with one name assertion. NCBI supplies the four related synonyms present in the YAML, including the duplicated authority string for `Candida phyllophila`, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has 11 exact rows for this species, covering holotype spellings for `CBS 12671` and normalized type-material designations for `BCC 42662`, `K59`, and `NBRC 107776`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

No BacDive, StrainInfo, or local generated strain rows are attached to `NCBITaxon:1212665`, so `strain_count: 0` is consistent with the maintained inputs inspected.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1212665` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clavispora_phyllophila.yaml` plus `just validate-strict data/taxa/eukaryota/clavispora_phyllophila.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` records old ID `NCBITaxon:1212666` as merged into `NCBITaxon:1212665`; no retained old-ID row exists for this target, so the generated YAML correctly omits `replaces`.
