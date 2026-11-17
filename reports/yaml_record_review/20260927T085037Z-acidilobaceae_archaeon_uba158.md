# YAML Record Review: Acidilobaceae archaeon UBA158

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidilobaceae_archaeon_uba158.yaml
- Started UTC: 2026-09-27T08:50:37Z
- Finished UTC: 2026-09-27T08:50:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidilobaceae_archaeon_uba158.yaml` |
| Identifier | `NCBITaxon:1915614` |
| Label | `Acidilobaceae archaeon UBA158` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1915610` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB-backed NCBI species record, with path pinned by
`data/taxa/PATHS.tsv:302218` and fields owned by generated inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidilobaceae_archaeon_uba158.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_uzoniensis.yaml data/taxa/archaea/acidilobaceae_archaeon.yaml data/taxa/archaea/acidilobaceae_archaeon_uba158.yaml data/taxa/archaea/acidilobaceae_archaeon_uba162.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 70 YAML lines, 9 lineage entries, 1 GTDB `closeMatch`, 1 GTDB exact synonym, 1 xref, 1 NCBI source attestation, 1 GTDB genome attestation, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1915614` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:494273`, the GTDB row at `data/raw/gtdb_mappings.tsv:95587`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, BactoTraits, normalized strain, normalized genome, normalized related-record, or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1915614` resolves to label `Acidilobaceae archaeon UBA158`, rank
`SPECIES`, parent `NCBITaxon:1915610`, genetic code `11`, source set
`ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`. The generated record
carries those same NCBI-owned fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1915610` unclassified
Acidilobaceae. The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

GTDB species `GTDB:s__Caldisphaera_sp002506595` maps to this taxon with
`skos:closeMatch` and `genome_count: 1`; the generated mapping, xref, GTDB
attestation, and `Caldisphaera sp002506595` exact synonym mirror that row.

The NCBI row has no synonym to project. The generated record correctly contains
no LPSN nomenclature, strain, genome assembly, genome record, or related-record
sections.

The seed event is supported by `curation/seed_scope.tsv:81200`, which records
`NCBITaxon:1915614` as added on `2026-09-13` with reason `attested rule:
Acidilobaceae archaeon UBA158, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. Exact and
bounded scans accounted for expected NCBI, GTDB mapping, seed, path, and YAML
inputs, and found no omitted NCBI merge, type-material, LPSN, GOLD, BacDive,
MediaDive, MADIN, BactoTraits, normalized strain, normalized genome,
normalized related-record, or StrainInfo row.

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
The GTDB mapping is a species-level `closeMatch`, not a broader pooled mapping.
No LPSN nomenclature row accompanies the provisional NCBI isolate name.
No normalized strain base row exists, so `strain_count: 0` is expected.
The unclassified `Acidilobaceae` parent matches the committed NCBI parent row.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
The report therefore has no follow-up curation item.
The ignored report probe included gitignored files.
