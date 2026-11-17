# YAML Record Review: Nitrososphaera viennensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/nitrososphaera_viennensis.yaml
- Started UTC: 2026-09-27T14:15:42Z
- Finished UTC: 2026-09-27T14:15:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/nitrososphaera_viennensis.yaml` |
| Identifier | `NCBITaxon:1034015` |
| Label | `Nitrososphaera viennensis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:497726` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GTDB, LPSN, MADIN, and NCBI-backed archaeal
species record, with path pinned by `data/taxa/PATHS.tsv:13875`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/nitrososphaera_viennensis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/candidatus_aciduliprofundum_sp_lau09_cd652.yaml data/taxa/archaea/candidatus_aciduliprofundum_sp_lau09_cd1713.yaml data/taxa/archaea/halorhabdus_tiamatea_sarl4b.yaml data/taxa/archaea/nitrososphaera_viennensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 321 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 4 related NCBI synonyms, 2 xrefs, 1 BacDive strain, 3 genome assemblies, 5 genome records, 9 related records, 5 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1034015` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:221419`, 9 checked lineage entries with no missing rows or mismatches, 1 LPSN row at line 28787, 1 GTDB row at line 1390, 1 BacDive row, 1 MADIN row, 2 culture-collection rows, 1 exact StrainInfo row and 2 StrainInfo related rows, 6 NCBI type-material rows, 1 NCBI merge row from `NCBITaxon:945196`, 0 retained GOLD aggregate rows, no native GOLD organism, project, or analysis rows, and no exact-target MediaDive or BactoTraits rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1034015` resolves to `Nitrososphaera viennensis`, rank `SPECIES`,
parent `NCBITaxon:497726`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
genus `NCBITaxon:497726` Nitrososphaera. NCBI old ID `NCBITaxon:945196`
merges into the target and no retained old-id row was present.

## Evidence

The raw NCBI row supports the species identity, direct Nitrososphaera parent,
genetic code, four related NCBI synonyms, five-source source set, and snapshot
date. The seed event is supported by `curation/seed_scope.tsv:14831`.

LPSN row `lpsn:792004` supports the nomenclature block, Stieglmeier et al.
2014 authority, correct-name status, type strain IDs DSM-26422/JCM-19564, two
DOIs, PMID:24907263, and sequence accession `INSDC:FR773157`. The GTDB row
supports the `GTDB:s__Nitrososphaera_viennensis` closeMatch with 3 genomes.

BacDive row 24819 supports local strain `kgmicrobe.strain:bacdive_24819`,
designation EN76, 3 media, and DSM-26422/JCM-19564 culture IDs; StrainInfo
adds deposit/strain related records for DSM 26422.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, MADIN,
StrainInfo, type-material, seed, path, and generated YAML inputs.

No exact-target GOLD aggregate, native GOLD, MediaDive, or BactoTraits rows
are filed under this taxon; generated GOLD/BV-BRC genome records are attached
through the EN76 strain child `NCBITaxon:926571`.

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
`strain_count: 1` matches the exact BacDive strain row.
The LPSN row links to the same GTDB species.
The GTDB closeMatch has 3 genomes.
Six exact NCBI type-material rows support EN76 and its deposit IDs.
The `NCBITaxon:945196` merge is already resolved to this target.
Nine NCBI lineage rows are expected.
The 321-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
