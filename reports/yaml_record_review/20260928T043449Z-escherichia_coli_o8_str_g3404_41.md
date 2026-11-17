# YAML Record Review: Escherichia coli O8 str. G3404-41

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_o8_str_g3404_41.yaml
- Started UTC: 2026-09-28T04:34:49Z
- Finished UTC: 2026-09-28T04:34:49Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/escherichia_coli_o8_str_g3404_41.yaml` |
| Identifier | `NCBITaxon:1010806` |
| Label | `Escherichia coli O8 str. G3404-41` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1010796` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon/GOLD/MADIN Escherichia coli strain record,
with path pinned by `data/taxa/PATHS.tsv:3899`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/escherichia_coli_o8_str_g3404_41.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/escherichia_coli_o8_str_g3404_41.yaml data/taxa/bacteria/escherichia_coli_o9_str_bi316_42.yaml data/taxa/bacteria/escherichia_coli_o10_str_bi8337_41.yaml data/taxa/bacteria/escherichia_coli_o16_str_f11119_41.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 67 YAML lines, 11 lineage entries, 1 NCBITAXON source attestation, 1 GOLD source attestation, 1 MADIN source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010806` in the expected seed, NCBI, GOLD/MADIN-attested YAML, and `data/taxa/PATHS.tsv` rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212455`, 1 GOLD aggregate row, 1 native GOLD organism row, 1 native GOLD project row, 1 MADIN row, 11 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no LPSN, GTDB, MediaDive, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010806` resolves to `Escherichia coli O8 str. G3404-41`, rank
`STRAIN`, parent `NCBITaxon:1010796`, genetic code `11`, source set
`ncbitaxon|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:1010796` Escherichia coli O8. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the Escherichia coli O8 str. G3404-41 identity, E. coli
O8 parent, genetic code, NCBITAXON source attestation, and 2026-09-13 snapshot
date. GOLD rows support one aggregate and native organism/project evidence row.
The MADIN row supports the six-assertion MADIN source attestation.

No LPSN, GTDB, native GOLD analysis, BacDive, MediaDive, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly, normalized
genome, or exact-target related-record row is filed.

## Completeness

The native GOLD organism is `Go0011792` and the project is `Gp0011792`; no
native GOLD analysis row was filed for this exact NCBI taxon. No BacDive, LPSN,
MediaDive, BactoTraits, type-material, StrainInfo, normalized strain, normalized
genome, or exact-target related-record row was filed.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
The direct GOLD row is represented as one `ORGANISM` source attestation.
The direct MADIN row is represented as one `TRAIT_ASSERTION` attestation.
No NCBI synonym was present; no `taxonomy_mappings` section is expected.
No retained GOLD aggregate row beyond the exact 1-count row is filed.
No native GOLD analysis row was filed.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
The 11-line lineage reaches Escherichia coli O8.
The 67-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
