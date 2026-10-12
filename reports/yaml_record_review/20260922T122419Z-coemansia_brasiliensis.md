# YAML Record Review: Coemansia brasiliensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coemansia_brasiliensis.yaml
- Started UTC: 2026-09-22T12:21:02Z
- Finished UTC: 2026-09-22T12:24:19Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2650707` |
| Label | `Coemansia brasiliensis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4863` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coemansia_brasiliensis.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/coemansia_brasiliensis.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one current native GOLD organism/project chain, exact StrainInfo species/deposit matches, no native GOLD analyses, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2650707`, `label: Coemansia brasiliensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4863`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:540353`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coemansia`; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:24278`, which records one retained organism for `NCBITaxon:2650707`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2650707` with one name assertion. NCBI supplies the related synonym `Coemansia brasiliensis Thaxt. ex Linder, 1943` present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism row for `Coemansia brasiliensis NRRL 1566` on organism `Go0532379` and one resequencing project row on `Gp0478831`; no native GOLD analysis rows are currently linked to that project.

StrainInfo has exact species-level side inventory rows, including deposits for `MUCL 14422`, `ATCC 12438`, and `NRRL 1566`. Because no generated rows exist for `NCBITaxon:2650707` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:2650707` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coemansia_brasiliensis.yaml` plus `just validate-strict data/taxa/eukaryota/coemansia_brasiliensis.yaml`.

## Additional Notes

No `data/raw/ncbi_type_material.tsv` or `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:2650707`.
