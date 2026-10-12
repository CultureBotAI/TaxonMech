# YAML Record Review: Archaeoglobus sulfaticallidus PM70-1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml
- Started UTC: 2026-09-27T11:12:15Z
- Finished UTC: 2026-09-27T11:12:15Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml` |
| Identifier | `NCBITaxon:387631` |
| Label | `Archaeoglobus sulfaticallidus PM70-1` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1316941` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon strain record with retained GOLD, GTDB, and
MADIN attestations, with path pinned by `data/taxa/PATHS.tsv:488855`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_sp_uba234.yaml data/taxa/archaea/archaeoglobus_sp_uba236.yaml data/taxa/archaea/archaeoglobus_sulfaticallidus.yaml data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 86 YAML lines, 10 lineage entries, 4 source attestations across NCBITAXON, GOLD, GTDB, and MADIN, 1 GTDB taxonomy mapping, 2 exact synonyms, 1 xref, 0 strain rows, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:387631` in the expected NCBI, GTDB, `data/taxa/PATHS.tsv`, seed, species-level related-record YAML, and generated target YAML rows; found `NCBITaxon:1316941` only as the expected parent and lineage species. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:81841`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 1 GTDB mapping row, 1 retained GOLD aggregate row, 1 native GOLD organism row, 1 native GOLD project row, 1 native GOLD analysis row, 1 MADIN row, 0 exact BacDive rows, no LPSN, MediaDive, BactoTraits, StrainInfo, or NCBI type-material rows, 2 raw assembly rows, 3 raw genome rows, and 5 raw related-record rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:387631` resolves to label `Archaeoglobus sulfaticallidus PM70-1`,
rank `STRAIN`, parent `NCBITaxon:1316941`, genetic code `11`, source set
`ncbitaxon|gtdb|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.
The generated record carries those fields.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:1316941` Archaeoglobus sulfaticallidus. The bounded scan found no
NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the strain identity, parent species, exact synonym
`Archaeoglobus sp. PM70-1`, genetic code, four-source attestation set, and the
2026-09-13 snapshot date; the seed event is supported by
`curation/seed_scope.tsv:24313`.

The GTDB row at `data/raw/gtdb_mappings.tsv:285381` supports the closeMatch
mapping to `GTDB:s__Archaeoglobus_A_sulfaticallidus`, the generated GTDB exact
synonym, the GTDB xref, and its one-genome assertion count.

The retained GOLD aggregate at `data/raw/gold_organism_counts.tsv:34035`
supports the GOLD source attestation. Native GOLD rows tie Go0030878, Gp0030878,
and one analysis row to this NCBI strain; normalized tables retain 2 assembly
rows, 3 genome rows, and 5 GOLD related records under the same exact taxon.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, GTDB, retained GOLD,
native GOLD, normalized GOLD, and MADIN inputs, and found no omitted exact
BacDive, LPSN, MediaDive, BactoTraits, StrainInfo, or type-material row.

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
`strain_count: 0` is expected on a generated strain-level taxon.
The GTDB closeMatch mints the GTDB exact synonym and xref.
Native GOLD rows are summarized in source attestations but not expanded as strain rows here.
No exact BacDive row is filed on the PM70-1 NCBI taxon.
No NCBI type-material row is available on this target.
The ignored report probe included gitignored files.
