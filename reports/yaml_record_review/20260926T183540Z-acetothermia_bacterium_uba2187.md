# YAML Record Review: Acetothermia bacterium UBA2187

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetothermia_bacterium_uba2187.yaml
- Started UTC: 2026-09-26T18:35:40Z
- Finished UTC: 2026-09-26T18:35:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetothermia_bacterium_uba2187.yaml` |
| Identifier | `NCBITaxon:1953092` |
| Label | `Acetothermia bacterium UBA2187` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1046990` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:312215`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetothermia_bacterium_uba2187.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetothermia_bacterium_jgi_g03_019.yaml data/taxa/bacteria/acetothermia_bacterium_jgi_h02_002.yaml data/taxa/bacteria/acetothermia_bacterium_scgc_aaa255_c06.yaml data/taxa/bacteria/acetothermia_bacterium_uba2187.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB closeMatch shape: 64 YAML lines, 7 lineage entries, 1 `skos:closeMatch` taxonomy mapping, 1 exact GTDB synonym, 1 GTDB xref, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, and 0 strains or causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/taxa/PATHS.tsv`; also found `GTDB:s__Bipolaricaulis_anaerobius` in the expected GTDB species, closeMatch, and broadMatch rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:503819`, 1 target-specific GTDB closeMatch row, 7 checked lineage entries with no missing rows or mismatches, and no LPSN, BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits rows for this target. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1953092` resolves in the committed NCBI inventory to label
`Acetothermia bacterium UBA2187`, rank `SPECIES`, parent
`NCBITaxon:1046990`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 7 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1046990` unclassified
Candidatus Bipolaricaulota. There are no retained old identifiers for this
target in the NCBI merge input.

## Evidence

The GTDB mapping is supported by `data/raw/gtdb_mappings.tsv:108435`, which
maps `GTDB:s__Bipolaricaulis_anaerobius` to this target with predicate
`skos:closeMatch` and `genome_count: 15`.

The seed event is supported by `curation/seed_scope.tsv:87736`, which records
`NCBITaxon:1953092` as added on `2026-09-13` with reason `attested rule:
Acetothermia bacterium UBA2187, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated GTDB-backed
record. The bounded scan found the expected GTDB closeMatch row and no LPSN,
BacDive, StrainInfo, normalized strain, NCBI type-material, GOLD, MediaDive,
Madin, BactoTraits, or NCBI merge row for this target.

The exact GTDB ID also appears in two other `skos:closeMatch` rows and three
`skos:broadMatch` rows to other NCBITaxon targets; those are not
target-specific rows for `NCBITaxon:1953092`.

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
