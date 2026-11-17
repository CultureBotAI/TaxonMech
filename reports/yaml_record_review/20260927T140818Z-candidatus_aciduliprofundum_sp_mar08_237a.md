# YAML Record Review: Candidatus Aciduliprofundum sp. MAR08-237A

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/candidatus_aciduliprofundum_sp_mar08_237a.yaml
- Started UTC: 2026-09-27T14:08:18Z
- Finished UTC: 2026-09-27T14:08:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/candidatus_aciduliprofundum_sp_mar08_237a.yaml` |
| Identifier | `NCBITaxon:1033304` |
| Label | `Candidatus Aciduliprofundum sp. MAR08-237A` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2633939` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon+GOLD Thermoplasmatota placeholder, with path
pinned by `data/taxa/PATHS.tsv:13395`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/candidatus_aciduliprofundum_sp_mar08_237a.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/candidatus_aciduliprofundum_sp_mar08_641.yaml data/taxa/archaea/candidatus_aciduliprofundum_sp_epr07_159.yaml data/taxa/archaea/candidatus_aciduliprofundum_sp_mar08_237a.yaml data/taxa/archaea/candidatus_aciduliprofundum_sp_lau09_654.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 53 YAML lines, 8 lineage entries, 2 source attestations, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1033304` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:220950`, 8 checked lineage entries with no missing rows or mismatches, 1 GOLD aggregate row at line 441, 1 native GOLD organism at line 526237, 1 native GOLD project at line 610524, 1 native GOLD analysis at line 451989, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1033304` resolves to `Candidatus Aciduliprofundum sp. MAR08-237A`,
rank `SPECIES`, parent `NCBITaxon:2633939`, genetic code `11`, source set
`ncbitaxon|gold`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 8 committed NCBI rows, ending at
`NCBITaxon:2633939` unclassified Candidatus Aciduliprofundum. The bounded scan
found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank placeholder identity, direct
unclassified-Candidatus-Aciduliprofundum parent, genetic code, empty synonym
columns, NCBI source attestation, GOLD source flag, and snapshot date. The
seed event is supported by `curation/seed_scope.tsv:57243`.

The retained GOLD aggregate row supports a one-organism GOLD source
attestation. Native GOLD organism `Go0705926`, project `Gp0832670`, and one
linked analysis confirm compatible exact native side evidence for this target.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GOLD, seed, path, and generated
YAML inputs, and found no omitted GTDB, LPSN, BacDive, MediaDive, MADIN,
BactoTraits, type-material, or strain inventory row.

The native GOLD organism, project, and analysis rows are side evidence only;
there is no BacDive-derived local strain row to materialize them as a strain.

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
No GTDB mapping row is filed under this exact target.
The retained GOLD aggregate supplies the second source attestation.
Native GOLD did not become generated GOLD strain evidence.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Eight NCBI lineage rows are expected.
The 53-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
