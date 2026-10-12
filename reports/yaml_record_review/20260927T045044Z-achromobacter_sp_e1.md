# YAML Record Review: Achromobacter sp. E1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_e1.yaml
- Started UTC: 2026-09-27T04:50:44Z
- Finished UTC: 2026-09-27T04:50:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_e1.yaml` |
| Identifier | `NCBITaxon:3141581` |
| Label | `Achromobacter sp. E1` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI and GTDB inputs. Its path is
pinned by `data/taxa/PATHS.tsv:428708`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_e1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_e06_11b_jo.yaml data/taxa/bacteria/achromobacter_sp_e1.yaml data/taxa/bacteria/achromobacter_sp_e2bcu_s8.yaml data/taxa/bacteria/achromobacter_sp_e4l5.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB-backed shape: 73 YAML lines, 10 lineage entries, 2 source attestations, 1 `skos:closeMatch` GTDB mapping, 1 GTDB exact synonym, 1 GTDB xref, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found this identifier in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no generated side-reference rows; found no prior ignored report for this identifier. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:606294`, the GTDB mapping row at `data/raw/gtdb_mappings.tsv:263850`, 10 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row for old `NCBITaxon:3122409`, and 0 GOLD aggregate, LPSN, BacDive, MediaDive, MADIN, BactoTraits, type-material, native GOLD, normalized strain, normalized genome, normalized related-record, or StrainInfo rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:3141581` resolves in the committed NCBI inventory to label
`Achromobacter sp. E1`, rank `SPECIES`, parent `NCBITaxon:2626865`, genetic
code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`.
The generated record carries those same identity fields and lands in the
`bacteria` path bucket.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found one NCBI merge from old
`NCBITaxon:3122409` into this active identifier and no retained old-id row to
project.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation. The GTDB mapping row
maps `GTDB:s__Achromobacter_mucicolens` to `NCBITaxon:3141581` with predicate
`skos:closeMatch` and genome count 44, supporting the `GTDB` source
attestation, xref, mapping, and exact synonym `Achromobacter mucicolens`.

The bounded scan found no native GOLD organism, project, or analysis row and no retained GOLD aggregate or eligible local strain for this target.

The seed event is supported by `curation/seed_scope.tsv:122102`, which records
`NCBITaxon:3141581` as added on `2026-09-13` with reason `attested rule:
Achromobacter sp. E1, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans found no retained GOLD aggregate, LPSN, BacDive, MediaDive,
MADIN, BactoTraits, NCBI type-material, ATB, native GOLD, normalized
strain/genome/related-record, or StrainInfo row to project.

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

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML.
