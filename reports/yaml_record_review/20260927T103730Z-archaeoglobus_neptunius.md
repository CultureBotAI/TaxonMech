# YAML Record Review: Archaeoglobus neptunius

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_neptunius.yaml
- Started UTC: 2026-09-27T10:37:30Z
- Finished UTC: 2026-09-27T10:37:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_neptunius.yaml` |
| Identifier | `NCBITaxon:2798580` |
| Label | `Archaeoglobus neptunius` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2233` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated LPSN, GTDB, BacDive, and GOLD-backed archaeal species
record, with path pinned by `data/taxa/PATHS.tsv:376601`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_neptunius.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_infectus_dsm_18877.yaml data/taxa/archaea/archaeoglobus_lithotrophicus.yaml data/taxa/archaea/archaeoglobus_neptunius.yaml data/taxa/archaea/archaeoglobus_profundus.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 267 YAML lines, 9 lineage entries, 5 source attestations, 1 LPSN nomenclature entry, 1 GTDB closeMatch, 2 related NCBI synonyms, 2 xrefs, 1 BacDive type strain, 2 assemblies, 3 genome records, and 7 related records. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:2798580` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:556609`, 9 checked lineage entries with no mismatches, 1 LPSN row, 1 GTDB row, 1 exact BacDive row, 1 GOLD aggregate row, 1 native GOLD organism row, 1 native GOLD project row, 1 native GOLD analysis row, 1 direct StrainInfo row, and 6 NCBI type-material rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:2798580` resolves to label `Archaeoglobus neptunius`, rank
`SPECIES`, parent `NCBITaxon:2233`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`,
and taxonomy snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, ending at genus `NCBITaxon:2233` Archaeoglobus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row at `data/raw/lpsn_names.tsv:4075` supports name id `lpsn:20981`,
authority Slobodkina et al. 2021, correct-name status, three publications,
INSDC accession MW531883, and type-strain designation DSM 110954.

GTDB row `data/raw/gtdb_mappings.tsv:218308` supports the closeMatch to
`GTDB:s__Archaeoglobus_neptunius`; NCBI adds two related synonyms.
BacDive row 167621 supports type strain SE56 with DSM 110954 and VKM B-3474.

GOLD aggregate row 26746 supports one organism; native GOLD has the matching
organism, project, and analysis rows; and StrainInfo contributes the DSM
110954 deposit/strain related records.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, retained GOLD,
native GOLD, StrainInfo, path, and YAML inputs, and found no omitted MediaDive,
MADIN, BactoTraits, assembly, genome, or merge rows.

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
The GTDB mapping is a closeMatch to the species-level GTDB name.
The retained GOLD aggregate and native GOLD rows are both accounted for.
No exact MediaDive row is filed on this target.
No exact MADIN row is filed on this target.
Six NCBI type-material rows are present as side evidence.
No NCBI merge row complicates identity.
Nine NCBI lineage rows are expected.
The ignored report probe included gitignored files.
