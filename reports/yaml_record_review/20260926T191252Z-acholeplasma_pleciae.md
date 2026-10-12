# YAML Record Review: Acholeplasma pleciae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_pleciae.yaml
- Started UTC: 2026-09-26T19:12:52Z
- Finished UTC: 2026-09-26T19:12:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_pleciae.yaml` |
| Identifier | `NCBITaxon:228419` |
| Label | `Acholeplasma pleciae` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2147` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:336114`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_pleciae.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_palmae.yaml data/taxa/bacteria/acholeplasma_pleciae.yaml data/taxa/bacteria/acholeplasma_sp.yaml data/taxa/bacteria/acholeplasma_sp_assh51.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact generated shape: 104 YAML lines, 9 lineage entries, 4 source attestations, 1 nomenclature entry, 0 taxonomy mappings, 4 synonyms, 1 xref, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, LPSN, Madin, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:44738`, 9 checked lineage entries with no missing rows or mismatches, the LPSN row at `data/raw/lpsn_names.tsv:21376`, 1 Madin row, 1 GOLD aggregate row, 1 native GOLD organism, 1 direct StrainInfo strain with 2 deposits, 6 NCBI type-material rows, 0 NCBI merge rows, and 0 GTDB, BacDive, BactoTraits, MediaDive, or normalized strain rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:228419` resolves in the committed NCBI inventory to label
`Acholeplasma pleciae`, rank `SPECIES`, parent `NCBITaxon:2147`, genetic code
`11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2147` Acholeplasma. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:228419`, source label `Acholeplasma pleciae`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The nomenclature block is backed by `lpsn:783260`, a legitimate, validly
published LPSN species row whose type strains are `ATCC-49582` and
`NBRC-100476`. Its LPSN synonym `lpsn:784204` and the committed NCBI exact
and related synonyms account for all 4 stored synonyms.

The `GOLD` source attestation is supported by the aggregate row and native
organism `Go0018722` for ATCC 49582. That organism has no project or analysis
descendant, so no assembly, genome, or related-record payload is expected here.

The seed event is supported by `curation/seed_scope.tsv:23892`, which records
`NCBITaxon:228419` as added on `2026-09-12` with reason `attested rule:
Acholeplasma pleciae, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated compact record.
The exact and bounded scans account for the expected NCBI, LPSN, GOLD, Madin,
StrainInfo, and type-material inputs, and found no NCBI merge, GTDB, BacDive,
BactoTraits, MediaDive, AllTheBacteria, normalized assembly, normalized genome,
or normalized related-record row that would require an enriched YAML section.

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
