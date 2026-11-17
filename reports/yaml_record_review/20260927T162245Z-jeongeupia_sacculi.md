# YAML Record Review: Jeongeupia sacculi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/jeongeupia_sacculi.yaml
- Started UTC: 2026-09-27T16:22:45Z
- Finished UTC: 2026-09-27T16:22:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/jeongeupia_sacculi.yaml` |
| Identifier | `NCBITaxon:1009682` |
| Label | `Jeongeupia sacculi` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:885864` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB- and GOLD-backed Jeongeupia species record, with
path pinned by `data/taxa/PATHS.tsv:3177`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/jeongeupia_sacculi.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/jeongeupia_sacculi.yaml data/taxa/bacteria/nocardiopsis_sp_25l_1_1c.yaml data/taxa/bacteria/bradyrhizobium_sp_ccbau_051161.yaml data/taxa/bacteria/bradyrhizobium_sp_ccbau_23332.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 81 YAML lines, 9 lineage entries, 1 GTDB closeMatch taxonomy mapping, 1 GTDB exact synonym, 2 NCBI related synonyms, 1 GTDB xref, 1 NCBITAXON, 1 GTDB, and 1 GOLD source attestation, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009682` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211780`, 1 GTDB mapping row at `data/raw/gtdb_mappings.tsv:1126`, 1 GOLD aggregate row, 1 native GOLD organism, project, and analysis row, 2 NCBI type-material rows, 9 checked lineage entries with no mismatches, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009682` resolves to `Jeongeupia sacculi`, rank `SPECIES`, parent
`NCBITaxon:885864`, genetic code `11`, source set `ncbitaxon|gtdb|gold`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
`NCBITaxon:885864` Jeongeupia. The bounded scan found no NCBI merge row and no
retained old-id row.

## Evidence

The NCBI row supports the species-rank identity, direct Jeongeupia parent, two
related synonyms for HS-3, and snapshot date. The seed event is supported by
`curation/seed_scope.tsv:36077`.

GTDB line 1126 supports the one-genome `skos:closeMatch`,
`GTDB:s__Jeongeupia_sp015140455`; the GOLD aggregate row supports the GOLD
source attestation.

## Completeness

Native GOLD rows for `Go0566467` / `Gp0536828` are side evidence only: no
normalized genome/strain row was retained. The NCBI type-material rows for
HS-3 are bare designations and do not mint a strain without a BacDive or
culture-collection row.

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
One GTDB closeMatch row is expected.
One GOLD aggregate row is expected.
The GOLD aggregate row explains the GOLD source attestation.
Native GOLD rows were side evidence only.
No BacDive row was available to mint a strain.
Two NCBI type-material rows are side evidence only.
No normalized genome rows are filed for HS-3.
No NCBI merge row complicates identity.
Nine NCBI lineage rows are expected.
The single GTDB mapping row is direct and exact-ID aligned.
The 81-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
