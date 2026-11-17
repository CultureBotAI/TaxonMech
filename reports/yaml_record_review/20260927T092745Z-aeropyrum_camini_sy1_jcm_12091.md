# YAML Record Review: Aeropyrum camini SY1 = JCM 12091

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/aeropyrum_camini_sy1_jcm_12091.yaml
- Started UTC: 2026-09-27T09:27:45Z
- Finished UTC: 2026-09-27T09:27:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/aeropyrum_camini_sy1_jcm_12091.yaml` |
| Identifier | `NCBITaxon:1198449` |
| Label | `Aeropyrum camini SY1 = JCM 12091` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:229980` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI strain record with GTDB, BacDive, MediaDive, MADIN,
GOLD, and genome-overlay evidence, with path pinned by
`data/taxa/PATHS.tsv:65736`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/aeropyrum_camini_sy1_jcm_12091.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/aeropyrum_camini.yaml data/taxa/archaea/aeropyrum_camini_sy1_jcm_12091.yaml data/taxa/archaea/aeropyrum_pernix.yaml data/taxa/archaea/aeropyrum_pernix_k1.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 705 YAML lines, 10 lineage entries, 0 LPSN nomenclature entries, 1 GTDB mapping, 4 exact synonyms, 1 xref, 1 BacDive strain, 12 genome assemblies, 9 genome records, 29 related records, 5 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1198449` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:269919`, 10 checked lineage rows with no mismatches, 1 GTDB mapping row, 1 exact BacDive row, 1 MediaDive row with 2 media, 1 MADIN row with 7 assertions, 1 native GOLD organism, 2 native GOLD projects and analyses, 10 raw strain assemblies, 9 genome rows, 18 raw related rows, and no LPSN, retained GOLD, exact StrainInfo, type-material, or NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1198449` resolves to label `Aeropyrum camini SY1 = JCM 12091`, rank
`STRAIN`, parent `NCBITaxon:229980`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|mediadive|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through species `NCBITaxon:229980` Aeropyrum
camini. The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

NCBI supplies exact synonyms for JCM 12091 and SY1 spellings. No LPSN
nomenclature row maps directly to the NCBI strain taxon, so no LPSN xref is
expected here.

BacDive exact row `bacdive:4196` supplies SY1 with ATCC BAA-758, DSM 16960, and
JCM 12091 deposits. The strain block carries BacDive, BV-BRC, GOLD, GTDB, NCBI
Assembly, and StrainInfo overlay links that produce 12 assembly, 9 genome, and
29 related rows in the generated record.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, BacDive, MediaDive, MADIN,
native GOLD, seed, path, and YAML inputs, and found no omitted NCBI merge, LPSN,
retained GOLD, exact StrainInfo, type-material, or BactoTraits row.

The exact GOLD organism `Go0048799`, projects `Gp0048799` and `Gp0093097`, and
analyses `Ga0021833` and `Ga0128336` support the generated GOLD strain-genome
and related-record links through the JCM 12091 culture identifier.

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
`strain_count: 1` matches the single exact BacDive SY1 strain.
The retained GTDB closeMatch is the committed kg-microbe mapping.
The `MEDIADIVE` row contributes 2 media to this strain taxon.
The parent `Aeropyrum camini` record also gathers this BacDive strain.
No retained GOLD aggregate row maps directly to the child strain taxon.
No exact StrainInfo taxon row is keyed to `NCBITaxon:1198449`.
No NCBI type-material row maps directly to the child strain taxon.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
