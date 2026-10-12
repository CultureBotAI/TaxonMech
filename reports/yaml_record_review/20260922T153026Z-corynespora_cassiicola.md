# YAML Record Review: Corynespora cassiicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/corynespora_cassiicola.yaml
- Started UTC: 2026-09-22T15:30:26Z
- Finished UTC: 2026-09-22T15:30:26Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:59586` |
| Label | `Corynespora cassiicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:59585` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/corynespora_cassiicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/corynascus_sepedonium.yaml data/taxa/eukaryota/corynascus_similis_cbs_632_67.yaml data/taxa/eukaryota/corynespora_cambrensis.yaml data/taxa/eukaryota/corynespora_cassiicola.yaml` | Passed; the strict validator exited successfully for the four-file batch, including this record. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, three exact native GOLD organism rows, four exact native GOLD project rows, three exact native GOLD analysis rows, no NCBI type-material rows, 45 exact direct StrainInfo records covering 77 deposits, one NCBI merged-ID side row, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:59586`, `label: Corynespora cassiicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:59585`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7491`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Corynespora` genus; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39684`, which records three retained organisms for `NCBITaxon:59586`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:59586`. NCBI supplies the exact synonym `Helminthosporium cassiicola`, plus related synonyms `Corynespora cassiicola (Berk. & M.A. Curtis) C.T. Wei, 1950` and `Helminthosporium cassiicola Berk. & M.A. Curtis, 1869`, matching the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organisms `Go0036348`, `Go0384273`, and `Go0679248`, exact projects `Gp0036348`, `Gp0036349`, `Gp0235364`, and `Gp0781235`, and three native analysis rows linked through those projects.

StrainInfo has exact direct records for the taxon, but no BacDive-backed strain row joins them into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; `strain_count: 0` is therefore consistent with the maintained generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/corynespora_cassiicola.yaml` plus `just validate-strict data/taxa/eukaryota/corynespora_cassiicola.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv:33515` maps old ID `NCBITaxon:1962294` into `NCBITaxon:59586`, but the bounded scan found no retained retired NCBI row, so no generated `replaces` entry is expected.
