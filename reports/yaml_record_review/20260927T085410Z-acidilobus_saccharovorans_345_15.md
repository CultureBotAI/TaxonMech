# YAML Record Review: Acidilobus saccharovorans 345-15

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidilobus_saccharovorans_345_15.yaml
- Started UTC: 2026-09-27T08:54:10Z
- Finished UTC: 2026-09-27T08:54:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidilobus_saccharovorans_345_15.yaml` |
| Identifier | `NCBITaxon:666510` |
| Label | `Acidilobus saccharovorans 345-15` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:242703` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated strain-taxon record with GTDB and MADIN support, with
path pinned by `data/taxa/PATHS.tsv:564364`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidilobus_saccharovorans_345_15.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidilobales_archaeon.yaml data/taxa/archaea/acidilobus_aceticus.yaml data/taxa/archaea/acidilobus_saccharovorans.yaml data/taxa/archaea/acidilobus_saccharovorans_345_15.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 87 YAML lines, 10 lineage entries, 1 GTDB `closeMatch`, 4 exact synonyms, 1 xref, 3 source attestations, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:666510` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:154411`, the GTDB row at `data/raw/gtdb_mappings.tsv:301651`, 10 checked lineage entries, 1 MADIN row with 5 assertions, 1 native GOLD organism, 1 native GOLD project, 1 native GOLD analysis, 2 raw strain-assembly rows, 3 raw strain-genome rows, 5 raw strain-related rows, 0 NCBI merge rows, 0 type-material rows, and no BacDive base-strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:666510` resolves to label `Acidilobus saccharovorans 345-15`, rank
`STRAIN`, parent `NCBITaxon:242703`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`. The generated
record carries those same NCBI-owned fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through species `NCBITaxon:242703` Acidilobus
saccharovorans. The bounded scan found no NCBI merge row.

## Evidence

GTDB species `GTDB:s__Acidilobus_saccharovorans` maps to this strain taxon with
`skos:closeMatch` and `genome_count: 1`; the generated mapping, xref, GTDB
attestation, and `Acidilobus saccharovorans` exact synonym mirror that row.

The three NCBI exact synonyms for `str. 345-15`, `strain 345-15`, and
`Acidilobus sp. 345-15` are all emitted. MADIN contributes 5 assertions.

Native GOLD and normalized raw tables carry assembly, genome, BioProject,
BioSample, GOLD analysis, GOLD organism, and GOLD project rows for DSM 16705,
but no base `data/raw/bacdive_strains.tsv` row names `NCBITaxon:666510`.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, MADIN, native GOLD, normalized
genome-side evidence, seed, path, and YAML inputs, and found no omitted NCBI
merge, type-material, LPSN, BactoTraits, MediaDive, retained GOLD aggregate,
BacDive base-strain, or StrainInfo row.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

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
`strain_count: 0` is expected without a retained base strain row on this taxon.
The raw 345-15 genome rows are represented on the parent species strain section.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
The report therefore has no follow-up curation item.
No LPSN row maps directly to the strain taxon.
No MediaDive aggregate row is filed on this strain taxon.
No retained GOLD aggregate row is filed on this strain taxon.
The ignored report probe included gitignored files.
