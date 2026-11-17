# YAML Record Review: Clavispora vitiphila

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clavispora_vitiphila.yaml
- Started UTC: 2026-09-22T11:17:28Z
- Finished UTC: 2026-09-22T11:23:24Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1212667` |
| Label | `Clavispora vitiphila` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:36910` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clavispora_vitiphila.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clavispora_vitiphila.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism/project chain, 11 NCBI type-material rows, no final raw strain rows, no StrainInfo exact rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1212667`, `label: Clavispora vitiphila`, `rank: SPECIES`, `parent_taxon: NCBITaxon:36910`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:274410`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clavispora`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:5066` records one organism for `NCBITaxon:1212667`, and the native GOLD chain includes organism `Go0705060` and project `Gp0831080` for taxon `1212667`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1212667` with one name assertion. NCBI supplies the three related synonyms present in the YAML, including the duplicated authority string for `Candida vitiphila`, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has 11 exact rows for this species under the synonym `Candida vitiphila`, covering normalized forms of `BCC 42663`, `CBS 12672`, `K70`, and `NBRC 107777`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

No BacDive, StrainInfo, or local generated strain rows are attached to `NCBITaxon:1212667`, so `strain_count: 0` is consistent with the maintained inputs inspected.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1212667` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clavispora_vitiphila.yaml` plus `just validate-strict data/taxa/eukaryota/clavispora_vitiphila.yaml`.

## Additional Notes

The native GOLD snapshot has no exact analysis rows for project `Gp0831080`; that is consistent with the YAML, which only records the aggregate organism-level GOLD source attestation.
