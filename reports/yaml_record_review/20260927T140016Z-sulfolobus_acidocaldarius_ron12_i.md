# YAML Record Review: Sulfolobus acidocaldarius Ron12/I

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/sulfolobus_acidocaldarius_ron12_i.yaml
- Started UTC: 2026-09-27T14:00:16Z
- Finished UTC: 2026-09-27T14:00:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/sulfolobus_acidocaldarius_ron12_i.yaml` |
| Identifier | `NCBITaxon:1028567` |
| Label | `Sulfolobus acidocaldarius Ron12/I` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2285` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon+GTDB+MADIN strain record, with path pinned
by `data/taxa/PATHS.tsv:11333`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/sulfolobus_acidocaldarius_ron12_i.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/nitrosopumilus_sp_sj.yaml data/taxa/archaea/sulfolobus_acidocaldarius_n8.yaml data/taxa/archaea/sulfolobus_acidocaldarius_ron12_i.yaml data/taxa/archaea/marine_group_ii_euryarchaeote_scgc_aaa288_c18.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 84 YAML lines, 10 lineage entries, 3 source attestations, 1 GTDB closeMatch mapping, 3 exact synonyms, 1 xref, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1028567` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:219170`, 10 checked lineage entries with no missing rows or mismatches, the 57-genome GTDB closeMatch row at `data/raw/gtdb_mappings.tsv:1230`, 1 MADIN row with 1 assertion, 1 native GOLD organism, 1 native GOLD project, 1 native GOLD analysis, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no BacDive rows, no LPSN, MediaDive, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1028567` resolves to `Sulfolobus acidocaldarius Ron12/I`, rank `STRAIN`,
parent `NCBITaxon:2285`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:2285` Sulfolobus acidocaldarius. The bounded scan found no NCBI
merge row and no retained old-id row.

## Evidence

The NCBI row supports the strain identity, parent species, genetic code, two
NCBI exact synonyms, source set, and 2026-09-13 snapshot date. The seed event
is supported by `curation/seed_scope.tsv:36101`.

The GTDB row maps `GTDB:s__Sulfolobus_acidocaldarius` to the NCBI target with
`skos:closeMatch` and 57 genomes, and it supports the GTDB xref and exact
synonym. The MADIN row at `data/raw/madin_taxa.tsv:523` supports 1 assertion.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, MADIN, seed, path, and
generated YAML inputs, and found no omitted LPSN, retained GOLD, BacDive,
MediaDive, BactoTraits, type-material, or strain inventory row.

The native GOLD organism, project, and analysis rows are side evidence only;
there is no retained aggregate GOLD row or BacDive-derived local strain row.

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
No `nomenclature` section is expected on this strain record.
`GTDB:s__Sulfolobus_acidocaldarius` has `skos:closeMatch` with 57 genomes.
Native GOLD did not become generated GOLD strain evidence.
No retained GOLD aggregate row is filed on this target.
No direct BacDive row is filed on this target.
No same-taxon direct StrainInfo row is filed for this target.
MADIN is the only non-GTDB, non-NCBI retained source row.
No NCBI type-material row is filed on this strain target.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 84-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
