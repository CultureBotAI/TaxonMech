# YAML Record Review: gamma proteobacterium GE35

- Repository: TaxonMech
- Record: `data/taxa/bacteria/gamma_proteobacterium_ge35.yaml`
- Started UTC: 2026-09-23T04:09:04Z
- Finished UTC: 2026-09-23T04:09:04Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006489`
- Label: `gamma proteobacterium GE35`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:33811` / `unclassified Gammaproteobacteria`
- PATHS row: `data/taxa/PATHS.tsv:2033` maps the identifier to `gamma_proteobacterium_ge35`.

## Validation

- `just validate-strict data/taxa/bacteria/gamma_proteobacterium_ge35.yaml data/taxa/bacteria/gamma_proteobacterium_r001.yaml data/taxa/bacteria/gamma_proteobacterium_sgm02.yaml data/taxa/bacteria/gamma_proteobacterium_y001.yaml` scanned all four files with zero errors.
- `just validate data/taxa/bacteria/gamma_proteobacterium_ge35.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded exactly to `NCBITaxon:1006489` and preserves the seeded NCBI label, species rank, bacterial domain, genetic code `11`, and direct parent `NCBITaxon:33811`.

The YAML lineage follows the same unclassified `Gammaproteobacteria` branch implied by the pinned NCBI parent: root -> cellular organisms -> Bacteria -> Pseudomonadati -> Pseudomonadota -> Gammaproteobacteria -> unclassified Gammaproteobacteria.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210697` is the local pinned source row for `NCBITaxon:1006489`, with label `gamma proteobacterium GE35`, rank `SPECIES`, parent `NCBITaxon:33811`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.
- The YAML has a single `NCBITAXON` source attestation for `NCBITaxon:1006489` and one name assertion, matching the one local NCBI source row.
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

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `gamma_proteobacterium_ge35`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
