# YAML Record Review: uncultured bacterium PM4-2

- Repository: TaxonMech
- Record: `data/taxa/bacteria/uncultured_bacterium_pm4_2.yaml`
- Started UTC: 2026-09-23T04:12:31Z
- Finished UTC: 2026-09-23T04:12:31Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:100656`
- Label: `uncultured bacterium PM4-2`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:90628` / `environmental samples`
- PATHS row: `data/taxa/PATHS.tsv:2040` maps the identifier to `uncultured_bacterium_pm4_2`.

## Validation

- `just validate-strict data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_t0131.yaml data/taxa/bacteria/klebsiella_michiganensis_kctc_1686.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_101655.yaml data/taxa/bacteria/uncultured_bacterium_pm4_2.yaml` completed successfully for this batch.
- `just validate data/taxa/bacteria/uncultured_bacterium_pm4_2.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded exactly to `NCBITaxon:100656` and preserves the seeded NCBI label, species rank, bacterial domain, genetic code `11`, and direct parent `NCBITaxon:90628`.

The YAML lineage follows the same environmental `Rhodocyclaceae` branch implied by the pinned NCBI parent: root -> cellular organisms -> Bacteria -> Pseudomonadati -> Pseudomonadota -> Betaproteobacteria -> Rhodocyclales -> Rhodocyclaceae -> environmental samples.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:17274` is the local pinned source row for `NCBITaxon:100656`, with label `uncultured bacterium PM4-2`, rank `SPECIES`, parent `NCBITaxon:90628`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.
- The YAML has a single `NCBITAXON` source attestation for `NCBITaxon:100656` and one name assertion, matching the one local NCBI source row.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, GTDB, GOLD, LPSN, or other auxiliary rows for this identifier, hyphenated label, or slug.

## Completeness

For an NCBI-only uncultured environmental placeholder with one pinned source row and no local auxiliary rows, the record is complete enough as seeded: there are no synonyms, child strain counts, taxonomy mappings, strain identifiers, descriptions, or deprecation metadata to add from the local inventory.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

No follow-up required for this record.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `uncultured_bacterium_pm4_2`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
