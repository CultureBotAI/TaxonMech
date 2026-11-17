# YAML Record Review: Clavispora asparagi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clavispora_asparagi.yaml
- Started UTC: 2026-09-22T11:05:00Z
- Finished UTC: 2026-09-22T11:11:05Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:255214` |
| Label | `Clavispora asparagi` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:36910` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clavispora_asparagi.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clavispora_asparagi.yaml` | Passed; the strict validator scanned one file and reported 0 files with errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism/project chain, ten NCBI type-material rows, one exact StrainInfo species entry, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:255214`, `label: Clavispora asparagi`, `rank: SPECIES`, `parent_taxon: NCBITaxon:36910`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:51839`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clavispora`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:23202` records one organism for `NCBITaxon:255214`, and the native GOLD chain includes organism `Go0705556` and project `Gp0831599` for taxon `255214`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:255214` with one name assertion. NCBI supplies the exact synonym `Candida asparagi` and the two related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has ten exact culture-from-holotype rows for this species under the synonym `Candida asparagi`, covering normalized forms of `AS 2.2526`, `CBS 9770`, `CGMCC 2.2526`, and `NRRL Y-48714`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has an exact species-level entry, `siID 280889`, with three non-type deposits matching the NCBI type-material designations. Because no generated rows exist for `NCBITaxon:255214` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:255214` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clavispora_asparagi.yaml` plus `just validate-strict data/taxa/eukaryota/clavispora_asparagi.yaml`.

## Additional Notes

The native GOLD snapshot has no exact analysis rows for project `Gp0831599`; that is consistent with the YAML, which only records the aggregate organism-level GOLD source attestation.
