# YAML Record Review: Haloparvum alkalitolerans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/haloparvum_alkalitolerans.yaml
- Started UTC: 2026-09-27T14:34:27Z
- Finished UTC: 2026-09-27T14:34:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/haloparvum_alkalitolerans.yaml` |
| Identifier | `NCBITaxon:1042953` |
| Label | `Haloparvum alkalitolerans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1820337` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GOLD, GTDB, LPSN, and NCBI-backed archaeal
species record, with path pinned by `data/taxa/PATHS.tsv:16789`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/haloparvum_alkalitolerans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/haloparvum_alkalitolerans.yaml data/taxa/archaea/halophilic_archaeon_mk206_1.yaml data/taxa/archaea/uncultured_halomicrobium_sp.yaml data/taxa/archaea/uncultured_halogranum_sp.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 332 YAML lines, 10 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 2 related NCBI synonyms, 2 xrefs, 1 BacDive strain, 3 NCBI Assembly rows, 4 BV-BRC genome rows, 14 related records, 5 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1042953` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:224190`, 10 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 1 GTDB row at line 1748, 1 BacDive row, 1 retained GOLD aggregate row, 1 native GOLD organism row, 1 project, 1 analysis, 2 culture-collection rows, 3 normalized assemblies, 4 BV-BRC genome rows, 14 related rows, 6 type-material rows, and 0 exact StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1042953` resolves to `Haloparvum alkalitolerans`, rank `SPECIES`,
parent `NCBITaxon:1820337`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|gold`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
genus `NCBITaxon:1820337` Haloparvum. The bounded scan found no NCBI merge row
and no retained old-id row.

## Evidence

LPSN row `lpsn:794884` supports the nomenclature block, Kondo et al. 2016
authority, correct-name status, type strain IDs JCM-30442/KCTC-4214, two DOIs,
PMID:27666573, and sequence accession `INSDC:AB638839`.

The GTDB row supports the `GTDB:s__Haloparvum_alkalitolerans` closeMatch with
1 genome. BacDive row 133245 supports local strain `bacdive_133245`,
designation MK62-1, type-material culture IDs, `medium_count: 1`, 3 NCBI
Assembly rows, and 4 BV-BRC genome records.

Retained GOLD, native GOLD, and 14 strain related rows account for the
remaining generated source blocks. All generated related records stay under
the exact target taxon and no StrainInfo row was filed for this target.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, GOLD,
type-material, seed, path, strain, assembly, genome, and generated YAML inputs.

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
The GTDB closeMatch has 1 genome.
Native GOLD supplied one organism/project/analysis chain.
One retained GOLD aggregate row was filed on this target.
Three NCBI Assembly rows were materialized.
Four BV-BRC genome records were materialized.
Fourteen related records preserve exact-target side evidence.
Six NCBI type-material rows were checked.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 332-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
