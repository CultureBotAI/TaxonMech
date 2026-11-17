# YAML Record Review: Mycobacterium tuberculosis BT2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/mycobacterium_tuberculosis_bt2.yaml
- Started UTC: 2026-09-28T05:03:10Z
- Finished UTC: 2026-09-28T05:03:10Z
- Verdict: fail

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/mycobacterium_tuberculosis_bt2.yaml` |
| Identifier | `NCBITaxon:1010835` |
| Label | `Mycobacterium tuberculosis BT2` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1773` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon/GTDB M. tuberculosis strain record,
with path pinned by `data/taxa/PATHS.tsv:3923`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mycobacterium_tuberculosis_bt2.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/mycobacterium_tuberculosis_bt2.yaml data/taxa/bacteria/mycobacterium_tuberculosis_bt1.yaml data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_s397.yaml data/taxa/bacteria/bacillus_sp_nrs_866.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 82 YAML lines, 11 lineage entries, 1 GTDB taxonomy mapping, 3 exact synonyms, 1 xref, 1 NCBITAXON source attestation, 1 GTDB source attestation, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010835` in the expected seed, NCBI, GTDB mapping, GTDB-attested YAML, and `data/taxa/PATHS.tsv` rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212476`, 1 GTDB mapping, 1 native GOLD organism row, 1 native GOLD project row, 1 native GOLD analysis row, 0 GOLD aggregate rows, 11 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no MADIN row, and no StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010835` resolves to `Mycobacterium tuberculosis BT2`, rank `STRAIN`,
parent `NCBITaxon:1773`, genetic code `11`, source set `ncbitaxon|gtdb`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:1773` Mycobacterium tuberculosis. The bounded scan found no NCBI
merge row and no retained old-id row.

## Evidence

NCBI supports the strain identity, M. tuberculosis parent, two exact synonyms,
genetic code, NCBITAXON source attestation, and 2026-09-13 snapshot date.

GTDB supports `skos:closeMatch` to `GTDB:s__Mycobacterium_tuberculosis` and
7759 genome assertions.

Native GOLD rows support exact organism `Go0089928`, project `Gp0089928`, and one
analysis row, but `data/raw/gold_taxa.tsv` has no retained aggregate row.

## Completeness

No MADIN, BacDive, LPSN, MediaDive, BactoTraits, NCBI type-material, StrainInfo,
culture-collection, normalized assembly, normalized genome, or exact-target
related-record row is filed.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

## Findings

- Minor: exact native GOLD organism/project/analysis evidence is not aggregated into `data/raw/gold_taxa.tsv`, so the generated record lacks a GOLD `ORGANISM` source attestation. Fix belongs in the GOLD aggregation seeder, not in generated YAML.

- Blocker: 0
- Major: 0
- Minor: 1

## Recommended Edits

Repair GOLD aggregation for this exact NCBI taxon and regenerate the YAML.

## Follow-up Checks

Confirm `data/raw/gold_taxa.tsv` gains `NCBITaxon:1010835`.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
The GTDB closeMatch predicate is the committed kg-microbe mapping.
NCBI contributes two exact strain synonyms.
No MADIN row is filed on this exact target.
The native GOLD rows share the exact NCBI tax id.
No retained GOLD aggregate row is filed on this exact target.
No direct GOLD source attestation is expected until aggregation is repaired.
The missing aggregate is a source-retention gap, not an identity mismatch.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
Regeneration should add GOLD without changing identifier or lineage.
The ignored report probe included gitignored files.
