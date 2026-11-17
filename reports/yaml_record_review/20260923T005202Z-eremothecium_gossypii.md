# YAML Record Review: Eremothecium gossypii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/eremothecium_gossypii.yaml
- Started UTC: 2026-09-23T00:52:02Z
- Finished UTC: 2026-09-23T00:52:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:33169` |
| Label | `Eremothecium gossypii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:33170` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/eremothecium_gossypii.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/eremothecium_gossypii.yaml data/taxa/eukaryota/eremothecium_sinecaudum.yaml data/taxa/eukaryota/erysiphe_necator.yaml data/taxa/eukaryota/erysiphe_neolycopersici.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis row, two NCBI type-material rows, eight exact StrainInfo rows with 19 deposits, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:33169`, `label: Eremothecium gossypii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:33170`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:3546`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Eremothecium` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32328`, which records one retained direct organism for `NCBITaxon:33169`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:33169`. The YAML preserves NCBI's exact synonyms `Ashbya gossypii (S.F. Ashby & W. Nowell) Guillierm., 1928` and `Nematospora gossypii`, plus its two related synonyms; NCBI supplies no broad synonyms and no old-ID side rows.

The native GOLD catalogs contain one exact organism row, `Go0000589` for `Eremothecium gossypii ATCC 10895`, with one matching project, `Gp0000589`, and one native GOLD analysis row linked through `AP PROJECT GOLD IDS: Gp0000589`.

NCBI type-material evidence contributes the `CBS 109.26` and `CBS:109.26` reference-material aliases for `Nematospora gossypii`. StrainInfo contains eight exact target rows with 19 deposit designations for `Eremothecium gossypii`; those side rows do not produce BacDive-derived local strain children for this taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/eremothecium_gossypii.yaml` plus `just validate-strict data/taxa/eukaryota/eremothecium_gossypii.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row. The NCBI type-material table contributes evidence but does not create child strain records by itself.
