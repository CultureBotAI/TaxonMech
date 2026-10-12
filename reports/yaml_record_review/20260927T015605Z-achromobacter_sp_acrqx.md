# YAML Record Review: Achromobacter sp. ACRQX

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_acrqx.yaml
- Started UTC: 2026-09-27T01:56:05Z
- Finished UTC: 2026-09-27T01:56:05Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_acrqx.yaml` |
| Identifier | `NCBITaxon:2918181` |
| Label | `Achromobacter sp. ACRQX` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI and GTDB inputs. Its path is
pinned by `data/taxa/PATHS.tsv:392140`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_acrqx.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_acm04.yaml data/taxa/bacteria/achromobacter_sp_acm05.yaml data/taxa/bacteria/achromobacter_sp_acrqx.yaml data/taxa/bacteria/achromobacter_sp_adc_31.yaml` | Passed strict validation with 4 files scanned, 0 files in error, and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 73 YAML lines, 10 lineage entries, 2 source attestations, 1 `skos:closeMatch`, 1 GTDB exact synonym, 1 GTDB xref, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found this identifier in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no generated side-reference rows; found no prior ignored report for this identifier. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:571330`, the GTDB mapping row at `data/raw/gtdb_mappings.tsv:234034`, 10 checked lineage entries with no missing rows or mismatches, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive, LPSN, MediaDive, MADIN, or BactoTraits rows, no normalized strain rows, and no StrainInfo assembly or related rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2918181` resolves in the committed NCBI inventory to label
`Achromobacter sp. ACRQX`, rank `SPECIES`, parent `NCBITaxon:2626865`,
genetic code `11`, source set `ncbitaxon|gtdb`, and snapshot `2026-09-13`.
The generated record carries those same identity fields and correctly lands in
the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation. It has no exact,
related, or broad NCBI synonyms to project into the generated record.

The GTDB row maps `GTDB:s__Achromobacter_animicus` to this taxon with
`skos:closeMatch` and genome count `18`, supporting the GTDB source attestation,
xref, taxonomy mapping, and exact synonym `Achromobacter animicus`.

The generated record correctly contains no native GOLD, BacDive, LPSN,
MediaDive, MADIN, BactoTraits, strain, genome, or related-record sections.

The seed event is supported by `curation/seed_scope.tsv:109119`, which records
`NCBITaxon:2918181` as added on `2026-09-13` with reason `attested rule:
Achromobacter sp. ACRQX, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The scans
account for the expected NCBI, GTDB, seed, path, generated YAML, and raw-source
inputs, and found no omitted NCBI merge, NCBI type-material, retained GOLD
aggregate, LPSN, BacDive, MediaDive, MADIN, BactoTraits, ATB,
culture-collection, normalized assembly, normalized genome, normalized
related-record, StrainInfo, or StrainInfo exclusion row for this taxon.

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
This read-only generated-record review did not append a curation event, promote
`mapping_status`, write a history record, or touch the seeded YAML.
