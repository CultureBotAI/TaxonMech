# YAML Record Review: Aigarchaeota archaeon

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/aigarchaeota_archaeon.yaml
- Started UTC: 2026-09-27T09:32:04Z
- Finished UTC: 2026-09-27T09:32:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/aigarchaeota_archaeon.yaml` |
| Identifier | `NCBITaxon:2528703` |
| Label | `Aigarchaeota archaeon` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1104572` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI archaeal placeholder species record with pooled
GTDB broad mappings, retained GOLD evidence, and path pinned by
`data/taxa/PATHS.tsv:348670`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/aigarchaeota_archaeon.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/aeropyrum_sp.yaml data/taxa/archaea/aeropyrum_sp_af1t6_18.yaml data/taxa/archaea/afararchaeum_irisae_seqcode.yaml data/taxa/archaea/aigarchaeota_archaeon.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 90 YAML lines, 6 lineage entries, 5 GTDB `skos:broadMatch` mappings, 3 source attestations, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:2528703` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:529457`, 6 checked lineage entries with no missing rows or mismatches, 5 GTDB broadMatch rows at `data/raw/gtdb_mappings.tsv:197396-197400`, 1 retained GOLD aggregate row with 4 organisms, 4 exact native GOLD organisms, 4 native GOLD projects, 8 native GOLD analyses, 0 NCBI merge rows, 0 NCBI type-material rows, and no BacDive, LPSN, MediaDive, MADIN, BactoTraits, normalized strain, or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:2528703` resolves to label `Aigarchaeota archaeon`, rank `SPECIES`,
parent `NCBITaxon:1104572`, genetic code `11`, source set
`ncbitaxon|gtdb|gold`, and taxonomy snapshot `2026-09-13`. The generated
record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 6 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1104572` unclassified
Nitrososphaerota. The bounded scan found no NCBI merge row and no retained
old-id row.

## Evidence

GTDB supplies five `skos:broadMatch` rows: 3 genomes each for
`GTDB:s__Geocrenenecus_sp025058515` and
`GTDB:s__Wolframiiraptor_sp025059415`, and 2 genomes each for
`GTDB:s__Benthortus_lauensis`, `GTDB:s__JANXDH01_sp025059745`, and
`GTDB:s__Terraquivivens_sp025059205`. None is exact, so no xref is generated.

The retained GOLD aggregate row at `data/raw/gold_organisms.tsv:23035`
supplies the 4-organism GOLD source attestation. The current native GOLD
organism/project/analysis rows match strains JGI MDM2 JNZ-1-G18, JGI MDM2
JNZ-1-H10, JGI MDM2 JNZ-1-K18, and JGI MDM2 JNZ-1-N15 as side evidence only.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, GOLD, seed, path, native GOLD,
and generated YAML inputs, and found no omitted NCBI merge, NCBI type-material,
LPSN, BacDive, MediaDive, MADIN, BactoTraits, normalized strain, or direct
StrainInfo evidence for this taxon.

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
All five GTDB mappings stay broad and do not mint xrefs.
The source attestation records only the first GTDB species and summarizes four more.
The retained GOLD aggregate count matches the four native GOLD organism rows.
Native GOLD rows do not create generated child strains by themselves.
The ignored report probe included gitignored files.
