# YAML Record Review: uncultured Filimonas sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_filimonas_sp.yaml
- Started UTC: 2026-09-27T17:08:17Z
- Finished UTC: 2026-09-27T17:08:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/uncultured_filimonas_sp.yaml` |
| Identifier | `NCBITaxon:1009873` |
| Label | `uncultured Filimonas sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1009872` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only uncultured Filimonas record,
with path pinned by `data/taxa/PATHS.tsv:3215`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/uncultured_filimonas_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/buchnera_aphidicola_str_f009_myzus_persicae.yaml data/taxa/bacteria/uncultured_filimonas_sp.yaml data/taxa/bacteria/uncultured_algorimarina_sp.yaml data/taxa/bacteria/uncultured_starkeya_sp.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 60 YAML lines, 12 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009873` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211819`, 12 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009873` resolves to `uncultured Filimonas sp.`, rank `SPECIES`,
parent `NCBITaxon:1009872`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 12 committed NCBI rows, ending at
`NCBITaxon:1009872` environmental samples. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the uncultured Filimonas species identity, environmental
samples parent, genetic code, single NCBITAXON source attestation, and
2026-09-13 snapshot date. The seed event is supported by `curation/seed_scope.tsv:312423`.

No LPSN, GTDB, GOLD aggregate, native GOLD organism/project/analysis, BacDive,
MediaDive, MADIN, BactoTraits, NCBI type-material, StrainInfo,
culture-collection, normalized assembly, normalized genome, or normalized
related-record row is filed.

## Completeness

No native GOLD organism, project, or analysis rows were found for this exact
NCBI taxon, and no GOLD aggregate or normalized genome/strain row was retained.
No BacDive, LPSN, MediaDive, MADIN, BactoTraits, type-material, or StrainInfo
row was filed under this exact taxon.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

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
No NCBI synonym was present to materialize.
No `taxonomy_mappings` section is expected.
No xref section is expected.
No native GOLD organism, project, or analysis row was filed.
No retained GOLD aggregate row is filed on this target.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Twelve NCBI lineage rows are expected.
The 60-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
