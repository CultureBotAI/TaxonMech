# YAML Record Review: Clonostachys rosea f. catenulata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_rosea_f_catenulata.yaml
- Started UTC: 2026-09-22T11:58:23Z
- Finished UTC: 2026-09-22T12:03:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:62888` |
| Label | `Clonostachys rosea f. catenulata` |
| Rank | `FORMA` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29856` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_rosea_f_catenulata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clonostachys_rosea_f_catenulata.yaml` | Passed; the strict validator exited successfully for one file. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, four NCBI type-material rows, exact StrainInfo species/deposit matches, no current native GOLD exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:62888`, `label: Clonostachys rosea f. catenulata`, `rank: FORMA`, `parent_taxon: NCBITaxon:29856`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7929`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clonostachys rosea`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy forma ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40019`, which records one retained organism for `NCBITaxon:62888`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:62888` with one name assertion. NCBI supplies the exact synonym `Gliocladium catenulatum` and the two related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has four exact rows for this forma: `CBS 154.27`, `CBS:154.27`, `MUCL 7575`, and `MUCL:7575` under `Gliocladium catenulatum`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including a type-strain `MUCL 7575` deposit and a matching `CBS 154.27` deposit under `SI-ID73462`. Because no generated rows exist for `NCBITaxon:62888` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:62888` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_rosea_f_catenulata.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_rosea_f_catenulata.yaml`.

## Additional Notes

The retained aggregate GOLD table has a row for this forma even though the local native GOLD `organisms.jsonl.gz`, `projects.jsonl.gz`, and `analyses.jsonl.gz` exact joins did not contain a current organism, project, or analysis for `62888`. That difference is confined to the supporting inventories; the YAML only asserts one aggregate `GOLD` source attestation.
