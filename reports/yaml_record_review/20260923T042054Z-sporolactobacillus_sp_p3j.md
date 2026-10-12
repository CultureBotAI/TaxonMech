# YAML Record Review: Sporolactobacillus sp. P3J

- Repository: TaxonMech
- Record: `data/taxa/bacteria/sporolactobacillus_sp_p3j.yaml`
- Started UTC: 2026-09-23T04:20:54Z
- Finished UTC: 2026-09-23T04:20:54Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006587`
- Label: `Sporolactobacillus sp. P3J`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2628533` / `unclassified Sporolactobacillus`
- PATHS row: `data/taxa/PATHS.tsv:2046` maps the identifier to `sporolactobacillus_sp_p3j`.

## Validation

- `just validate-strict data/taxa/bacteria/mycoplasmoides_gallisepticum_s6.yaml data/taxa/bacteria/sporolactobacillus_sp_p3j.yaml data/taxa/bacteria/bacterium_5a_1.yaml data/taxa/bacteria/bacterium_60e.yaml` scanned all four files with zero errors.
- `just validate data/taxa/bacteria/sporolactobacillus_sp_p3j.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded exactly to `NCBITaxon:1006587` and preserves the seeded NCBI label, species rank, bacterial domain, genetic code `11`, and direct parent `NCBITaxon:2628533`.

The YAML lineage follows the same unclassified `Sporolactobacillus` branch implied by the pinned NCBI parent: root -> cellular organisms -> Bacteria -> Bacillati -> Bacillota -> Bacilli -> Caryophanales -> Sporolactobacillaceae -> Sporolactobacillus -> unclassified Sporolactobacillus.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210707` is the local pinned source row for `NCBITaxon:1006587`, with label `Sporolactobacillus sp. P3J`, rank `SPECIES`, parent `NCBITaxon:2628533`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.
- The YAML has a single `NCBITAXON` source attestation for `NCBITaxon:1006587` and one name assertion, matching the one local NCBI source row.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, GTDB, GOLD, LPSN, or other auxiliary rows for this identifier, label, or slug.

## Completeness

For an NCBI-only unclassified species placeholder with one pinned source row and no local auxiliary rows, the record is complete enough as seeded: there are no synonyms, child strain counts, taxonomy mappings, strain identifiers, descriptions, or deprecation metadata to add from the local inventory.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

No follow-up required for this record.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `sporolactobacillus_sp_p3j`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
