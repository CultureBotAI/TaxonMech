# YAML Record Review: Collybiopsis confluens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/collybiopsis_confluens.yaml
- Started UTC: 2026-09-22T13:58:33Z
- Finished UTC: 2026-09-22T14:03:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2823264` |
| Label | `Collybiopsis confluens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2607957` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/collybiopsis_confluens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/collybiopsis_confluens.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD organism rows, no NCBI type-material rows, two NCBI merged-ID side rows, seven exact StrainInfo side rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2823264`, `label: Collybiopsis confluens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2607957`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:560937`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Collybiopsis` genus; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27294`, which records one retained organism for `NCBITaxon:2823264`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2823264`. NCBI supplies all four exact synonyms and all six related synonyms present in the YAML.

The native GOLD snapshot currently has no exact organism rows for this NCBI taxon, while the maintained `data/raw/gold_organisms.tsv` aggregate row records one retained GOLD organism. The generated YAML follows that retained aggregate source, so the `GOLD` attestation count is consistent with the generated input used by this record.

The exact StrainInfo side inventory has seven deposits and seven direct DOI records for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:2823264`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/collybiopsis_confluens.yaml` plus `just validate-strict data/taxa/eukaryota/collybiopsis_confluens.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` has two side-inventory old IDs that now map into `NCBITaxon:2823264`: `NCBITaxon:176087` and `NCBITaxon:206315`. The retained retired-row inventory is empty for this target, so the absence of `replaces` values in the YAML is expected.
