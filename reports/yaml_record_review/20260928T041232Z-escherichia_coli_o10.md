# YAML Record Review: Escherichia coli O10

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_o10.yaml
- Started UTC: 2026-09-28T04:12:32Z
- Finished UTC: 2026-09-28T04:12:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/escherichia_coli_o10.yaml` |
| Identifier | `NCBITaxon:1010798` |
| Label | `Escherichia coli O10` |
| Class | `TaxonRecord` |
| Rank | `SEROGROUP` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:562` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Escherichia coli serogroup record,
with path pinned by `data/taxa/PATHS.tsv:3890`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/escherichia_coli_o10.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/escherichia_coli_o5.yaml data/taxa/bacteria/escherichia_coli_o8.yaml data/taxa/bacteria/escherichia_coli_o9.yaml data/taxa/bacteria/escherichia_coli_o10.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 53 YAML lines, 10 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010798` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact MADIN or GTDB mapping or prior ignored report for this stem, and found the id as the parent of one NCBI strain row. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212447`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010798` resolves to `Escherichia coli O10`, rank `SEROGROUP`,
parent `NCBITaxon:562`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:562` Escherichia coli. The bounded scan found no NCBI merge row and
no retained old-id row.

## Evidence

The NCBI row supports the Escherichia coli O10 serogroup identity, E. coli
parent, genetic code, single NCBITAXON source attestation, and 2026-09-13
snapshot date.

No LPSN, GTDB, GOLD aggregate, native GOLD organism/project/analysis, BacDive,
MediaDive, MADIN, BactoTraits, NCBI type-material, StrainInfo,
culture-collection, normalized assembly, normalized genome, or exact-target
related-record row is filed.

## Completeness

No native GOLD organism, project, or analysis rows were found for this exact
NCBI taxon, and no GOLD aggregate or normalized genome/strain row was retained.
One descendant NCBI strain row uses this serogroup as parent; it is not gathered
into the exact-target attestation or `strain_count` for this parent record.

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

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
No direct MADIN row is filed for this exact target.
No NCBI synonym was present; no `taxonomy_mappings` section is expected.
No native GOLD organism, project, or analysis row was filed.
No retained GOLD aggregate row is filed on this exact target.
One NCBI strain child retains this id as parent outside exact-target rows.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The ten-line lineage reaches Escherichia coli.
The 53-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
