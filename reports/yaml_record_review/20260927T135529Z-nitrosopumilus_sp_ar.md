# YAML Record Review: Nitrosopumilus sp. AR

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/nitrosopumilus_sp_ar.yaml
- Started UTC: 2026-09-27T13:55:29Z
- Finished UTC: 2026-09-27T13:55:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/nitrosopumilus_sp_ar.yaml` |
| Identifier | `NCBITaxon:1027373` |
| Label | `Nitrosopumilus sp. AR` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2619919` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon+MADIN Nitrosopumilus placeholder, with path
pinned by `data/taxa/PATHS.tsv:10964`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/nitrosopumilus_sp_ar.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/crenarchaeote_scgc_aaa160_j20.yaml data/taxa/archaea/methanomethylovorans_hollandica.yaml data/taxa/archaea/halobaculum_magnesiiphilum.yaml data/taxa/archaea/nitrosopumilus_sp_ar.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 59 YAML lines, 10 lineage entries, 2 source attestations, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1027373` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:218797`, 10 checked lineage entries with no missing rows or mismatches, 1 MADIN row with 1 assertion, 1 native GOLD organism, 1 native GOLD project, 1 native GOLD analysis, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no BacDive rows, no LPSN, GTDB, MediaDive, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1027373` resolves to label `Nitrosopumilus sp. AR`, rank `SPECIES`,
parent `NCBITaxon:2619919`, genetic code `11`, source set
`ncbitaxon|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:2619919` unclassified Nitrosopumilus. The bounded scan found no
NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank placeholder identity, direct
unclassified-Nitrosopumilus parent, genetic code, empty synonym columns,
single NCBITAXON source attestation, and 2026-09-13 snapshot date. The seed
event is supported by `curation/seed_scope.tsv:57220`.

The MADIN row at `data/raw/madin_taxa.tsv:512` supports the second source
attestation with 1 trait assertion. Exact source scans found native GOLD
organism `Go0011539`, project `Gp0011539`, and one linked native analysis.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, MADIN, seed, path, and generated
YAML inputs, and found no omitted GTDB, LPSN, retained GOLD, BacDive,
MediaDive, BactoTraits, type-material, or strain inventory row.

The native GOLD organism, project, and analysis rows are side evidence only;
there is no retained aggregate GOLD row or BacDive-derived local strain row.

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
No `synonyms` section is expected.
No `taxonomy_mappings` section is expected.
No xref section is expected.
Native GOLD did not become generated GOLD strain evidence.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The MADIN attestation is the only non-NCBI retained source row.
The 59-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
