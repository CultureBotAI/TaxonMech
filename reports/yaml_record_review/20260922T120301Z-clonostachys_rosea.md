# YAML Record Review: Clonostachys rosea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_rosea.yaml
- Started UTC: 2026-09-22T11:58:23Z
- Finished UTC: 2026-09-22T12:03:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:29856` |
| Label | `Clonostachys rosea` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:110564` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_rosea.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/clonostachys_rosea.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with ten retained organisms, eight current native GOLD exact organism rows, 11 native GOLD project rows, three native GOLD analysis rows, eight NCBI type-material rows, five NCBI merged-ID side rows, exact StrainInfo species/deposit matches, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:29856`, `label: Clonostachys rosea`, `rank: SPECIES`, `parent_taxon: NCBITaxon:110564`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:3282`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clonostachys`; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:29885`, which records ten retained direct organisms for `NCBITaxon:29856`. The native GOLD snapshot also has eight exact organism rows and 11 project rows for this NCBI taxon, including `Gliocladium roseum 321H`, `Gliocladium roseum 321U`, `Clonostachys rosea CBS125111`, `Clonostachys rosea 67-1`, `Clonostachys rosea YKD0085`, `Clonostachys rosea 406A_c4.1`, `Clonostachys rosea B403_7`, and `Clonostachys rosea CLO192961`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:29856` with one name assertion. NCBI supplies all 20 synonyms in the YAML: 13 exact synonyms and seven related synonyms.

The native GOLD snapshot has three exact analysis rows for projects under this taxon: `Clonostachys rosea 67-1` on `Gp0117568`, `Clonostachys rosea YKD0085` on `Gp0149884`, and `Clonostachys rosea CLO192961` on `Gp0645992`. These rows corroborate direct GOLD evidence for the taxon, while the YAML assertion count correctly follows the retained aggregate count of ten organisms.

The NCBI type-material side inventory has eight exact rows for this species. They include lectotype `PAD S00005` under `Nectria congesta`, isolectotype `PAD S00016` under `Nectria phyllostachydis`, and four neotype spelling variants for `CBS 710.86` under `Penicillium roseum`.

StrainInfo has many exact species-level side inventory rows: 207 exact deposit matches and 185 direct species matches. Because no generated rows exist for `NCBITaxon:29856` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:29856` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_rosea.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_rosea.yaml`.

## Additional Notes

The retained aggregate GOLD table has ten organisms for this taxon even though the local native GOLD `organisms.jsonl.gz` exact join contains eight current organism rows. That difference is confined to the supporting inventories; the YAML correctly follows the retained aggregate `GOLD` source attestation.

`data/raw/ncbi_merged_ids.tsv` records old IDs `NCBITaxon:110566`, `NCBITaxon:2741099`, `NCBITaxon:2741106`, `NCBITaxon:29854`, and `NCBITaxon:29858` as merged into `NCBITaxon:29856`; no retained old-ID row exists for this target, so the generated YAML correctly omits `replaces`.
