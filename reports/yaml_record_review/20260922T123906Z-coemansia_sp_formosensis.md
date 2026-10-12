# YAML Record Review: Coemansia sp. 'formosensis'

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coemansia_sp_formosensis.yaml
- Started UTC: 2026-09-22T12:35:20Z
- Finished UTC: 2026-09-22T12:39:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:327750` |
| Label | `Coemansia sp. 'formosensis'` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2641067` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coemansia_sp_formosensis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coemansia_sp_formosensis.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one native GOLD organism/project chain, no NCBI type-material rows, no native GOLD analyses, no BacDive or StrainInfo exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:327750`, `label: Coemansia sp. 'formosensis'`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2641067`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:67019`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Coemansia`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy placeholder species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32194`, which records one retained organism for `NCBITaxon:327750`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:327750` with one name assertion. The NCBI source row has no exact, broad, or related synonyms, which agrees with the absent `synonyms` block in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism/project pair for this NCBI taxon: `NRRL 5531`, organism `Go0470755`, and project `Gp0345243`. No native GOLD analysis rows are currently linked to that project.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`; NCBI contributed no synonyms to emit.

The bounded scan found no exact target rows for `NCBITaxon:327750` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, `data/straininfo/related_records.tsv.gz`, or the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coemansia_sp_formosensis.yaml` plus `just validate-strict data/taxa/eukaryota/coemansia_sp_formosensis.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:327750`.

The exact native GOLD organism row for `Go0470755` uses the organism string `Coemansia formosensis NRRL 5531` while storing `ORGANISM NCBI TAX ID` `327750`; the generated taxon attestation is ID-based and does not promote the GOLD organism string into the NCBI-backed placeholder label.
