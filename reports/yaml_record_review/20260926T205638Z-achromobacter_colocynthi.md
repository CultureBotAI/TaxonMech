# YAML Record Review: Achromobacter colocynthi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_colocynthi.yaml
- Started UTC: 2026-09-26T20:56:38Z
- Finished UTC: 2026-09-26T20:56:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_colocynthi.yaml` |
| Identifier | `NCBITaxon:3341854` |
| Label | `Achromobacter colocynthi` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI input. Its path is pinned by
`data/taxa/PATHS.tsv:442391`, and all reviewed fields are owned by the seeder,
`curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than this YAML
file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_colocynthi.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_colocynthi.yaml data/taxa/bacteria/achromobacter_cycloclastes.yaml data/taxa/bacteria/achromobacter_deleyi.yaml data/taxa/bacteria/achromobacter_denitrificans.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 67 YAML lines, 9 lineage entries, 1 source attestation, 5 NCBI related synonyms, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, NCBI, NCBI merge, NCBI type-material, `data/taxa/PATHS.tsv`, and generated YAML rows; found no extra `data/atb` or generated target YAML hits; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:616108`, 9 checked lineage entries with no missing rows or mismatches, 3 NCBI merge rows, 10 NCBI type-material rows, 0 GOLD aggregate rows, 0 native GOLD rows, and no GTDB, LPSN, BacDive, MediaDive, MADIN, BactoTraits, normalized strain, StrainInfo assembly, StrainInfo related, direct StrainInfo, or StrainInfo deposit rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:3341854` resolves in the committed NCBI inventory to label
`Achromobacter colocynthi`, rank `SPECIES`, parent `NCBITaxon:222`, genetic
code `11`, source set `ncbitaxon`, and taxonomy snapshot `2026-09-13`. The
generated record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. Three
NCBI merge rows retire `NCBITaxon:3341858`, `NCBITaxon:3341865`, and
`NCBITaxon:3341869` into this identifier, and the bounded scan found no
retained raw `ncbitaxon_taxa.tsv` row for those old IDs.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and the 5 related
synonyms headed by `"Achromobacter colocynthi" Ait Si Mhand et al. 2026`.
NCBI also contributes 10 type-material aliases for this taxon.

The seed event is supported by `curation/seed_scope.tsv:601502`, which records
`NCBITaxon:3341854` as added on `2026-09-13` with reason `attested rule:
Achromobacter colocynthi, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, merge, type-material, seed,
path, and generated YAML inputs, and found no omitted GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, culture-collection,
normalized assembly, normalized genome, or normalized related-record row for
this taxon.

The NCBI type-material aliases do not have a matching LPSN, BacDive, or
normalized culture-collection strain row, so they do not produce a standalone
strain section in this generated NCBI-only record.

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
