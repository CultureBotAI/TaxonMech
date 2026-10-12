# YAML Record Review: Corynebacterium ulcerans 05149

- Repository: TaxonMech
- Record: `data/taxa/bacteria/corynebacterium_ulcerans_05149.yaml`
- Started UTC: 2026-09-23T04:16:57Z
- Finished UTC: 2026-09-23T04:16:57Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006580`
- Label: `Corynebacterium ulcerans 05149`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:65058` / `Corynebacterium ulcerans`
- PATHS row: `data/taxa/PATHS.tsv:2044` maps the identifier to `corynebacterium_ulcerans_05149`.

## Validation

- `just validate-strict data/taxa/bacteria/uncultured_bacterium_pm5.yaml data/taxa/bacteria/defluviitoga_tunisiensis.yaml data/taxa/bacteria/uncultured_bacterium_pm8_1.yaml data/taxa/bacteria/corynebacterium_ulcerans_05149.yaml` scanned all four files with zero errors.
- `just validate data/taxa/bacteria/corynebacterium_ulcerans_05149.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded exactly to strain-level `NCBITaxon:1006580` and preserves the NCBI strain label, rank, bacterial domain, genetic code `11`, and direct parent species `NCBITaxon:65058`.

The YAML lineage follows the expected `Corynebacterium ulcerans` branch: root -> cellular organisms -> Bacteria -> Bacillati -> Actinomycetota -> Actinomycetes -> Mycobacteriales -> Corynebacteriaceae -> Corynebacterium -> Corynebacterium ulcerans.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210705` is the local pinned NCBI row for `NCBITaxon:1006580`, with label `Corynebacterium ulcerans 05149`, rank `STRAIN`, parent `NCBITaxon:65058`, two NCBI exact synonyms, sources `ncbitaxon|madin_etal`, and snapshot date `2026-09-13`.
- `data/raw/madin_taxa.tsv:362` contributes one Madin trait assertion for this strain.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, GTDB, GOLD, LPSN, or other auxiliary rows for this identifier, label, or slug beyond the NCBI and Madin rows listed above.

## Completeness

The direct NCBI synonyms and Madin count are projected. There are no local BacDive, LPSN, ATB, StrainInfo, GTDB, or GOLD rows that would justify adding strain inventory entries, nomenclature entries, genome links, taxonomy mappings, GOLD organism links, or deprecation metadata.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

No follow-up required for this record.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `corynebacterium_ulcerans_05149`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
