# YAML Record Review: Acidilobaceae archaeon

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidilobaceae_archaeon.yaml
- Started UTC: 2026-09-27T08:50:37Z
- Finished UTC: 2026-09-27T08:50:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidilobaceae_archaeon.yaml` |
| Identifier | `NCBITaxon:2933264` |
| Label | `Acidilobaceae archaeon` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1915610` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI and pooled GTDB record, with path pinned by
`data/taxa/PATHS.tsv:394355` and fields owned by generated inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidilobaceae_archaeon.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_uzoniensis.yaml data/taxa/archaea/acidilobaceae_archaeon.yaml data/taxa/archaea/acidilobaceae_archaeon_uba158.yaml data/taxa/archaea/acidilobaceae_archaeon_uba162.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 301 YAML lines, 9 lineage entries, 34 GTDB broadMatch mappings, 1 NCBI exact synonym, 2 source attestations, 0 xrefs, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:2933264` in the expected seed, NCBI, 34 consecutive GTDB mapping rows, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:573390`, 9 checked lineage entries with no missing rows or mismatches, 34 GTDB broadMatch rows, 1 NCBI merge row from old `NCBITaxon:2614261`, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, and no BacDive, LPSN, MediaDive, MADIN, BactoTraits, normalized strain, or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:2933264` resolves to label `Acidilobaceae archaeon`, rank
`SPECIES`, parent `NCBITaxon:1915610`, genetic code `11`, source set
`ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`. The generated record
carries those same NCBI-owned fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1915610` unclassified
Acidilobaceae. The bounded scan found old `NCBITaxon:2614261` merged here.

## Evidence

The NCBI exact synonym `Caldisphaeraceae archaeon` is projected into the
generated synonym section.

The 34 GTDB mapping rows are all `skos:broadMatch` rows for pooled GTDB species.
The generated record emits all 34 rows and summarizes the top
`GTDB:s__DSZV01_sp030549835` mapping with 31 genomes in the GTDB attestation,
with a note that 33 additional GTDB species pool onto this NCBI taxon.

No retained GTDB mapping is a `closeMatch`, and the record accordingly has no
GTDB exact synonym or GTDB xref section.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, 34 GTDB mappings, the NCBI merge,
seed, path, and YAML inputs, and found no omitted NCBI type-material, LPSN,
GOLD, BacDive, MediaDive, MADIN, BactoTraits, normalized strain, normalized
genome, normalized related-record, or StrainInfo row.

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
The old NCBI ID is merge-only and is not emitted as a synonym.
The broad GTDB species span Aeropyrum, Caldisphaera, Calypsonella, DSZV01,
JALURD01, JALWTO01, JAWAWX01, S012-22, S141-84, S143-63, Thermodiscus, and
WAQN01 placeholder genera.
The unclassified family-level parent means the 9-entry lineage is expected.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
The report therefore has no follow-up curation item.
The ignored report probe included gitignored files.
