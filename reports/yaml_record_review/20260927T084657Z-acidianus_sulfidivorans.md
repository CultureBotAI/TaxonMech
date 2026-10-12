# YAML Record Review: Acidianus sulfidivorans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_sulfidivorans.yaml
- Started UTC: 2026-09-27T08:46:57Z
- Finished UTC: 2026-09-27T08:46:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_sulfidivorans.yaml` |
| Identifier | `NCBITaxon:312539` |
| Label | `Acidianus sulfidivorans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:12914` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated species record with LPSN, BacDive, GOLD, MADIN, and
StrainInfo strain-side support, with path pinned by `data/taxa/PATHS.tsv:426226`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_sulfidivorans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_sp_syk_eso_2.yaml data/taxa/archaea/acidianus_sulfidivorans.yaml data/taxa/archaea/acidianus_sulfidivorans_jp7.yaml data/taxa/archaea/acidianus_tengchongensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 325 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 NCBI related synonym, 2 xrefs, 1 BacDive strain, 3 genome assemblies, 4 genome records, 11 related records, 5 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:312539` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no direct exact GTDB mapping; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:63923`, 9 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 1 BacDive exact row, 1 GOLD aggregate row, 1 MADIN row with 3 assertions, 1 native GOLD organism, 6 NCBI type-material rows, 1 direct StrainInfo hit with 2 deposits, 4 StrainInfo related rows, 0 NCBI merge rows, and no StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:312539` resolves to label `Acidianus sulfidivorans`, rank
`SPECIES`, parent `NCBITaxon:12914`, genetic code `11`, source set
`ncbitaxon|lpsn|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.
The generated record carries those same NCBI-owned fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:12914` Acidianus. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row `lpsn:785735` supports legitimate, validly published, correct-name
nomenclature; Plumb et al. 2007 authority text; DSM 18786 and JCM 13667 type
strain designations; DOI and PMID publication identifiers; and `AY907891`.

BacDive exact row `bacdive:16644` connects JP7 at both strain
`NCBITaxon:619593` and species `NCBITaxon:312539`; the generated strain is
`classified_as: NCBITaxon:619593`, is type material, and carries 3 assembly, 4
genome, and 11 related rows from BacDive, BV-BRC, GOLD, and StrainInfo.

The GOLD aggregate contributes 7 organism assertions and MADIN contributes 3
trait assertions for the species. Native GOLD also has direct organism
`Go0608847`; its two normalized related rows are emitted under the JP7 strain.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, GOLD, MADIN,
StrainInfo, type-material, native GOLD, seed, path, and YAML inputs, and found
no omitted NCBI merge, direct GTDB mapping, MediaDive, BactoTraits, StrainInfo
assembly, or StrainInfo exclusion row.

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
The LPSN row carries `GTDB:s__Acidianus_sulfidivorans` as an xref, while the
direct GTDB mapping is filed to JP7.
`strain_count: 1` matches the single BacDive-derived JP7 strain.
The emitted StrainInfo deposit rows are exactly DSM 18786 and JCM 13667.
The generated GOLD attestation covers direct species organisms only.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
