# YAML Record Review: Methanobacterium movilense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/methanobacterium_movilense.yaml
- Started UTC: 2026-09-27T14:23:34Z
- Finished UTC: 2026-09-27T14:23:34Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/methanobacterium_movilense.yaml` |
| Identifier | `NCBITaxon:1036678` |
| Label | `Methanobacterium movilense` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2160` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GOLD, LPSN, MediaDive, MADIN, and NCBI-backed
archaeal species record, with path pinned by `data/taxa/PATHS.tsv:15097`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/methanobacterium_movilense.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/uncultured_methanogen_r9.yaml data/taxa/archaea/uncultured_thermogymnomonas_sp.yaml data/taxa/archaea/methanosarcina_soligelidi.yaml data/taxa/archaea/methanobacterium_movilense.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 322 YAML lines, 10 lineage entries, 1 LPSN nomenclature entry, 2 related NCBI synonyms, 1 xref, 1 BacDive strain, 2 NCBI Assembly rows, 2 BV-BRC genome records, 14 related records, 6 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1036678` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:222579`, 10 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 1 BacDive row, 1 MADIN row, 1 MediaDive row, 1 retained GOLD aggregate row, 3 native GOLD organism rows, no native GOLD project or analysis rows, 2 culture-collection rows, 2 NCBI Assembly rows, 2 BV-BRC genome rows, 12 exact normalized related rows, 2 StrainInfo related rows, 6 type-material rows, and 0 GTDB or NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1036678` resolves to `Methanobacterium movilense`, rank `SPECIES`,
parent `NCBITaxon:2160`, genetic code `11`, source set
`ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
genus `NCBITaxon:2160` Methanobacterium. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

LPSN row `lpsn:791527` supports the nomenclature block, Schirmack et al. 2014
authority, correct-name status, type strain IDs DSM-26032/JCM-18470, two DOIs,
PMID:24108325, and sequence accession `INSDC:JF812256`.

BacDive row 24154 supports local strain `bacdive_24154`, designation MC-20,
and DSM-26032/JCM-18470 culture IDs. NCBI Assembly, BV-BRC, GOLD, and
StrainInfo rows add the generated genome and related-record evidence.

MediaDive, MADIN, the retained GOLD aggregate, and three native GOLD organism
rows account for the remaining source attestations. No GTDB row is filed under
this exact taxon.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, MediaDive, MADIN,
GOLD, NCBI Assembly, BV-BRC, StrainInfo, type-material, seed, path, and
generated YAML inputs.

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
The record correctly has no GTDB mapping section.
Native GOLD supplied three organism rows.
Two NCBI Assembly rows were materialized.
Two BV-BRC genome rows were materialized.
The generated record materializes 14 related records.
Six NCBI type-material rows were checked.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 322-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
