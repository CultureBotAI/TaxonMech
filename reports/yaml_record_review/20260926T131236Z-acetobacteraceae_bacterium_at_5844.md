# YAML Record Review: Acetobacteraceae bacterium AT-5844

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteraceae_bacterium_at_5844.yaml
- Started UTC: 2026-09-26T13:12:36Z
- Finished UTC: 2026-09-26T13:12:36Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacteraceae_bacterium_at_5844.yaml` |
| Identifier | `NCBITaxon:1054213` |
| Label | `Acetobacteraceae bacterium AT-5844` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:41293` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:20514`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium_at_5844.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium_at_5844.yaml data/taxa/bacteria/acetobacteraceae_bacterium_b01_35.yaml data/taxa/bacteria/acetobacteraceae_bacterium_b02_15.yaml data/taxa/bacteria/acetobacteraceae_bacterium_b03_42.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected seeded shape: 9 lineage entries, 1 GTDB close-match mapping, 1 GTDB exact synonym, 1 GTDB xref, 3 source attestations, 0 nomenclature rows, 0 strains, 0 definitions, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier and label in the expected `curation/seed_scope.tsv`, `curation/legacy_page_paths.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/raw/madin_taxa.tsv` rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:227721`, the GTDB row at `data/raw/gtdb_mappings.tsv:2182`, the Madin row at `data/raw/madin_taxa.tsv:1196`, 9 checked lineage entries with no missing rows or mismatches, no retained old IDs, and no BacDive, StrainInfo, strain, LPSN, MediaDive, BactoTraits, or raw GOLD aggregate rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1054213` resolves in the committed NCBI inventory to label
`Acetobacteraceae bacterium AT-5844`, rank `SPECIES`, parent
`NCBITaxon:41293`, genetic code `11`, and taxonomy snapshot `2026-09-13`. The
record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:41293` unclassified
Acetobacteraceae. There are no retained old identifiers for this target in the
NCBI merge input.

The GTDB mapping from `GTDB:s__Pseudoroseomonas_sp000245075` is a
`skos:closeMatch` with `genome_count: 1`, so the GTDB xref, exact synonym
`Pseudoroseomonas sp000245075`, and the `GTDB` source attestation are scoped to
the exact source species mapping rather than a pooled broad match.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1054213`, source label `Acetobacteraceae bacterium AT-5844`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The `GTDB` mapping, synonym, xref, and source attestation are supported by
`data/raw/gtdb_mappings.tsv:2182`, whose GTDB ID, GTDB label, close-match
predicate, NCBI target, and genome count agree with the record.

The `MADIN` source attestation is supported by `data/raw/madin_taxa.tsv:1196`,
which carries `assertion_count: 1` for `NCBITaxon:1054213`.

The seed event is supported by `curation/seed_scope.tsv:36382`, which records
`NCBITaxon:1054213` as added on `2026-09-12` with reason
`attested rule: Acetobacteraceae bacterium AT-5844, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this GTDB/Madin/NCBI seeded
record. The bounded scan found no rows for this target in the LPSN, BacDive,
StrainInfo, strain, NCBI merged, MediaDive, or BactoTraits inputs, so the
empty nomenclature, strain, definition, and causal graph sections are
consistent with the inspected local sources.

The exact ignored-aware source scan found the legacy page path row for this
identifier at `curation/legacy_page_paths.tsv:1615` and found no prior history
or ignored review report mentioning this target before this report was written;
ignored files under `reports/` were included.

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

The bounded native GOLD scan found one organism, one project, and one analysis
for `1054213` in `data/gold/`, but no raw GOLD aggregate or supported
strain/genome rows were present for the record to expose.

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML.
