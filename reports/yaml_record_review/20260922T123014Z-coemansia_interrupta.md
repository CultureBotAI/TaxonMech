# YAML Record Review: Coemansia interrupta

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coemansia_interrupta.yaml
- Started UTC: 2026-09-22T12:27:00Z
- Finished UTC: 2026-09-22T12:30:14Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1126814` |
| Label | `Coemansia interrupta` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4863` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coemansia_interrupta.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coemansia_interrupta.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, one native GOLD organism/project chain, no NCBI type-material rows, no native GOLD analyses, no BacDive or StrainInfo exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1126814`, `label: Coemansia interrupta`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4863`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:244366`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Coemansia`; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:2536`, which records one retained organism for `NCBITaxon:1126814`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1126814` with one name assertion. NCBI supplies the related synonym `Coemansia interrupta Linder, 1943` present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The native GOLD snapshot has one exact organism/project pair for this NCBI taxon: `BCRC 34489`, organism `Go0515258`, and project `Gp0436026`. No native GOLD analysis rows are currently linked to that project.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1126814` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, `data/straininfo/related_records.tsv.gz`, or the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coemansia_interrupta.yaml` plus `just validate-strict data/taxa/eukaryota/coemansia_interrupta.yaml`.

## Additional Notes

No `data/raw/ncbi_merged_ids.tsv` side rows exist for `NCBITaxon:1126814`.
