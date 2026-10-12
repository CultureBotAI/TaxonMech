# YAML Record Review: Psilocybe cubensis

- Verdict: pass
- Target: `data/taxa/eukaryota/psilocybe_cubensis.yaml`
- Identifier: `NCBITaxon:181762`

## Target

Reviewed the complete 84-line YAML record for Psilocybe cubensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `psilocybe_cubensis`.

## Validation

- `just validate data/taxa/eukaryota/psilocybe_cubensis.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/psilocybe_cubensis.yaml data/taxa/eukaryota/psilocybe_cyanescens.yaml data/taxa/eukaryota/psilocybe_subaeruginosa.yaml data/taxa/eukaryota/pteridomonas_danica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:36421` retains `NCBITaxon:181762` as `Psilocybe cubensis`, rank `SPECIES`, parent `NCBITaxon:71950`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:54359`, with reason `attested rule: Psilocybe cubensis, 2 sources incl. NCBI`.
- NCBI lists 1 exact synonym, 3 related synonyms, and 0 broad synonyms for the taxon, matching the 4 synonym assertions in the YAML.
- All 14 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:181762`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:16113` reports `organism_count: 1` for `NCBITaxon:181762`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 1 project row, and 1 analysis row for this taxon.
- NCBI has 4 holotype rows for `Stropharia cubensis` at `data/raw/ncbi_type_material.tsv:62182` through `data/raw/ncbi_type_material.tsv:62185`: `NY 761563`, `NY-761563`, `NY761563`, and `NY:761563`.
- Local StrainInfo records have 14 direct exact taxon rows and 17 exact deposit entries for `NCBITaxon:181762`; an exact numeric-boundary scan of `data/straininfo/records.jsonl.gz` found the same 14 direct records.
- BacDive has 0 exact local rows for `NCBITaxon:181762`.

## Completeness

- Generated raw strain tables contain 0 target rows across `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary generated sources contain 0 target rows across BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive.
- Generated StrainInfo overlays contain 0 rows across `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- The YAML correctly carries `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The local StrainInfo cache has exact rows for the taxon, but no generated StrainInfo overlay or raw strain table currently contributes a strain assertion to this YAML.
