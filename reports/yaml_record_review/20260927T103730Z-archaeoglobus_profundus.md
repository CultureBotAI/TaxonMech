# YAML Record Review: Archaeoglobus profundus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_profundus.yaml
- Started UTC: 2026-09-27T10:37:30Z
- Finished UTC: 2026-09-27T10:37:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_profundus.yaml` |
| Identifier | `NCBITaxon:84156` |
| Label | `Archaeoglobus profundus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2233` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated LPSN, BacDive, GOLD, and MADIN-backed archaeal species
record, with path pinned by `data/taxa/PATHS.tsv:593605`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_profundus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_infectus_dsm_18877.yaml data/taxa/archaea/archaeoglobus_lithotrophicus.yaml data/taxa/archaea/archaeoglobus_neptunius.yaml data/taxa/archaea/archaeoglobus_profundus.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 794 YAML lines, 9 lineage entries, 5 source attestations, 1 LPSN nomenclature entry, 0 taxonomy mappings, 1 related NCBI synonym, 1 xref, 1 BacDive type strain, 12 assemblies, 10 genome records, and 36 related records. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:84156` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:12930`, 9 checked lineage entries with no mismatches, 1 LPSN row, 1 exact BacDive row, 1 GOLD aggregate row, 2 native GOLD organism rows, 1 MADIN row, 1 direct StrainInfo row, 1 target StrainInfo assembly row, and 8 StrainInfo related rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:84156` resolves to label `Archaeoglobus profundus`, rank `SPECIES`,
parent `NCBITaxon:2233`, source set `ncbitaxon|lpsn|gold|madin_etal`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, ending at genus `NCBITaxon:2233` Archaeoglobus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row at `data/raw/lpsn_names.tsv:15382` supports name id
`lpsn:773361`, authority Burggraf et al. 1990, correct-name status, two DOI
publications, INSDC accession AJ299219, and three type-strain designations.

BacDive row 18097 supports type strain AV18, classified at descendant
`NCBITaxon:572546`, with DSM 5631, JCM 9629, and NBRC 100127 identifiers.
NCBI adds the related synonym `Archaeoglobus profundus Burggraf et al. 1990`.

The retained GOLD row at `data/raw/gold_organism_counts.tsv:43163` supports two
organisms; MADIN row 31138 supports six trait assertions; StrainInfo and
descendant assembly rows account for the normalized genome evidence.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, retained GOLD, native
GOLD, MADIN, StrainInfo, path, and YAML inputs, and found no GTDB, MediaDive,
BactoTraits, species-level assembly gap, or merge rows.

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
`strain_count: 1` matches the BacDive-backed type-strain block.
No `taxonomy_mappings` section is expected.
The retained GOLD aggregate and native GOLD rows are both accounted for.
No exact GTDB mapping row is filed on this target.
No exact MediaDive row is filed on this target.
Eight NCBI type-material rows are present as side evidence.
No NCBI merge row complicates identity.
Nine NCBI lineage rows are expected.
The ignored report probe included gitignored files.
