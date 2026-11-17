# YAML Record Review: Clonostachys solani

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_solani.yaml
- Started UTC: 2026-09-22T12:03:02Z
- Finished UTC: 2026-09-22T12:06:37Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:160281` |
| Label | `Clonostachys solani` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:110564` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_solani.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clonostachys_solani.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, one exact native GOLD organism/project/analysis chain, two NCBI merged-ID side rows, exact StrainInfo species/deposit matches, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:160281`, `label: Clonostachys solani`, `rank: SPECIES`, `parent_taxon: NCBITaxon:110564`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:33084`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clonostachys`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12929`, which records two retained direct organisms for `NCBITaxon:160281`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:160281` with one name assertion. NCBI supplies all four exact synonyms and six related synonyms in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism row for `Clonostachys solani CSOL1703` on organism `Go0632169`, one project row on `Gp0645993`, and one matching analysis row. These rows corroborate GOLD evidence for the taxon, while the YAML assertion count correctly follows the retained aggregate count of two organisms.

StrainInfo has exact species-level side inventory rows, including 21 exact deposit matches and 17 direct species matches. Because no generated rows exist for `NCBITaxon:160281` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:160281` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_solani.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_solani.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` records old IDs `NCBITaxon:122657` and `NCBITaxon:160269` as merged into `NCBITaxon:160281`; no retained old-ID rows exist for this target, so the generated YAML correctly omits `replaces`.
