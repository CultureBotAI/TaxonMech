# YAML Record Review: Microcystis aeruginosa V-08

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/microcystis_aeruginosa_v_08.yaml
- Started UTC: 2026-09-27T16:34:10Z
- Finished UTC: 2026-09-27T16:34:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/microcystis_aeruginosa_v_08.yaml` |
| Identifier | `NCBITaxon:1009697` |
| Label | `Microcystis aeruginosa V-08` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1126` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Microcystis strain record,
with path pinned by `data/taxa/PATHS.tsv:3191`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/microcystis_aeruginosa_v_08.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/microcystis_aeruginosa_g_01.yaml data/taxa/bacteria/microcystis_aeruginosa_v_08.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_trissolcus_festivae.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_trissolcus_flavipes.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 60 YAML lines, 12 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009697` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211794`, 12 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009697` resolves to `Microcystis aeruginosa V-08`,
rank `STRAIN`, parent `NCBITaxon:1126`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 12 committed NCBI rows, ending at
`NCBITaxon:1126` Microcystis aeruginosa. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the V-08 strain identity, direct Microcystis aeruginosa
parent, genetic code, single NCBITAXON source attestation, and 2026-09-13
snapshot date. The seed event is supported by
`curation/seed_scope.tsv:312411`.

No LPSN, GTDB, GOLD aggregate, native GOLD organism/project/analysis, BacDive,
MediaDive, MADIN, BactoTraits, NCBI type-material, StrainInfo,
culture-collection, normalized assembly, normalized genome, or normalized
related-record row is filed.

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
No `taxonomy_mappings` section is expected.
No xref section is expected.
No native GOLD organism, project, or analysis row was filed.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Twelve NCBI lineage rows are expected.
The 60-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
