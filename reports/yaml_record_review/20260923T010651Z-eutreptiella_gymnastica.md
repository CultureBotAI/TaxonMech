# YAML Record Review: Eutreptiella gymnastica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/eutreptiella_gymnastica.yaml
- Started UTC: 2026-09-23T01:06:51Z
- Finished UTC: 2026-09-23T01:06:51Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:73025` |
| Label | `Eutreptiella gymnastica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:73024` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/eutreptiella_gymnastica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/eurotium_umbrosum.yaml data/taxa/eukaryota/eutreptiella_gymnastica.yaml data/taxa/eukaryota/eutypa_lata.yaml data/taxa/eukaryota/eutypa_leptoplaca.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two exact native GOLD organism rows, no exact native GOLD project/analysis rows, two exact StrainInfo rows with two deposits, no NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:73025`, `label: Eutreptiella gymnastica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:73024`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:10250`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the euglenid genus `Eutreptiella`; the bounded scan checked all 11 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42040`, which records two retained direct organisms for `NCBITaxon:73025`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:73025`. The YAML preserves NCBI's related synonym `Eutreptiella gymnastica Throndsen, 1969`; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The native GOLD catalogs contain two exact organism rows, `Go0368662` for `Eutreptiella gymnastica CCMP 1594` and `Go0368663` for `Eutreptiella gymnastica NIES-381`, with no linked exact native GOLD project or analysis rows.

StrainInfo contains two exact target rows with two deposit designations for `Eutreptiella gymnastica`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/eutreptiella_gymnastica.yaml` plus `just validate-strict data/taxa/eukaryota/eutreptiella_gymnastica.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the two current native GOLD organism rows.
