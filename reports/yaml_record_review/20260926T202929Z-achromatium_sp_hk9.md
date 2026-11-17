# YAML Record Review: Achromatium sp. HK9

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromatium_sp_hk9.yaml
- Started UTC: 2026-09-26T20:29:29Z
- Finished UTC: 2026-09-26T20:29:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromatium_sp_hk9.yaml` |
| Identifier | `NCBITaxon:94734` |
| Label | `Achromatium sp. HK9` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2634746` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI input. Its path is pinned
by `data/taxa/PATHS.tsv:619107`, and all reviewed fields are owned by the
seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than
this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromatium_sp_hk9.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromatium_sp_hk9.yaml data/taxa/bacteria/achromatium_sp_jd1.yaml data/taxa/bacteria/achromatium_sp_jd13.yaml data/taxa/bacteria/achromatium_sp_jd2.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 53 YAML lines, 10 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:15702`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, and 0 GTDB, GOLD, LPSN, BacDive, StrainInfo, Madin, MediaDive, BactoTraits, type-material, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:94734` resolves in the committed NCBI inventory to label
`Achromatium sp. HK9`, rank `SPECIES`, parent `NCBITaxon:2634746`, genetic code
`11`, source set `ncbitaxon`, and taxonomy snapshot `2026-09-13`. The
generated record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:2634746` unclassified
Achromatium. There are no retained old identifiers for this target in the NCBI
merge input.

## Evidence

The only source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:94734`, source label `Achromatium sp. HK9`, `assertion_count: 1`,
`assertion_unit: NAME`, and the 2026-09-13 snapshot note all match.

The seed event is supported by `curation/seed_scope.tsv:141800`, which records
`NCBITaxon:94734` as added on `2026-09-13` with reason `attested rule:
Achromatium sp. HK9, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBI-only record.
The exact and bounded scans account for the expected NCBI and generated YAML
inputs, and found no NCBI merge, GTDB, LPSN, GOLD, BacDive, StrainInfo, Madin,
MediaDive, BactoTraits, type-material, normalized assembly, normalized genome,
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
