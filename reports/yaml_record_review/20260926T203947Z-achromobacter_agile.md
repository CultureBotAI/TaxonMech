# YAML Record Review: Achromobacter agile

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_agile.yaml
- Started UTC: 2026-09-26T20:39:47Z
- Finished UTC: 2026-09-26T20:39:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_agile.yaml` |
| Identifier | `NCBITaxon:1783500` |
| Label | `Achromobacter agile` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI input. Its path is pinned
by `data/taxa/PATHS.tsv:271441`, and all reviewed fields are owned by the
seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than
this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_agile.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromatium_sp_wms2.yaml data/taxa/bacteria/achromatium_sp_wms3.yaml data/taxa/bacteria/achromobacter_aegrifaciens.yaml data/taxa/bacteria/achromobacter_agile.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 57 YAML lines, 9 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 2 NCBI related synonyms, 0 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbi_merged_ids.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no ATB row and no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:464878`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row for `NCBITaxon:1683494`, 1 native StrainInfo deposit hit for `NCIM 2530`, 0 retained old NCBI rows, and 0 GTDB, GOLD, LPSN, BacDive, Madin, MediaDive, BactoTraits, type-material, ATB, normalized assembly, normalized genome, normalized StrainInfo, or normalized related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1783500` resolves in the committed NCBI inventory to label
`Achromobacter agile`, rank `SPECIES`, parent `NCBITaxon:222`, genetic code
`11`, source set `ncbitaxon`, and taxonomy snapshot `2026-09-13`. The
generated record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1683494` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The only source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1783500`, source label `Achromobacter agile`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The two related synonyms in the YAML,
`"Achromobacter agile" (Jensen) Bergey et al. 1923` and
`Achromobacter sp. NCIM 2530`, are exactly the related-synonym values from the
same raw NCBI row.

The seed event is supported by `curation/seed_scope.tsv:526566`, which records
`NCBITaxon:1783500` as added on `2026-09-13` with reason `attested rule:
Achromobacter agile, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBI-only record.
The exact and bounded scans account for the expected NCBI and generated YAML
inputs, and found no ATB, GTDB, LPSN, GOLD, BacDive, Madin, MediaDive,
BactoTraits, type-material, normalized assembly, normalized genome,
normalized StrainInfo, or normalized related-record row that would require an
enriched YAML section.

The bounded scan found one native StrainInfo deposit for designation
`NCIM 2530`, but no normalized BacDive strain, StrainInfo assembly, or
StrainInfo related-record row for this NCBI target; the native StrainInfo hit
therefore does not seed a YAML strain section in this generated record.

The NCBI merge row is represented by the current target identifier rather than
as a YAML xref, and the bounded scan found no retained raw NCBI row for the old
identifier.

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
