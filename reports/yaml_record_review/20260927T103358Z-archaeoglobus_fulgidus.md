# YAML Record Review: Archaeoglobus fulgidus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_fulgidus.yaml
- Started UTC: 2026-09-27T10:33:58Z
- Finished UTC: 2026-09-27T10:33:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_fulgidus.yaml` |
| Identifier | `NCBITaxon:2234` |
| Label | `Archaeoglobus fulgidus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2233` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated LPSN, GTDB, BacDive, GOLD, MediaDive, and MADIN-backed
archaeal species record, with path pinned by `data/taxa/PATHS.tsv:334362`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_fulgidus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_fulgidus.yaml data/taxa/archaea/archaeoglobus_fulgidus_dsm_4304.yaml data/taxa/archaea/archaeoglobus_fulgidus_dsm_8774.yaml data/taxa/archaea/archaeoglobus_infectus.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 1452 YAML lines, 9 lineage entries, 7 source attestations, 1 LPSN nomenclature entry, 1 GTDB closeMatch, 1 related synonym, 2 xrefs, 3 BacDive strains, 19 assemblies, 14 genome records, and 75 related records. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:2234` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:1758`, 9 checked lineage entries with no mismatches, 1 LPSN row, 1 GTDB row, 3 exact BacDive rows, 1 GOLD aggregate row, 3 native GOLD organism rows, 1 MediaDive row, 1 MADIN row, 3 direct StrainInfo rows, and 10 NCBI type-material rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:2234` resolves to label `Archaeoglobus fulgidus`, rank `SPECIES`,
parent `NCBITaxon:2233`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy
snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, ending at genus `NCBITaxon:2233` Archaeoglobus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row at `data/raw/lpsn_names.tsv:15381` supports name id
`lpsn:773360`, authority Stetter 1988, correct-name status, two DOI
publications, INSDC accession X05567, and four type-strain designations.

GTDB row `data/raw/gtdb_mappings.tsv:177020` supports the closeMatch to
`GTDB:s__Archaeoglobus_fulgidus`, the GTDB xref, and the six-genome mapping.
NCBI adds the related synonym `Archaeoglobus fulgidus Stetter 1988`.

BacDive exact rows support the three declared strains, including DSM 4304 and
DSM 8774 descendant records. GOLD aggregate row 21140 supports four organisms;
MediaDive row 6868 supports one medium; MADIN row 19569 supports six trait
assertions; StrainInfo contributes DSM 4139, DSM 4304, and DSM 8774 evidence.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for the expected NCBI, LPSN, GTDB, BacDive, retained
GOLD, native GOLD, MediaDive, MADIN, StrainInfo, path, and YAML inputs, and
found no BactoTraits row or unresolved merge evidence.

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
`strain_count: 3` matches the BacDive-backed strain block.
The GTDB mapping is a closeMatch to the species-level GTDB name.
The retained GOLD aggregate and native GOLD rows are both accounted for.
No exact BactoTraits row is filed for this target.
No NCBI merge row complicates identity.
Nine NCBI lineage rows are expected.
The ignored report probe included gitignored files.
