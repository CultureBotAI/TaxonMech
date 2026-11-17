# YAML Record Review: Achromobacter sp. JD-1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_jd_1.yaml
- Started UTC: 2026-09-27T08:13:26Z
- Finished UTC: 2026-09-27T08:13:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_jd_1.yaml` |
| Identifier | `NCBITaxon:3128540` |
| Label | `Achromobacter sp. JD-1` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI and GTDB inputs. Its path is
pinned by `data/taxa/PATHS.tsv:426923`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_jd_1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_jcm_28662.yaml data/taxa/bacteria/achromobacter_sp_jcm_28709.yaml data/taxa/bacteria/achromobacter_sp_jd417.yaml data/taxa/bacteria/achromobacter_sp_jd_1.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB-backed shape: 73 YAML lines, 10 lineage entries, 1 NCBI and 1 GTDB source attestation, 1 `skos:closeMatch` GTDB mapping, 1 GTDB exact synonym, 1 GTDB xref, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found the NCBI and GTDB identifiers in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:604700`, the GTDB row at `data/raw/gtdb_mappings.tsv:262831`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:3128540` resolves in the committed NCBI inventory to label
`Achromobacter sp. JD-1`, rank `SPECIES`, parent `NCBITaxon:2626865`, genetic
code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`.
The generated record carries those same identity fields and correctly lands in
the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and has no NCBI
synonyms to project. The GTDB row supports the `skos:closeMatch` mapping, the
`Achromobacter spanius C` exact synonym, GTDB xref, 6-genome GTDB attestation,
and `GTDB:s__Achromobacter_spanius_C` source assertion.

The seed event is supported by `curation/seed_scope.tsv:121411`, which records
`NCBITaxon:3128540` as added on `2026-09-13` with reason `attested rule:
Achromobacter sp. JD-1, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent. The exact and bounded scans account
for the expected NCBI, GTDB, seed, path, and generated YAML inputs, and found no
omitted NCBI merge, NCBI type-material, LPSN, GOLD, BacDive, MediaDive, MADIN,
BactoTraits, StrainInfo, ATB, culture-collection, normalized assembly,
normalized genome, normalized related-record, native GOLD row, or StrainInfo
exclusion row for this taxon.

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
YAML, and it found no upstream side rows to stage for follow-up
curation.
