# YAML Record Review: Danielia reshetovae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/danielia_reshetovae.yaml
- Started UTC: 2026-09-22T21:58:01Z
- Finished UTC: 2026-09-22T21:58:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:657494` |
| Label | `Danielia reshetovae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3312681` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/danielia_reshetovae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/danielia_oregonensis.yaml data/taxa/eukaryota/danielia_reshetovae.yaml data/taxa/eukaryota/danielozyma_ontarioensis.yaml data/taxa/eukaryota/darkera_picea.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five retained organisms, 5 exact native GOLD organisms linked to one project and no analyses, 2 exact NCBI type-material rows, one exact StrainInfo direct record carrying 3 matching deposit designations that was not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:657494`, `label: Danielia reshetovae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3312681`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:152107`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Danielia` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40600`, which records five retained organisms for `NCBITaxon:657494`; this agrees with `source_attestations[1].assertion_count: 5`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:657494`. The YAML carries the one exact synonym and all three related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD rows contain organisms `Go0621321`, `Go0621322`, `Go0621323`, `Go0621324`, and `Go0621325`; one project, `Gp0831023`, links through `Go0621324`; the local native GOLD analysis export has no exact row that links through that project.

The NCBI type-material inventory contributes two exact rows under the synonym taxon name `Clavispora reshetovae`, covering `CBS 11556` and `CBS:11556` as culture-from-holotype designations.

One exact StrainInfo direct record is keyed to `NCBITaxon:657494` and carries deposit designations `DSM 105235`, `MUCL 52545`, and `CBS 11556`, but it has not been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/danielia_reshetovae.yaml` plus `just validate-strict data/taxa/eukaryota/danielia_reshetovae.yaml`.

## Additional Notes

None.
