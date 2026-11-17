# YAML Record Review: Geotrichum siamense (nom. inval.)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dipodascus_siamensis.yaml
- Started UTC: 2026-09-22T23:13:47Z
- Finished UTC: 2026-09-22T23:13:47Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2862415` |
| Label | `Geotrichum siamense (nom. inval.)` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2642240` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dipodascus_siamensis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dipodascus_albidus.yaml data/taxa/eukaryota/dipodascus_australiensis.yaml data/taxa/eukaryota/dipodascus_geniculatus.yaml data/taxa/eukaryota/dipodascus_siamensis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism linked to one project and no analyses, no exact NCBI type-material rows, no exact StrainInfo or BacDive rows, no final raw strain rows, one NCBI merged-ID side row with no retained old-taxon row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2862415`, `label: Geotrichum siamense (nom. inval.)`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2642240`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:565588`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Geotrichum`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27805`, which records one retained direct organism for `NCBITaxon:2862415`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2862415`. The YAML carries both exact synonyms and all three related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0704980` for `Dipodascus siamensis CBS 10929`, and one project, `Gp0830997`, under that organism; the native GOLD analysis table has no exact linked analyses for that project ID.

The NCBI merged-ID side inventory records retired `NCBITaxon:643071` as merged into `NCBITaxon:2862415`, but the old ID has no retained row in `data/raw/ncbitaxon_taxa.tsv`; that is consistent with the generated record carrying no `replaces` entry.

No exact NCBI type-material, StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dipodascus_siamensis.yaml` plus `just validate-strict data/taxa/eukaryota/dipodascus_siamensis.yaml`.

## Additional Notes

The YAML filename and scope reason retain the older `Dipodascus siamensis` label, while NCBI now labels `NCBITaxon:2862415` as `Geotrichum siamense (nom. inval.)` and preserves `Dipodascus siamensis` and `Geotrichum siamense` as exact synonyms on the same taxon ID.
