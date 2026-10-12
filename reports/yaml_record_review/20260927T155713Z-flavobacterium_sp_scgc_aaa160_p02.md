# YAML Record Review: Flavobacterium sp. SCGC AAA160-P02

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/flavobacterium_sp_scgc_aaa160_p02.yaml
- Started UTC: 2026-09-27T15:57:13Z
- Finished UTC: 2026-09-27T15:57:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/flavobacterium_sp_scgc_aaa160_p02.yaml` |
| Identifier | `NCBITaxon:1009412` |
| Label | `Flavobacterium sp. SCGC AAA160-P02` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:196869` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB-backed Bacteroidota unclassified-Flavobacterium
record, with path pinned by `data/taxa/PATHS.tsv:3153`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/flavobacterium_sp_scgc_aaa160_p02.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/staphylococcus_sp_wlsh_22.yaml data/taxa/bacteria/flavobacterium_sp_scgc_aaa160_p02.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa164_a08.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa164_b23.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 82 YAML lines, 12 lineage entries, 2 GTDB broadMatch taxonomy mappings, 1 NCBITAXON and 1 GTDB source attestation, 0 synonyms, 0 nomenclature entries, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009412` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211757`, 2 GTDB mapping rows at `data/raw/gtdb_mappings.tsv:1120-1121`, 12 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, 1 native GOLD organism, project, and analysis row, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009412` resolves to `Flavobacterium sp. SCGC AAA160-P02`, rank
`SPECIES`, parent `NCBITaxon:196869`, genetic code `11`, source set
`ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 12 committed NCBI rows, ending at
`NCBITaxon:196869` unclassified Flavobacterium under genus Flavobacterium.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank SCGC AAA160-P02 identity, direct
unclassified-Flavobacterium parent, genetic code, NCBITAXON source attestation,
and 2026-09-13 snapshot date. The seed event is supported by
`curation/seed_scope.tsv:65980`.

GTDB rows support two `skos:broadMatch` mappings: 19 genomes to
`GTDB:s__Polaribacter_sp000383355` and 1 genome to
`GTDB:s__Polaribacter_sp949541125`. They are pooled kg-microbe broadMatches,
not nomenclatural rows.

## Completeness

Native GOLD rows for `Go0012900` / `Gp0012900` are side evidence only: no GOLD
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
Two GTDB broadMatch rows are expected.
The GTDB mappings pool to `GTDB:g__Polaribacter` species.
Native GOLD rows were side evidence only.
No retained GOLD aggregate row is filed on this target.
No BacDive row was available to mint a strain.
No LPSN row was present for nomenclature.
No NCBI merge row complicates identity.
Twelve NCBI lineage rows are expected.
The 82-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
