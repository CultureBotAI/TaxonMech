# YAML Record Review: Afararchaeum irisae (SeqCode)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/afararchaeum_irisae_seqcode.yaml
- Started UTC: 2026-09-27T09:32:04Z
- Finished UTC: 2026-09-27T09:32:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/afararchaeum_irisae_seqcode.yaml` |
| Identifier | `NCBITaxon:3138747` |
| Label | `Afararchaeum irisae (SeqCode)` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:3138743` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated SeqCode archaeal species record with a close GTDB
mapping and path pinned by `data/taxa/PATHS.tsv:428311`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/afararchaeum_irisae_seqcode.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/aeropyrum_sp.yaml data/taxa/archaea/aeropyrum_sp_af1t6_18.yaml data/taxa/archaea/afararchaeum_irisae_seqcode.yaml data/taxa/archaea/aigarchaeota_archaeon.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 82 YAML lines, 10 lineage entries, 1 GTDB `skos:closeMatch` mapping, 3 exact synonyms, 1 related synonym, 1 xref, 2 source attestations, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:3138747` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:605886`, 10 checked lineage entries with no missing rows or mismatches, 1 GTDB closeMatch row at `data/raw/gtdb_mappings.tsv:263564`, 2 NCBI type-material rows, 0 NCBI merge rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, and no BacDive, LPSN, MediaDive, MADIN, BactoTraits, normalized strain, or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:3138747` resolves to label `Afararchaeum irisae (SeqCode)`, rank
`SPECIES`, parent `NCBITaxon:3138743`, genetic code `11`, source set
`ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`. The generated record
carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:3138743` Afararchaeum
(SeqCode). The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports exact synonyms `Afararchaeum irisae` and `Candidatus
Afararchaeum irisae`, plus related synonym `"Afararchaeum irisae" Baker et al.
2024`. GTDB contributes `GTDB:s__Afararchaeum_irisae`, one mapped genome, an
exact synonym `Afararchaeum irisae`, and the exact provider xref.

The NCBI type-material table carries two reference-material rows for isolate
`DAL-WCL_na_97C3R`, including its `personal::` alias. These rows are side
evidence only because no BacDive or final normalized strain row is filed under
this taxon. The seed event is supported by `curation/seed_scope.tsv:121888`.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, seed, path, type-material,
and generated YAML inputs, and found no omitted NCBI merge, LPSN, GOLD,
BacDive, MediaDive, MADIN, BactoTraits, native GOLD, normalized strain, or
direct StrainInfo evidence for this taxon.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

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
The GTDB close match is expected to mint both a mapping and xref.
No LPSN nomenclature section is expected for this SeqCode record.
No native GOLD rows were present for this target.
No retained GOLD aggregate row is filed on this target.
No NCBI merge row complicates identity.
The NCBI reference-material rows do not mint local strains by themselves.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
