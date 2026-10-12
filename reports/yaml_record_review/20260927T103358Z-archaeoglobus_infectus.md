# YAML Record Review: Archaeoglobus infectus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_infectus.yaml
- Started UTC: 2026-09-27T10:33:58Z
- Finished UTC: 2026-09-27T10:33:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_infectus.yaml` |
| Identifier | `NCBITaxon:403219` |
| Label | `Archaeoglobus infectus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2233` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated LPSN, BacDive, GOLD, and MADIN-backed archaeal species
record, with path pinned by `data/taxa/PATHS.tsv:493850`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_infectus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_fulgidus.yaml data/taxa/archaea/archaeoglobus_fulgidus_dsm_4304.yaml data/taxa/archaea/archaeoglobus_fulgidus_dsm_8774.yaml data/taxa/archaea/archaeoglobus_infectus.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 196 YAML lines, 9 lineage entries, 5 source attestations, 1 LPSN nomenclature entry, 1 related synonym, 1 xref, 1 BacDive strain, 0 assemblies, 0 genome records, and 6 related records. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:403219` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:86477`, 9 checked lineage entries with no mismatches, 1 LPSN row, 1 exact BacDive row, 1 GOLD aggregate row, 2 native GOLD organism rows, 1 MADIN row, 1 direct StrainInfo row, 2 StrainInfo related rows, and 6 NCBI type-material rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:403219` resolves to label `Archaeoglobus infectus`, rank `SPECIES`,
parent `NCBITaxon:2233`, source set `ncbitaxon|lpsn|gold|madin_etal`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, ending at genus `NCBITaxon:2233` Archaeoglobus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row at `data/raw/lpsn_names.tsv:23730` supports name id
`lpsn:786090`, authority Mori et al. 2008, correct-name status, three
publications, INSDC accession AB274307, and two type-strain designations.

BacDive row 18099 supports the single generated type strain, classified at
descendant `NCBITaxon:1121009`, with DSM 18877 and NBRC 100649 collection
identifiers. NCBI adds the related synonym `Archaeoglobus infectus Mori et al. 2008`.

The retained GOLD row at `data/raw/gold_organism_counts.tsv:34510` supports two
organisms; native GOLD adds two exact organism rows; MADIN row 23406 supports
four trait assertions; StrainInfo contributes DSM 18877 deposit evidence.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, retained GOLD, native
GOLD, MADIN, StrainInfo, path, and YAML inputs, and found no GTDB, MediaDive,
BactoTraits, assembly, genome, or merge rows.

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
`strain_count: 1` matches the BacDive-backed strain block.
No `taxonomy_mappings` section is expected.
The retained GOLD aggregate and native GOLD rows are both accounted for.
No native GOLD project or analysis rows were present.
No normalized assembly or genome rows are filed on this target.
No exact BactoTraits row is filed for this target.
No NCBI merge row complicates identity.
Nine NCBI lineage rows are expected.
The ignored report probe included gitignored files.
