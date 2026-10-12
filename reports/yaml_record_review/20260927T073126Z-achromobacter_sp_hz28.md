# YAML Record Review: Achromobacter sp. HZ28

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_hz28.yaml
- Started UTC: 2026-09-27T07:31:26Z
- Finished UTC: 2026-09-27T07:31:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_hz28.yaml` |
| Identifier | `NCBITaxon:2015171` |
| Label | `Achromobacter sp. HZ28` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI and GTDB inputs. Its path
is pinned by `data/taxa/PATHS.tsv:319774`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_hz28.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_hz28.yaml data/taxa/bacteria/achromobacter_sp_hz34.yaml data/taxa/bacteria/achromobacter_sp_i12b_00880.yaml data/taxa/bacteria/achromobacter_sp_i_43_j6pa9a.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 73 YAML lines, 10 lineage entries, 1 NCBI and 1 GTDB source attestation, 0 nomenclature entries, 1 taxonomy mapping, 1 synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found this identifier in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:510650`, the GTDB row at `data/raw/gtdb_mappings.tsv:121721`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, 1 native GOLD organism, 1 native GOLD project, 1 native GOLD analysis row, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, no direct StrainInfo or StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2015171` resolves in the committed NCBI inventory to label
`Achromobacter sp. HZ28`, rank `SPECIES`, parent `NCBITaxon:2626865`, genetic
code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`.
The generated record carries those same identity fields and correctly lands in
the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation, while the GTDB
mapping row supports the `skos:closeMatch` to
`GTDB:s__Bordetella_C_sp002209485`, the matching xref, the normalized exact
synonym `Bordetella C sp002209485`, and the 2-genome GTDB attestation.

The native GOLD organism, project, and analysis rows for `Go0493389` and
`Gp0377382` are side evidence only because no normalized GOLD aggregate row was emitted.

The seed event is supported by `curation/seed_scope.tsv:90363`, which records
`NCBITaxon:2015171` as added on `2026-09-13` with reason `attested rule:
Achromobacter sp. HZ28, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent. Exact and bounded scans account
for expected NCBI, GTDB mapping, seed, path, native GOLD, and generated YAML
inputs, and found no omitted NCBI merge, NCBI type-material, LPSN, BacDive,
MediaDive, MADIN, BactoTraits, StrainInfo, ATB, culture-collection,
normalized assembly, normalized genome, normalized related-record, or
StrainInfo exclusion row for this taxon.

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

This was a read-only generated-record review. It did not append a curation event, promote `mapping_status`, write a history record, touch the seeded YAML, or find upstream rows that require follow-up curation.
