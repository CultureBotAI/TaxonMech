# YAML Record Review: Crassisporium funariophilum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/crassisporium_funariophilum.yaml
- Started UTC: 2026-09-22T15:37:42Z
- Finished UTC: 2026-09-22T15:37:42Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1954473` |
| Label | `Crassisporium funariophilum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1954472` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/crassisporium_funariophilum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/craspedostauros_australis.yaml data/taxa/eukaryota/crassisporium_funariophilum.yaml data/taxa/eukaryota/craterellus_lutescens.yaml data/taxa/eukaryota/craterellus_tubaeformis.yaml` | Passed; the strict validator exited successfully for the four-file batch, including this record. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, two exact native GOLD project rows, no exact native GOLD analysis rows, four NCBI type-material rows, two NCBI merged-ID side rows, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1954473`, `label: Crassisporium funariophilum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1954472`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:504215`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Crassisporium` genus; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17939`, which records one retained organism for `NCBITaxon:1954473`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1954473`. NCBI supplies exact synonyms `Kuehneromyces carbonicola`, `Pachylepyrium carbonicola`, `Pachylepyrium funariophilum`, and `Pholiotina funariophila`, plus four related synonyms; all are mirrored in the YAML.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0358478` for `Crassisporium funariophilum CBS 144457` and exact projects `Gp0197235` and `Gp0304688`; no native analysis rows are filed under those projects.

NCBI has four exact type-material side rows for this taxon covering `MICH 5270`, `MICH AHS44640`, and `IB:1949/0008` designations under synonymous names. No exact StrainInfo rows or maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/crassisporium_funariophilum.yaml` plus `just validate-strict data/taxa/eukaryota/crassisporium_funariophilum.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv:29097` maps old ID `NCBITaxon:181949` into `NCBITaxon:1954473`, and `data/raw/ncbi_merged_ids.tsv:76183` maps old ID `NCBITaxon:406890` into the same current ID. The bounded scan found no retained retired NCBI rows, so no generated `replaces` entry is expected.
