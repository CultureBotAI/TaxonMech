# YAML Record Review: uncultured Starkeya sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_starkeya_sp.yaml
- Started UTC: 2026-09-27T17:08:17Z
- Finished UTC: 2026-09-27T17:08:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/uncultured_starkeya_sp.yaml` |
| Identifier | `NCBITaxon:1009877` |
| Label | `uncultured Starkeya sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1009876` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated uncultured Starkeya species record with NCBI and GTDB
support, with path pinned by `data/taxa/PATHS.tsv:3217`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/uncultured_starkeya_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/buchnera_aphidicola_str_f009_myzus_persicae.yaml data/taxa/bacteria/uncultured_filimonas_sp.yaml data/taxa/bacteria/uncultured_algorimarina_sp.yaml data/taxa/bacteria/uncultured_starkeya_sp.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 73 YAML lines, 10 lineage entries, 2 source attestations, 1 synonym, 0 nomenclature entries, 1 taxonomy mapping, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009877` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, generated target YAML, and 1 GTDB mapping row; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211823`, 1 GTDB row, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009877` resolves to `uncultured Starkeya sp.`, rank `SPECIES`,
parent `NCBITaxon:1009876`, genetic code `11`, source set `ncbitaxon|gtdb`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:1009876` environmental samples. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the uncultured Starkeya species identity and environmental
samples parent. The seed event is supported by `curation/seed_scope.tsv:65985`.

GTDB line 1139 supports the `s__Ancylobacter_sp964543245` closeMatch, xref, and
GTDB exact synonym. No native GOLD, MADIN, BacDive, LPSN, MediaDive, BactoTraits,
type-material, StrainInfo, or normalized strain row is filed.

## Completeness

No native GOLD organism, project, or analysis rows were found for this exact
NCBI taxon, and no GOLD aggregate or normalized genome/strain row was retained.
No BacDive, LPSN, MediaDive, MADIN, BactoTraits, type-material, or StrainInfo
row was filed under this exact taxon.

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
No NCBI synonym was present to materialize.
The GTDB closeMatch and xref are expected.
The GTDB exact synonym is expected.
No native GOLD organism, project, or analysis row was filed.
No retained GOLD aggregate row is filed on this target.
No normalized assembly row is filed on this target.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
No exact StrainInfo row is filed on this target.
Ten NCBI lineage rows are expected.
The 73-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
