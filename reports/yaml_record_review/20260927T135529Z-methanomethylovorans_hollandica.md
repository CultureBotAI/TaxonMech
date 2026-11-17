# YAML Record Review: Methanomethylovorans hollandica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/methanomethylovorans_hollandica.yaml
- Started UTC: 2026-09-27T13:55:29Z
- Finished UTC: 2026-09-27T13:55:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/methanomethylovorans_hollandica.yaml` |
| Identifier | `NCBITaxon:101192` |
| Label | `Methanomethylovorans hollandica` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:101191` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | `1` |

The file is an NCBITaxon/LPSN/BacDive/GOLD/MADIN species record, with path
pinned by `data/taxa/PATHS.tsv:5040`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/methanomethylovorans_hollandica.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/crenarchaeote_scgc_aaa160_j20.yaml data/taxa/archaea/methanomethylovorans_hollandica.yaml data/taxa/archaea/halobaculum_magnesiiphilum.yaml data/taxa/archaea/nitrosopumilus_sp_ar.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 647 YAML lines, 10 lineage entries, 5 source attestations, 1 LPSN nomenclature entry, 0 taxonomy mappings, 2 synonyms, 2 xrefs, 1 BacDive strain, 12 genome assemblies, 9 genome records, 28 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:101192` in the expected seed, NCBI, `PATHS.tsv`, and generated YAML rows; found no direct exact GTDB mapping row and no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17462`, 10 checked lineage entries with no mismatches, 1 LPSN row, 1 MADIN row with 10 assertions, 1 BacDive row, 1 GOLD aggregate row, 1 native GOLD organism, 2 same-taxon GOLD related rows, 1 StrainInfo assembly row, 2 StrainInfo related rows, 6 NCBI type-material rows, and 1 NCBI merge row. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101192` resolves to `Methanomethylovorans hollandica`, rank `SPECIES`,
parent `NCBITaxon:101191`, genetic code `11`, source set
`ncbitaxon|lpsn|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:101191` Methanomethylovorans. Old `NCBITaxon:225462` maps here in
the NCBI merge side table, but no retained old-id row is present.

## Evidence

The NCBI row supports the species identity, Methanomethylovorans parent,
genetic code, two generated related synonyms, source set, and snapshot date.
The seed event is supported by `curation/seed_scope.tsv:23610`.

The LPSN row at `data/raw/lpsn_names.tsv:18131` supports the legitimate,
validly published correct species name, `lpsn:777910`, the LPSN URL, DSM-15978
as type strain, two DOIs, one PMID, `INSDC:AF120163`, and the LPSN xref.

BacDive `7053` supports the single generated strain. The retained genome and
related-record payloads are backed by descendant strain `NCBITaxon:867904`,
StrainInfo strain `131425`, GOLD organism `Go0003615`, and side GOLD organism
`Go0627357` for NBRC 107637.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, GOLD, MADIN,
StrainInfo, type-material, seed, path, and generated YAML inputs.

The native GOLD row for NBRC 107637 is side evidence only and is represented
as two retained GOLD related records without a new BacDive-derived strain.

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
`strain_count: 1` matches the single BacDive row for this species.
The BacDive row also names descendant strain `NCBITaxon:867904`.
GOLD source attestations follow the retained aggregate row for this target.
No direct exact GTDB mapping row is filed under this NCBI taxon.
No BactoTraits or MediaDive rows were present for this target.
No retained old identifier is generated for the side NCBI merge row.
The ignored report probe included gitignored files.
The 647-line YAML shape is expected for this target.
