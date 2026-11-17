# YAML Record Review: Mycobacterium avium subsp. paratuberculosis S397

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_s397.yaml
- Started UTC: 2026-09-28T05:03:10Z
- Finished UTC: 2026-09-28T05:03:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_s397.yaml` |
| Identifier | `NCBITaxon:1010838` |
| Label | `Mycobacterium avium subsp. paratuberculosis S397` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1770` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon/GTDB/GOLD/MADIN M. avium strain record,
with path pinned by `data/taxa/PATHS.tsv:3925`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_s397.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/mycobacterium_tuberculosis_bt2.yaml data/taxa/bacteria/mycobacterium_tuberculosis_bt1.yaml data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_s397.yaml data/taxa/bacteria/bacillus_sp_nrs_866.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 95 YAML lines, 12 lineage entries, 4 source attestations, 1 GTDB taxonomy mapping, 3 exact synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010838` in the expected seed, NCBI, GTDB mapping, `GOLD`/`MADIN`-attested YAML, and `data/taxa/PATHS.tsv` rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212478`, 1 GTDB mapping, 1 MADIN row, 1 GOLD aggregate row, 1 native GOLD organism row, 1 native GOLD project row, 1 native GOLD analysis row, 12 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, and no StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010838` resolves to `Mycobacterium avium subsp. paratuberculosis S397`, rank `STRAIN`,
parent `NCBITaxon:1770`, genetic code `11`, source set `ncbitaxon|gtdb|gold|madin_etal`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 12 committed NCBI rows, ending at
`NCBITaxon:1770` Mycobacterium avium subsp. paratuberculosis. The bounded scan found no NCBI
merge row and no retained old-id row.

## Evidence

NCBI supports the strain identity, M. avium subsp. paratuberculosis parent, two exact synonyms,
genetic code, NCBITAXON source attestation, and 2026-09-13 snapshot date.

GTDB supports `skos:closeMatch` to `GTDB:s__Mycobacterium_avium` and 324
genome assertions; GOLD supports one aggregate and one native organism,
project, and analysis row.

MADIN supports the four-assertion MADIN source attestation.

## Completeness

No BacDive, LPSN, MediaDive, BactoTraits, NCBI type-material, StrainInfo,
culture-collection, normalized assembly, normalized genome, or exact-target
related-record row is filed.

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
The GTDB closeMatch predicate is the committed kg-microbe mapping.
NCBI contributes two exact strain synonyms.
The GOLD aggregate is retained for the exact NCBI taxon.
Native GOLD organism `Go0010150` points at project `Gp0010150`.
Native GOLD analysis evidence is present for the same project.
The MADIN assertion row is represented directly.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Twelve NCBI lineage rows are expected.
The 95-line YAML shape includes all retained source sections.
Regeneration should preserve identifier, lineage, and attestations.
The ignored report probe included gitignored files.
