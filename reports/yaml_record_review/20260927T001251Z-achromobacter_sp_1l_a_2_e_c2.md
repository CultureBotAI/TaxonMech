# YAML Record Review: Achromobacter sp. 1L-A-2-E-C2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_1l_a_2_e_c2.yaml
- Started UTC: 2026-09-27T00:12:51Z
- Finished UTC: 2026-09-27T00:12:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_1l_a_2_e_c2.yaml` |
| Identifier | `NCBITaxon:3696435` |
| Label | `Achromobacter sp. 1L-A-2-E-C2` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI input only. Its path is
pinned by `data/taxa/PATHS.tsv:477344`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_1l_a_2_e_c2.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_178r.yaml data/taxa/bacteria/achromobacter_sp_18p8_1_1.yaml data/taxa/bacteria/achromobacter_sp_1ap2.yaml data/taxa/bacteria/achromobacter_sp_1l_a_2_e_c2.yaml` | Passed strict validation with 4 files scanned, 0 files in error, and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 NCBI source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact ID-only `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no generated side-reference rows; found no prior ignored report for this identifier. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:642647`, 10 checked lineage entries with no missing rows or mismatches, 1 native GOLD organism, 1 native GOLD project, 1 native GOLD analysis, 0 NCBI merge rows, and 0 GOLD aggregate, LPSN, GTDB, BacDive, MediaDive, MADIN, BactoTraits, type-material, normalized strain, normalized genome, normalized related-record, or StrainInfo rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:3696435` resolves in the committed NCBI inventory to label
`Achromobacter sp. 1L-A-2-E-C2`, rank `SPECIES`, parent
`NCBITaxon:2626865`, genetic code `11`, source set `ncbitaxon`, and taxonomy
snapshot `2026-09-13`. The generated record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and has no exact,
related, or broad synonyms to project. The generated record correctly contains
no LPSN, GTDB, xref, strain, genome, or related-record sections.

The native GOLD organism `Go0714191`, project `Gp0873783`, and joined analysis
are side evidence only without a retained aggregate or eligible local strain.

The seed event is supported by `curation/seed_scope.tsv:618442`, which records
`NCBITaxon:3696435` as added on `2026-09-13` with reason `attested rule:
Achromobacter sp. 1L-A-2-E-C2, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans found no retained GOLD aggregate, LPSN, GTDB, BacDive,
MediaDive, MADIN, BactoTraits, NCBI type-material, merge, ATB, normalized
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
