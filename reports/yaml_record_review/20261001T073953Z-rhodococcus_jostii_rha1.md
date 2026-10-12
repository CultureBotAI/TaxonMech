# YAML Record Review: Rhodococcus jostii RHA1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/rhodococcus_jostii_rha1.yaml
- Started UTC: 2026-10-01T07:39:53Z
- Finished UTC: 2026-10-01T07:39:53Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/rhodococcus_jostii_rha1.yaml` |
| Identifier | `NCBITaxon:101510` |
| Label | `Rhodococcus jostii RHA1` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:132919` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon/GTDB/MADIN strain record with path pinned by
`data/taxa/PATHS.tsv:8335`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/rhodococcus_jostii_rha1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 90 YAML lines, 10 lineage entries, 3 source attestations, 5 synonyms, 1 taxonomy mapping, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact local scans | Found the seed row, legacy page-path row, retained NCBI row, GTDB mapping row, MADIN row, NCBI merge side row, YAML, and `data/taxa/PATHS.tsv` entries expected for `NCBITaxon:101510`; the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17577`, 10 checked lineage entries with no missing rows or mismatches, 1 exact GTDB `skos:closeMatch` row with 9 genomes, 1 MADIN row with 8 trait assertions, 1 NCBI merge side row from `NCBITaxon:269090`, 0 GOLD rows, no BacDive rows, no type-material rows, no auxiliary rows, and no StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101510` resolves to retained NCBI strain `Rhodococcus jostii RHA1`,
rank `STRAIN`, parent `NCBITaxon:132919`, genetic code `11`, and source set
`ncbitaxon|gtdb|madin_etal` in the 2026-09-13 NCBI snapshot row.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:132919` `Rhodococcus jostii`. The bounded scan found one NCBI
merged-ID side row mapping old `NCBITaxon:269090` onto this retained target.

The GTDB side evidence is the exact `GTDB:s__Rhodococcus_F_jostii_A`
`skos:closeMatch` row for `NCBITaxon:101510` with genome count 9. The MADIN
side evidence is a single exact row with 8 trait assertions.

## Evidence

The retained NCBI row supplies the strain identity, parent, four NCBI
synonyms, source set, and taxonomy snapshot date. The YAML mirrors all four
NCBI synonyms and keeps the GTDB species representative as both a taxonomy
mapping and an xref.

No native GOLD organism, retained GOLD aggregate, BacDive, type-material,
StrainInfo, culture-collection, normalized assembly, or exact-target
related-record row is filed for this exact strain taxon.

## Completeness

The generated record contains all NCBI synonyms, the exact GTDB mapping and
corresponding xref, and the MADIN source attestation. The NCBI merge row is
side evidence only and does not require a generated `replaces` field.

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
The record is strain-rank while its parent is the `Rhodococcus jostii` species.
The GTDB mapping is closeMatch, not exactMatch.
The GTDB species identifier also maps to other nearby Rhodococcus records.
Only the `NCBITaxon:101510` GTDB row is target-exact here.
MADIN contributes a source attestation but no extra child records.
The old NCBI ID `NCBITaxon:269090` is merge-side evidence only.
No NCBI type-material row is available to mint side-only strain evidence.
Ten NCBI lineage rows are expected.
The 90-line YAML shape includes synonyms, GTDB, and MADIN but no strains.
The bounded scan found no exact BacDive evidence.
The exact `NCBITaxon:` probe avoided `1015100` and `1015101`.
The ignored report probe included gitignored files.
The legacy page path still points at the same checked-in slug.
