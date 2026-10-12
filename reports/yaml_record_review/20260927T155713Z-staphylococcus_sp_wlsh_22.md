# YAML Record Review: Staphylococcus sp. WLSH-22

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/staphylococcus_sp_wlsh_22.yaml
- Started UTC: 2026-09-27T15:57:13Z
- Finished UTC: 2026-09-27T15:57:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/staphylococcus_sp_wlsh_22.yaml` |
| Identifier | `NCBITaxon:1009411` |
| Label | `Staphylococcus sp. WLSH-22` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:91994` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Bacillota unclassified-Staphylococcus
record, with path pinned by `data/taxa/PATHS.tsv:3152`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/staphylococcus_sp_wlsh_22.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_wlsh_22.yaml data/taxa/bacteria/flavobacterium_sp_scgc_aaa160_p02.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa164_a08.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa164_b23.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009411` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211756`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009411` resolves to `Staphylococcus sp. WLSH-22`, rank `SPECIES`,
parent `NCBITaxon:91994`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:91994` unclassified Staphylococcus under genus Staphylococcus. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank WLSH-22 identity, direct
unclassified-Staphylococcus parent, genetic code, single NCBITAXON source
attestation, and 2026-09-13 snapshot date. The seed event is supported by
`curation/seed_scope.tsv:312379`.

No LPSN, GTDB, GOLD aggregate, BacDive, MediaDive, MADIN, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly, normalized
genome, normalized related-record, or native GOLD row is filed under this exact
taxon in the committed source tables.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, and generated YAML
inputs, and found no omitted GTDB, LPSN, retained GOLD, native GOLD, BacDive,
MediaDive, MADIN, BactoTraits, type-material, or strain inventory row.

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
No native GOLD rows were present for this target.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 54-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
