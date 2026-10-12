# YAML Record Review: Aeropyrum pernix K1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/aeropyrum_pernix_k1.yaml
- Started UTC: 2026-09-27T09:27:45Z
- Finished UTC: 2026-09-27T09:27:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/aeropyrum_pernix_k1.yaml` |
| Identifier | `NCBITaxon:272557` |
| Label | `Aeropyrum pernix K1` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:56636` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI strain record with GTDB and MADIN support and path
pinned by `data/taxa/PATHS.tsv:367693`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/aeropyrum_pernix_k1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/aeropyrum_camini.yaml data/taxa/archaea/aeropyrum_camini_sy1_jcm_12091.yaml data/taxa/archaea/aeropyrum_pernix.yaml data/taxa/archaea/aeropyrum_pernix_k1.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 84 YAML lines, 10 lineage entries, 0 LPSN nomenclature entries, 1 GTDB mapping, 3 exact synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, 3 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:272557` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:56196`, 10 checked lineage rows with no mismatches, 1 GTDB mapping row, 1 MADIN row with 7 assertions, 1 native GOLD organism, 4 native GOLD projects, 1 native GOLD analysis, 2 raw strain assemblies, 4 genome records, 16 raw related rows, 0 NCBI merge rows, and no LPSN, BacDive, MediaDive, retained GOLD, exact StrainInfo, or type-material rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:272557` resolves to label `Aeropyrum pernix K1`, rank `STRAIN`,
parent `NCBITaxon:56636`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`. The generated
record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through species `NCBITaxon:56636` Aeropyrum
pernix. The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

GTDB mapping row 210667 maps `GTDB:s__Aeropyrum_pernix` to this NCBI record
with `skos:closeMatch` and 2 genomes. The generated record preserves that
mapping, adds the GTDB label as an exact synonym, and exposes a single GTDB xref.

NCBI supplies two exact K1 strain synonyms and MADIN contributes 7 trait
assertions. The native GOLD organism/project/analysis chain is side evidence
because no retained BacDive strain row is keyed directly to `NCBITaxon:272557`.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, MADIN, native GOLD, seed, path,
and YAML inputs, and found no omitted NCBI merge, LPSN, BacDive, MediaDive,
retained GOLD, exact StrainInfo, type-material, or final strain row.

The raw K1 strain-genome rows are available for BacDive strain 4195, but that
local strain is filed at species `NCBITaxon:56636`; this child record correctly
has `strain_count: 0` and no generated genome links of its own.

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
The retained GTDB closeMatch is the committed kg-microbe mapping.
No generated LPSN xref is expected.
No generated BacDive attestation is expected.
The parent species record owns the K1 BacDive strain block.
No exact MediaDive row maps directly to the K1 child taxon.
No retained GOLD aggregate row maps directly to the K1 child taxon.
No exact StrainInfo taxon row is keyed to `NCBITaxon:272557`.
No NCBI type-material row maps directly to the K1 child taxon.
The exact native GOLD K1 chain remains side evidence only.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
