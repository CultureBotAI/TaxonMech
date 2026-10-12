# YAML Record Review: Clonostachys solani f. nigrovirens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/clonostachys_solani_f_nigrovirens.yaml
- Started UTC: 2026-09-22T12:03:02Z
- Finished UTC: 2026-09-22T12:06:37Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:122091` |
| Label | `Clonostachys solani f. nigrovirens` |
| Rank | `FORMA` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:160281` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/clonostachys_solani_f_nigrovirens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/clonostachys_solani_f_nigrovirens.yaml` | Passed; the strict validator reported 0 errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row, five NCBI type-material rows, exact StrainInfo species/deposit matches, no current native GOLD exact rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:122091`, `label: Clonostachys solani f. nigrovirens`, `rank: FORMA`, `parent_taxon: NCBITaxon:160281`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:23056`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Clonostachys solani`; the bounded scan checked all 17 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy forma ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:5310`, which records one retained organism for `NCBITaxon:122091`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:122091` with one name assertion. NCBI supplies the exact synonym `Gliocladium nigrovirens` and the two related synonyms present in the YAML, and the curation-history source list agrees with the two retained source attestations.

The NCBI type-material side inventory has five exact rows for `Gliocladium nigrovirens`: `CBS 183.30`, `CBS:183.30`, `VKM F-3258`, `VKM:F-3258`, and `VKM:F:3258`. Those rows support external type-material relationships for the same NCBI taxon, but the current generated `TaxonRecord` does not attempt to embed type material directly.

StrainInfo has exact species-level side inventory rows, including a type-strain `MUCL 39113` deposit and a matching `CBS 183.30` deposit under `SI-ID79794`. Because no generated rows exist for `NCBITaxon:122091` in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or the final raw strain tables, the YAML correctly omits StrainInfo-derived strain, assembly, and related-record evidence.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows for `NCBITaxon:122091` in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`. It also found no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/clonostachys_solani_f_nigrovirens.yaml` plus `just validate-strict data/taxa/eukaryota/clonostachys_solani_f_nigrovirens.yaml`.

## Additional Notes

The retained aggregate GOLD table has a row for this forma even though the local native GOLD `organisms.jsonl.gz`, `projects.jsonl.gz`, and `analyses.jsonl.gz` exact joins did not contain a current organism, project, or analysis for `122091`. That difference is confined to the supporting inventories; the YAML only asserts one aggregate `GOLD` source attestation.
