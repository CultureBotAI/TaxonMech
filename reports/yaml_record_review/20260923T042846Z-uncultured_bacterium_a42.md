# YAML Record Review: uncultured bacterium A42

- Repository: TaxonMech
- Record: `data/taxa/bacteria/uncultured_bacterium_a42.yaml`
- Started UTC: 2026-09-23T04:28:46Z
- Finished UTC: 2026-09-23T04:28:46Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:100660`
- Label: `uncultured bacterium A42`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:90628` / `environmental samples`
- PATHS row: `data/taxa/PATHS.tsv:2053` maps the identifier to `uncultured_bacterium_a42`.

## Validation

- `just validate-strict data/taxa/bacteria/uncultured_bacterium_a42.yaml data/taxa/bacteria/uncultured_bacterium_a49.yaml data/taxa/bacteria/uncultured_bacterium_pm3.yaml data/taxa/bacteria/aeromonas_cavernicola.yaml` scanned all four files with zero errors.
- `just validate data/taxa/bacteria/uncultured_bacterium_a42.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded exactly to `NCBITaxon:100660` and preserves the seeded NCBI label, species rank, bacterial domain, genetic code `11`, and direct parent `NCBITaxon:90628`.

The YAML lineage follows the same environmental `Rhodocyclaceae` branch implied by the pinned NCBI parent: root -> cellular organisms -> Bacteria -> Pseudomonadati -> Pseudomonadota -> Betaproteobacteria -> Rhodocyclales -> Rhodocyclaceae -> environmental samples.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:17278` is the local pinned source row for `NCBITaxon:100660`, with label `uncultured bacterium A42`, rank `SPECIES`, parent `NCBITaxon:90628`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.
- The YAML has a single `NCBITAXON` source attestation for `NCBITaxon:100660` and one name assertion, matching the one local NCBI source row.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, GTDB, GOLD, LPSN, or other auxiliary rows for this identifier, label, or slug.

## Completeness

For an NCBI-only uncultured environmental placeholder with one pinned source row and no local auxiliary rows, the record is complete enough as seeded: there are no synonyms, child strain counts, taxonomy mappings, strain identifiers, descriptions, or deprecation metadata to add from the local inventory.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

No follow-up required for this record.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `uncultured_bacterium_a42`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
