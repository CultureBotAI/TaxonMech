# YAML Record Review: Thalassovita litoralis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/thalassovita_litoralis.yaml
- Started UTC: 2026-09-28T02:23:11Z
- Finished UTC: 2026-09-28T02:23:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/thalassovita_litoralis.yaml` |
| Identifier | `NCBITaxon:1010611` |
| Label | `Thalassovita litoralis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:335927` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated multi-source Thalassovita species record,
with path pinned by `data/taxa/PATHS.tsv:3798`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/thalassovita_litoralis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_bd_89.yaml data/taxa/bacteria/bacillus_sp_bd_93.yaml data/taxa/bacteria/methylobacterium_gnaphalii.yaml data/taxa/bacteria/thalassovita_litoralis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 720 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 9 synonyms, 1 xref, 1 BacDive type strain, 3 culture IDs, 10 genome assemblies, 8 genome records, 26 related rows, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010611` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212369`, 9 checked lineage rows, 1 LPSN row, 1 BacDive row, 1 GOLD aggregate row, 4 native GOLD organisms, 1 GOLD project, 1 GOLD analysis, 1 MediaDive row, 1 MADIN row, 8 type-material rows, no BactoTraits row, and no NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010611` resolves to `Thalassovita litoralis`, rank `SPECIES`,
parent `NCBITaxon:335927`, genetic code `11`, source set with seven upstreams,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
`NCBITaxon:335927` genus `Thalassovita`; no NCBI merge row was retained.

## Evidence

The NCBI row supports the current species name, parent, genetic code, 2 exact
and 5 related synonyms, seven upstream source flags, and the snapshot date.

LPSN `lpsn:17241` supplies the validly published but illegitimate synonym
nomenclature row, four type-strain designations, three publications, and
sequence accession `INSDC:AB627076`.

BacDive `bacdive:130638` supplies the KU5D5 type strain with three culture IDs.
GOLD contributes 4 organism rows and rows for project `Gp0194233`.
GTDB contributes `GTDB:s__Thalassobius_litoralis` as a `skos:closeMatch`;
MediaDive, MADIN, BV-BRC, NCBI Assembly, and StrainInfo add retained rows.

## Completeness

No BactoTraits, native `data/raw/gtdb_species.tsv`, NCBI merge, retained
old-id, StrainInfo exclusion, definition, or causal-graph row was filed.
The normalized raw inventories account for the generated assembly, genome,
and related-record counts under this exact NCBI taxon.

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
`strain_count: 1` is expected from the exact BacDive row.
NCBI contributes 7 synonyms; GTDB and LPSN add one synonym each.
The LPSN name is deprecated and synonymized to `lpsn:791232`.
The GOLD source attestation preserves the aggregate organism count of 4.
Only the DSM 29506 GOLD project currently generates GOLD assembly rows.
MediaDive contributes two media and MADIN contributes one trait assertion.
No BactoTraits row is expected for this target.
The 10 assembly entries and 8 genome records are expected after source cross-links.
The 720-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
