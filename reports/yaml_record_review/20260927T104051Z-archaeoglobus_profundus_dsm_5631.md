# YAML Record Review: Archaeoglobus profundus DSM 5631

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_profundus_dsm_5631.yaml
- Started UTC: 2026-09-27T10:40:51Z
- Finished UTC: 2026-09-27T10:40:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_profundus_dsm_5631.yaml` |
| Identifier | `NCBITaxon:572546` |
| Label | `Archaeoglobus profundus DSM 5631` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:84156` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB, BacDive, GOLD, MediaDive, and MADIN-backed
strain record, with path pinned by `data/taxa/PATHS.tsv:543973`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_profundus_dsm_5631.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_profundus_dsm_5631.yaml data/taxa/archaea/archaeoglobus_sp.yaml data/taxa/archaea/archaeoglobus_sp_arc22.yaml data/taxa/archaea/archaeoglobus_sp_enrichment_culture.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 789 YAML lines, 10 lineage entries, 6 source attestations, 1 GTDB closeMatch, 3 exact synonyms, 1 xref, 1 BacDive strain, 12 assemblies, 10 genome records, and 36 related records. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:572546` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:135031`, 10 checked lineage entries with no mismatches, 1 GTDB row, 1 exact BacDive row, 1 GOLD aggregate row, 1 native GOLD organism row, 1 native GOLD project row, 1 native GOLD analysis row, 1 MediaDive row, and 1 MADIN row. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:572546` resolves to label `Archaeoglobus profundus DSM 5631`, rank
`STRAIN`, parent `NCBITaxon:84156`, source set
`ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, ending at species `NCBITaxon:84156` Archaeoglobus profundus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

GTDB row `data/raw/gtdb_mappings.tsv:297068` supports the closeMatch to
`GTDB:s__Archaeoglobus_B_profundus`, the GTDB xref, and the single-genome
mapping. NCBI supports two DSM 5631 exact synonyms.

BacDive row 18097 supports the single generated strain with AV18 designation
and DSM 5631, JCM 9629, and NBRC 100127 culture identifiers. The retained GOLD
row at `data/raw/gold_organism_counts.tsv:39181` supports one organism.

Native GOLD rows, MediaDive row 11679, MADIN row 27237, and normalized
BACDIVE, GOLD, GTDB, BV-BRC, NCBI Assembly, and StrainInfo rows account for the
generated assemblies, genome records, and 36 related records.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, BacDive, retained GOLD, native
GOLD, MediaDive, MADIN, path, and YAML inputs, and found no LPSN, BactoTraits,
type-material, merge, or target-taxid StrainInfo side row.

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
The GTDB closeMatch also mints an exact GTDB synonym and xref.
The retained GOLD aggregate and native GOLD rows are both accounted for.
No LPSN nomenclature entry is expected on this strain record.
No NCBI type-material row is filed on this strain taxon.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The ignored report probe included gitignored files.
