# YAML Record Review: Emericellopsis atlantica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/emericellopsis_atlantica.yaml
- Started UTC: 2026-09-22T23:56:01Z
- Finished UTC: 2026-09-22T23:56:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2614577` |
| Label | `Emericellopsis atlantica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:45244` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/emericellopsis_atlantica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/emergomyces_pasteurianus_ep9510.yaml data/taxa/eukaryota/emericellopsis_atlantica.yaml data/taxa/eukaryota/emericellopsis_fuci.yaml data/taxa/eukaryota/emericellopsis_maritima.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism, two matching native GOLD projects, no native GOLD analyses, five NCBI type-material rows, no NCBI merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2614577`, `label: Emericellopsis atlantica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:45244`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:537118`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Emericellopsis` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:24121`, which records one retained direct organism for `NCBITaxon:2614577`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2614577`. The YAML carries both related synonyms filed for this NCBI row, `Emericellopsis atlantica L.W. Hou, Crous, Rama & Hagestad, 2021` and `Emericellopsis sp. TS7`; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The five NCBI type-material rows preserve `CBS 147198`, `CBS:147198`, and `TS7` as cultures from the holotype plus `CBS H-24579` and `CBS:H-24579` as holotype designations for `Emericellopsis atlantica`. The native GOLD catalogs contain one exact organism row, `Go0460456` for `Emericellopsis atlantica TS7`, with two matching projects, `Gp0329213` for the TS7 standard draft and `Gp0348905` for the TS7 transcriptome.

No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/emericellopsis_atlantica.yaml` plus `just validate-strict data/taxa/eukaryota/emericellopsis_atlantica.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row.
