# YAML Record Review: Colletotrichum tofieldiae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/colletotrichum_tofieldiae.yaml
- Started UTC: 2026-09-22T13:53:16Z
- Finished UTC: 2026-09-22T13:58:32Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:708197` |
| Label | `Colletotrichum tofieldiae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2707349` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/colletotrichum_tofieldiae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/colletotrichum_tofieldiae.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five retained organisms, five exact native GOLD organism/project/analysis chains, no NCBI type-material rows, no NCBI merged-ID side rows, two exact StrainInfo side rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:708197`, `label: Colletotrichum tofieldiae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2707349`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:165657`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Colletotrichum spaethianum species complex`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41751`, which records five retained organisms for `NCBITaxon:708197`; this agrees with `source_attestations[1].assertion_count: 5`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:708197`. NCBI supplies both exact synonyms and both related synonyms present in the YAML.

The native GOLD snapshot has five exact organism rows for this NCBI taxon, covering `Colletotrichum tofieldiae CBS 495.85`, `Colletotrichum tofieldiae 0861`, `Colletotrichum tofieldiae CBS 168.49`, `Colletotrichum tofieldiae CBS 127615`, and `Colletotrichum tofieldiae CBS 130851`. Those rows link to five projects and five analyses, and the exact native organism count agrees with the retained aggregate count.

The exact StrainInfo side rows cover deposits `CBS 168.49` and `ICMP 23601` for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:708197`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/colletotrichum_tofieldiae.yaml` plus `just validate-strict data/taxa/eukaryota/colletotrichum_tofieldiae.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:708197`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
