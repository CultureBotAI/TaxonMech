# YAML Record Review: gamma proteobacterium SCGC AAA168-I18

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gamma_proteobacterium_scgc_aaa168_i18.yaml
- Started UTC: 2026-09-27T16:09:46Z
- Finished UTC: 2026-09-27T16:09:46Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/gamma_proteobacterium_scgc_aaa168_i18.yaml` |
| Identifier | `NCBITaxon:1009425` |
| Label | `gamma proteobacterium SCGC AAA168-I18` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33811` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB-backed Gammaproteobacteria unclassified record,
with path pinned by `data/taxa/PATHS.tsv:3165`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa168_i18.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa168_f10.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa168_i18.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa168_p09.yaml data/taxa/bacteria/streptomyces_sp_ouc6819.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 64 YAML lines, 7 lineage entries, 1 GTDB closeMatch taxonomy mapping, 1 GTDB exact synonym, 1 GTDB xref, 1 NCBITAXON and 1 GTDB source attestation, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009425` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211769`, 1 GTDB mapping row at `data/raw/gtdb_mappings.tsv:1123`, 7 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, 1 native GOLD organism, project, and analysis row, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009425` resolves to `gamma proteobacterium SCGC AAA168-I18`,
rank `SPECIES`, parent `NCBITaxon:33811`, genetic code `11`, source set
`ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 7 committed NCBI rows, ending at
`NCBITaxon:33811` unclassified Gammaproteobacteria. The bounded scan found no
NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank SCGC AAA168-I18 identity, direct
unclassified-Gammaproteobacteria parent, genetic code, and 2026-09-13 snapshot
date. The seed event is supported by `curation/seed_scope.tsv:65982`.

The GTDB row supports the `skos:closeMatch` mapping, GTDB exact synonym and
xref, and GTDB source attestation for 3 genomes under
`GTDB:s__SCGC-AAA076-P13_sp000385055`.

## Completeness

Native GOLD rows for `Go0012912` / `Gp0012912` are side evidence only: no GOLD
aggregate or normalized genome/strain row was retained, and no BacDive, LPSN,
MediaDive, MADIN, BactoTraits, type-material, or StrainInfo row was filed under
this exact taxon.

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
One GTDB closeMatch row is expected.
The GTDB mapping mints the exact GTDB synonym and xref.
Native GOLD rows were side evidence only.
No retained GOLD aggregate row is filed on this target.
No BacDive row was available to mint a strain.
No LPSN row was present for nomenclature.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Seven NCBI lineage rows are expected.
The single GTDB mapping row is direct and exact-ID aligned.
The 64-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
