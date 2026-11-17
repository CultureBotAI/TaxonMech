# YAML Record Review: Achromobacter piechaudii ATCC 43553

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_piechaudii_atcc_43553.yaml
- Started UTC: 2026-09-26T21:17:01Z
- Finished UTC: 2026-09-26T21:17:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_piechaudii_atcc_43553.yaml` |
| Identifier | `NCBITaxon:742159` |
| Label | `Achromobacter piechaudii ATCC 43553` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:72556` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded strain record from NCBI, GTDB, and MADIN
inputs. Its path is pinned by `data/taxa/PATHS.tsv:582334`, and all reviewed
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_piechaudii_atcc_43553.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_piechaudii_atcc_43553.yaml data/taxa/bacteria/achromobacter_piechaudii_hle.yaml data/taxa/bacteria/achromobacter_piechaudii_nbrc_102461.yaml data/taxa/bacteria/achromobacter_pulmonis.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 84 YAML lines, 10 lineage entries, 3 source attestations, 1 GTDB `skos:closeMatch` mapping, 3 exact synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, GTDB, MADIN, `data/taxa/PATHS.tsv`, and generated YAML rows; found no extra BacDive, LPSN, GOLD aggregate, StrainInfo, or normalized strain rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:170950`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 1 GTDB closeMatch row, 1 MADIN row, 0 GOLD aggregate rows, 1 native GOLD organism/project/analysis, and no LPSN, BacDive, MediaDive, BactoTraits, NCBI type-material, culture-collection, normalized strain, StrainInfo assembly, StrainInfo related, direct StrainInfo, or StrainInfo deposit rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:742159` resolves in the committed NCBI inventory to label
`Achromobacter piechaudii ATCC 43553`, rank `STRAIN`, parent
`NCBITaxon:72556`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`. The generated
record carries those same identity fields and correctly lands in the `bacteria`
path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through parent species `NCBITaxon:72556`
Achromobacter piechaudii. The bounded scan found no NCBI merge row and no
retained old-id row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and both NCBI exact
synonyms, `Achromobacter piechaudii str. ATCC 43553` and `Achromobacter
piechaudii strain ATCC 43553`.

The GTDB source attestation, xref, GTDB-derived exact synonym
`Achromobacter piechaudii`, and closeMatch mapping are supported by
`data/raw/gtdb_mappings.tsv:305475`, where
`GTDB:s__Achromobacter_piechaudii` links to this strain with
`genome_count: 9`. The MADIN row supports 5 trait assertions filed directly
under this NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:34144`, which records
`NCBITaxon:742159` as added on `2026-09-12` with reason `attested rule:
Achromobacter piechaudii ATCC 43553, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, MADIN, seed, path, and
generated YAML inputs, and found no omitted LPSN, BacDive, MediaDive,
BactoTraits, StrainInfo, ATB, culture-collection, type-material, normalized
assembly, normalized genome, normalized related-record, NCBI merge, or
StrainInfo exclusion row for this taxon.

A native GOLD row for `Go0004050` exactly matches `NCBITaxon:742159`, but
there is no `data/raw/gold_organisms.tsv` aggregate row for the target, so the
native row does not contribute a seeded GOLD attestation or YAML section in
this generated record.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

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
