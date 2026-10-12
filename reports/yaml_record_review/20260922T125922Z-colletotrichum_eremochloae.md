# YAML Record Review: Colletotrichum eremochloae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_eremochloae.yaml
- Started UTC: 2026-09-22T12:56:00Z
- Finished UTC: 2026-09-22T12:59:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1173702` |
| Label | `Colletotrichum eremochloae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707348` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_eremochloae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_eremochloae.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, one current native GOLD organism with two projects, two NCBI type-material rows, no native GOLD analyses, no BacDive or StrainInfo exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1173702`, `label: Colletotrichum eremochloae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707348`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:260348`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum graminicola species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:3801`, which records two retained organisms for `NCBITaxon:1173702`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1173702` with one name assertion. NCBI supplies the related synonym `Colletotrichum eremochloae J.A. Crouch & Tomaso-Peterson 2012` present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism, `CBS129661` / `Go0102820`, and two projects for this NCBI taxon: `Gp0102820` and `Gp0102821`. No native GOLD analysis rows are currently linked to those projects.

The NCBI type-material side inventory has two exact culture-from-holotype rows for this species, `CBS 129661` and `CBS:129661`. Those rows support an external type-material relationship for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1173702` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, `data/straininfo/related_records.tsv.gz`, or the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_eremochloae.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_eremochloae.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:1173702`.

The retained GOLD aggregate count is two, while the current local native GOLD JSONL snapshot exposes one exact organism with two linked projects; the generated source attestation follows the retained aggregate row.
