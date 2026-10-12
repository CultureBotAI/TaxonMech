# YAML Record Review: Colletotrichum sublineola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_sublineola.yaml
- Started UTC: 2026-09-22T13:44:37Z
- Finished UTC: 2026-09-22T13:53:15Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1173701` |
| Label | `Colletotrichum sublineola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707348` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_sublineola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_sublineola.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 149 retained organisms, 76 exact native GOLD organisms with 78 projects and four analyses, four NCBI type-material rows, one NCBI merged-ID side row, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1173701`, `label: Colletotrichum sublineola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707348`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:260347`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum graminicola species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:3800`, which records 149 retained organisms for `NCBITaxon:1173701`; this agrees with `source_attestations[1].assertion_count: 149`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1173701` with one name assertion. NCBI supplies the single exact synonym present in the YAML and no related synonyms.

The native GOLD snapshot has 76 exact organism rows for this NCBI taxon. An exact organism-ID expansion found 78 native GOLD project rows, including `Gp0016973` / `Colletotrichum sublineola S3.001`, `Gp0017395` / `Colletotrichum sublineola TX-BI-SH2A`, and `Gp0094476` / `Colletotrichum sublineola TX430BB`; an exact project-ID expansion found four linked analysis rows: `Colletotrichum sublineola TX-BI-SH2A`, `Colletotrichum sublineola TX430BB`, `Colletotrichum sublineola CgSl1`, and `Colletotrichum sublineola CsGL1`. The generated YAML correctly follows the maintained retained aggregate in `data/raw/gold_organisms.tsv`, whose 149 retained GOLD organisms exceed the native exact rows currently visible in the JSONL mirror.

The NCBI type-material side inventory has four exact `Colletotrichum sublineola` culture-from-epitype rows, `CBS 131301`, `CBS:131301`, `S3.001`, and `S:3.001`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated synonym from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:1173701` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_sublineola.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_sublineola.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` has one side-inventory old ID that now maps into `NCBITaxon:1173701`: `NCBITaxon:34410`. The retained retired-row inventory is empty for this target, so the absence of `replaces` values in the YAML is expected.
