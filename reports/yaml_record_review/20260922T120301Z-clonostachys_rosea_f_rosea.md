# YAML Record Review: Clonostachys rosea f. rosea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_rosea_f_rosea.yaml
- Started UTC: 2026-09-22T11:58:23Z
- Finished UTC: 2026-09-22T12:03:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:768735` |
| Label | `Clonostachys rosea f. rosea` |
| Rank | `FORMA` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29856` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_rosea_f_rosea.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/clonostachys_rosea_f_rosea.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, four NCBI type-material rows, no exact StrainInfo species entry, no current native GOLD exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:768735`, `label: Clonostachys rosea f. rosea`, `rank: FORMA`, `parent_taxon: NCBITaxon:29856`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:178961`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clonostachys rosea`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy forma ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42652`, which records one retained organism for `NCBITaxon:768735`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:768735` with one name assertion. NCBI supplies the related forma synonym present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has four exact neotype rows for `Penicillium roseum`, spelling `CBS 710.86` with spaces, hyphens, no delimiter, or a colon. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

The bounded scan found no exact StrainInfo species entry and no generated rows for `NCBITaxon:768735` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, so the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:768735` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_rosea_f_rosea.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_rosea_f_rosea.yaml`.

## Additional Notes

The retained aggregate GOLD table has a row for this forma even though the local native GOLD `organisms.jsonl.gz`, `projects.jsonl.gz`, and `analyses.jsonl.gz` exact joins did not contain a current organism, project, or analysis for `768735`. That difference is confined to the supporting inventories; the YAML only asserts one aggregate `GOLD` source attestation.
