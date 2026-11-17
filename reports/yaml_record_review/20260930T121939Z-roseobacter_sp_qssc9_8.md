# YAML Record Review: Roseobacter sp. QSSC9-8

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/roseobacter_sp_qssc9_8.yaml
- Started UTC: 2026-09-30T12:19:39Z
- Finished UTC: 2026-09-30T12:19:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/roseobacter_sp_qssc9_8.yaml` |
| Identifier | `NCBITaxon:101403` |
| Label | `Roseobacter sp. QSSC9-8` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:196798` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Roseobacter record, with path pinned
by `data/taxa/PATHS.tsv:7223`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/roseobacter_sp_qssc9_8.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:101403` in the expected seed, NCBI, YAML, and `data/taxa/PATHS.tsv` rows; found no exact GTDB mapping, and the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17533`, 10 checked lineage entries with no missing rows or mismatches, no native GOLD organism, project, or analysis rows, 0 GOLD aggregate rows, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no auxiliary rows, and no StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101403` resolves to `Roseobacter sp. QSSC9-8`, rank `SPECIES`,
parent `NCBITaxon:196798`, genetic code `11`, source set `ncbitaxon`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:196798` unclassified Roseobacter. The bounded scan found no NCBI
merge row and no retained old-id row.

## Evidence

The NCBI row supports the Roseobacter identity, unclassified-Roseobacter
parent, genetic code, NCBITAXON source attestation, and 2026-09-13 snapshot
date.

No native GOLD organism, project, or analysis rows and no retained GOLD
aggregate row are filed for this exact NCBI taxon.

## Completeness

No MADIN, BacDive, LPSN, GTDB, GOLD, MediaDive, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly,
normalized genome, or exact-target related-record row is filed.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

## Findings

No findings.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

No follow-up needed.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
The rank is the NCBI retained rank for this Roseobacter record.
The parent is NCBI's unclassified Roseobacter placeholder.
No NCBI synonym was present; no `taxonomy_mappings` section is expected.
No GTDB row is expected for this exact Roseobacter target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The ten-line lineage reaches unclassified Roseobacter.
The 54-line YAML shape omits all non-NCBI sections.
The bounded scan found no native GOLD evidence.
The record has no MADIN row.
The source set is just `ncbitaxon`.
The boundary `NCBITaxon:` probe excluded longer neighboring identifiers.
The ignored report probe included gitignored files.
