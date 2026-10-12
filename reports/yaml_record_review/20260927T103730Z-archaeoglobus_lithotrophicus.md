# YAML Record Review: Archaeoglobus lithotrophicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_lithotrophicus.yaml
- Started UTC: 2026-09-27T10:37:30Z
- Finished UTC: 2026-09-27T10:37:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_lithotrophicus.yaml` |
| Identifier | `NCBITaxon:138903` |
| Label | `Archaeoglobus lithotrophicus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2233` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon and MADIN-backed archaeal species record,
with path pinned by `data/taxa/PATHS.tsv:141422`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_lithotrophicus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_infectus_dsm_18877.yaml data/taxa/archaea/archaeoglobus_lithotrophicus.yaml data/taxa/archaea/archaeoglobus_neptunius.yaml data/taxa/archaea/archaeoglobus_profundus.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 63 YAML lines, 9 lineage entries, 2 source attestations, 2 related NCBI synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:138903` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:28042`, 9 checked lineage entries with no mismatches, 1 MADIN row, 2 NCBI type-material rows, 0 retained GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, and no LPSN, GTDB, MediaDive, or BactoTraits rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:138903` resolves to label `Archaeoglobus lithotrophicus`, rank
`SPECIES`, parent `NCBITaxon:2233`, source set `ncbitaxon|madin_etal`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, ending at genus `NCBITaxon:2233` Archaeoglobus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The raw NCBI row supports the species identity, direct Archaeoglobus parent,
genetic code, related synonym `"Archaeoglobus lithotrophicus" Stetter et al.
1993`, related synonym `Archaeoglobus lithotrophicus TF2`, and snapshot date.

The MADIN row at `data/raw/madin_taxa.tsv:13827` supports the MADIN source
attestation with two trait assertions. NCBI type-material rows list TF2
designations, but no BacDive strain or normalized strain row is filed here.

No LPSN, GTDB, GOLD aggregate, native GOLD, BacDive, MediaDive, BactoTraits,
StrainInfo, culture-collection, normalized assembly, normalized genome, or
normalized related-record row is filed under this exact taxon.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, MADIN, type-material, seed, path,
and YAML inputs, and found no omitted LPSN, GTDB, retained GOLD, native GOLD,
BacDive, MediaDive, BactoTraits, or strain inventory row.

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
No `taxonomy_mappings` section is expected.
No xref section is expected.
No retained GOLD aggregate row is filed on this target.
No native GOLD rows were present for this target.
Two NCBI type-material rows are present as side evidence.
No NCBI merge row complicates identity.
Nine NCBI lineage rows are expected.
The ignored report probe included gitignored files.
