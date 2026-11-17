# YAML Record Review: Didymella americana

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/didymella_americana.yaml
- Started UTC: 2026-09-22T22:47:57Z
- Finished UTC: 2026-09-22T22:47:57Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:749596` |
| Label | `Didymella americana` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:55170` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/didymella_americana.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/diddensiella_transvaalensis.yaml data/taxa/eukaryota/didymella_americana.yaml data/taxa/eukaryota/didymella_arachidicola.yaml data/taxa/eukaryota/didymella_glomerata.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to two projects and no analyses, no exact NCBI type-material rows, one exact StrainInfo direct record carrying one matching deposit designation, no exact BacDive rows, no final raw strain rows, two NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:749596`, `label: Didymella americana`, `rank: SPECIES`, `parent_taxon: NCBITaxon:55170`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:173283`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Didymella` genus; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42281`, which records one retained direct organism for `NCBITaxon:749596`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:749596`. The YAML carries both exact synonyms and all four related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0583398` for `Didymella americana B211-43`; two projects, `Gp0587361` and `Gp0749128`, under that organism; and no exact analysis rows linked through those project IDs.

The exact StrainInfo side inventory has one direct record and one matching `CBS 185.85` deposit designation for `NCBITaxon:749596`, but it is not present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/didymella_americana.yaml` plus `just validate-strict data/taxa/eukaryota/didymella_americana.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:1766647` and `NCBITaxon:72999` into `NCBITaxon:749596`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
