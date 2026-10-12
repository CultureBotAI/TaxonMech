# YAML Record Review: Clohesyomyces aquaticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clohesyomyces_aquaticus.yaml
- Started UTC: 2026-09-22T11:23:25Z
- Finished UTC: 2026-09-22T11:27:52Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1231657` |
| Label | `Clohesyomyces aquaticus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1231656` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clohesyomyces_aquaticus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clohesyomyces_aquaticus.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one exact native GOLD organism with two projects and two analyses, no NCBI type-material rows, no final raw strain rows, no StrainInfo exact rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1231657`, `label: Clohesyomyces aquaticus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1231656`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:281305`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clohesyomyces`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is also supported. `data/raw/gold_organisms.tsv:5545` records one organism for `NCBITaxon:1231657`, and the native GOLD chain includes organism `Go0111506`, projects `Gp0113499` and `Gp0113500`, and two duplicate analysis rows for the `Gp0113499` standard-draft project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1231657` with one name assertion. NCBI supplies the one related synonym present in the YAML, and the curation-history source list agrees with the two retained source attestations.

No NCBI type-material, BacDive, StrainInfo, or local generated strain rows are attached to `NCBITaxon:1231657`, so `strain_count: 0` is consistent with the maintained inputs inspected.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated related synonym from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1231657` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clohesyomyces_aquaticus.yaml` plus `just validate-strict data/taxa/eukaryota/clohesyomyces_aquaticus.yaml`.

## Additional Notes

The duplicate native GOLD analysis rows are both scoped to project `Gp0113499`; they do not inflate the generated `GOLD` source attestation, which is derived from the retained aggregate organism count.
