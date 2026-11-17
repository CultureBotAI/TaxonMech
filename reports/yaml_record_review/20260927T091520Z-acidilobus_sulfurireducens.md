# YAML Record Review: Acidilobus sulfurireducens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidilobus_sulfurireducens.yaml
- Started UTC: 2026-09-27T09:15:20Z
- Finished UTC: 2026-09-27T09:15:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidilobus_sulfurireducens.yaml` |
| Identifier | `NCBITaxon:411357` |
| Label | `Acidilobus sulfurireducens` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:105850` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI species record with NCBI synonym, retained GOLD,
current native GOLD, and MADIN evidence, and path pinned by
`data/taxa/PATHS.tsv:496990`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidilobus_sulfurireducens.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidilobus_sp_scgc_ad_903_n04.yaml data/taxa/archaea/acidilobus_sp_scgc_ad_903_n18.yaml data/taxa/archaea/acidilobus_sp_scgc_ad_903_o15.yaml data/taxa/archaea/acidilobus_sulfurireducens.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 68 YAML lines, 9 lineage entries, 1 exact and 1 related NCBI synonym, 3 source attestations, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:411357` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:89500`, 9 checked lineage entries, 1 retained GOLD aggregate row with 1 organism, 1 MADIN row with 2 assertions, 1 native GOLD organism/project/analysis chain, 2 NCBI type-material rows, 0 NCBI merge rows, and no LPSN, GTDB, BacDive, MediaDive, BactoTraits, normalized strain, or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:411357` resolves to label `Acidilobus sulfurireducens`, rank
`SPECIES`, parent `NCBITaxon:105850`, genetic code `11`, source set
`ncbitaxon|gold|madin_etal`, and taxonomy snapshot `2026-09-13`. The generated
record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:105850` Acidilobus. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supplies exact synonym `Acidococcus sulfurreducens` and related
synonym `"Acidilobus sulfurireducens" Boyd et al. 2007`; both synonyms are
projected into YAML with their NCBI synonym types.

Retained GOLD supplies the one-organism source attestation, and current native
GOLD carries the matching `Go0006358` / `Gp0006358` organism-project-analysis
chain as side evidence. MADIN contributes 2 trait assertions.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GOLD, MADIN, native GOLD, seed,
path, and YAML inputs, and found no omitted NCBI merge, LPSN, GTDB, BacDive,
MediaDive, BactoTraits, normalized strain, or StrainInfo evidence.

The 2 exact NCBI type-material rows for 18D70 are side evidence only and do not
create local generated strains without a retained BacDive or normalized strain
row. No native GOLD genome record is emitted without a local strain inventory.

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
The retained GOLD aggregate intentionally supplies the generated GOLD count.
The current native GOLD rows are side evidence only.
No GTDB species maps directly or broadly to this species.
No LPSN row maps directly to this species in the retained inventory.
No MediaDive row is present either.
No generated taxonomy mapping section is expected.
No generated xref section is expected.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
