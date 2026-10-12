# YAML Record Review: Halobaculum magnesiiphilum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halobaculum_magnesiiphilum.yaml
- Started UTC: 2026-09-27T13:55:29Z
- Finished UTC: 2026-09-27T13:55:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/halobaculum_magnesiiphilum.yaml` |
| Identifier | `NCBITaxon:1017351` |
| Label | `Halobaculum magnesiiphilum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:43927` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | `2` |

The file is an NCBITaxon/LPSN/GTDB/BacDive/GOLD/MADIN species record, with
path pinned by `data/taxa/PATHS.tsv:10341`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/halobaculum_magnesiiphilum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/crenarchaeote_scgc_aaa160_j20.yaml data/taxa/archaea/methanomethylovorans_hollandica.yaml data/taxa/archaea/halobaculum_magnesiiphilum.yaml data/taxa/archaea/nitrosopumilus_sp_ar.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 627 YAML lines, 10 lineage entries, 6 source attestations, 1 LPSN nomenclature entry, 1 GTDB closeMatch mapping, 3 synonyms, 2 xrefs, 2 BacDive strains, 11 genome assemblies, 11 genome records, 26 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1017351` in the expected seed, NCBI, GTDB mapping, `PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:218678`, 10 checked lineage entries with no mismatches, 1 LPSN row, 1 GTDB row, 1 MADIN row with 11 assertions, 2 BacDive rows, 4 culture-collection rows, 11 strain assembly rows, 11 genome rows, 26 related rows, 1 GOLD aggregate row, 2 native GOLD organisms, 1 native GOLD project, 1 native GOLD analysis, 8 NCBI type-material rows, and 1 NCBI merge row. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1017351` resolves to `Halobaculum magnesiiphilum`, rank `SPECIES`,
parent `NCBITaxon:43927`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:43927` Halobaculum. Old `NCBITaxon:1017352` maps here in the NCBI
merge side table, but no retained old-id row is present.

## Evidence

The NCBI row supports the species identity, Halobaculum parent, genetic code,
three generated related synonyms, source set, and snapshot date. The seed
event is supported by `curation/seed_scope.tsv:9028`.

The LPSN row at `data/raw/lpsn_names.tsv:27519` supports the legitimate,
validly published correct name, `lpsn:790578`, two type-strain designations,
two DOIs, one PMID, `INSDC:AB627357`, and the LPSN and GTDB xrefs.

GTDB `s__Halobaculum_magnesiiphilum` is a supported one-genome closeMatch.
BacDive rows `133787` and `162116`, native GOLD organisms `Go0043820` and
`Go0593690`, and project `Gp0607635` account for the retained strain payload.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, GOLD, MADIN,
type-material, seed, path, culture-collection, and generated strain rows.

The native GOLD organism, project, and analysis rows agree with the retained
GOLD-derived assembly, genome, and related-record rows for NBRC 109044.

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
`strain_count: 2` matches the two exact BacDive rows for this species.
The JCM, KCTC, and NBRC culture identifiers are all exact target rows.
`GTDB:s__Halobaculum_magnesiiphilum` has `skos:closeMatch` with one genome.
No StrainInfo rows were present for this target.
No BactoTraits or MediaDive rows were present for this target.
No retained old identifier is generated for the side NCBI merge row.
The ignored report probe included gitignored files.
Native GOLD also listed side organism `Go0043820` for KCTC 4100.
The 627-line YAML shape is expected for this target.
