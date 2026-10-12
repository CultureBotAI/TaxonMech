# YAML Record Review: Achromobacter seleniivolatilans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_seleniivolatilans.yaml
- Started UTC: 2026-09-26T21:21:20Z
- Finished UTC: 2026-09-26T21:21:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_seleniivolatilans.yaml` |
| Identifier | `NCBITaxon:3047478` |
| Label | `Achromobacter seleniivolatilans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, and GOLD inputs.
Its path is pinned by `data/taxa/PATHS.tsv:412109`, and all reviewed fields are
owned by the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs
rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_seleniivolatilans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_ruhlandii.yaml data/taxa/bacteria/achromobacter_seleniivolatilans.yaml data/taxa/bacteria/achromobacter_semiaridum.yaml data/taxa/bacteria/achromobacter_sp.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 105 YAML lines, 9 lineage entries, 4 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 2 NCBI related synonyms, 2 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, type-material, `data/taxa/PATHS.tsv`, and generated YAML rows; found no extra BacDive, MediaDive, MADIN, BactoTraits, StrainInfo, or normalized strain rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:589792`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 1 LPSN row, 1 GTDB closeMatch row, 1 GOLD aggregate row, 1 native GOLD organism/project/analysis, 10 NCBI type-material rows, and no BacDive, MediaDive, MADIN, BactoTraits, culture-collection, normalized strain, StrainInfo assembly, StrainInfo related, direct StrainInfo, StrainInfo deposit, or StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:3047478` resolves in the committed NCBI inventory to label
`Achromobacter seleniivolatilans`, rank `SPECIES`, parent `NCBITaxon:222`,
genetic code `11`, source set `ncbitaxon|gtdb|lpsn|gold`, and taxonomy
snapshot `2026-09-13`. The generated record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. The
bounded scan found no NCBI merge row and no retained old-id row that would
change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and 2 related
synonyms. LPSN row `lpsn:47818` supports the legitimate, validly published,
correct species name, authority `Zhang et al. 2024`, type-strain alias
`JCM-36009`, and sequence accession `INSDC:OR000211`.

The GTDB evidence is the single `GTDB:s__Achromobacter_seleniivolatilans`
closeMatch row with `genome_count: 1`. GOLD asserts 1 organism and the native
GOLD row links `Achromobacter seleniivolatilans R39` to organism `Go0703937`,
project `Gp0828933`, and its analysis row.

The seed event is supported by `curation/seed_scope.tsv:29342`, which records
`NCBITaxon:3047478` as added on `2026-09-12` with reason `attested rule:
Achromobacter seleniivolatilans, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, GOLD,
type-material, seed, path, and generated YAML inputs, and found no omitted
BacDive, MediaDive, MADIN, BactoTraits, StrainInfo, ATB, culture-collection,
normalized assembly, normalized genome, normalized related-record, NCBI merge,
or StrainInfo exclusion row for this taxon.

The NCBI type-material aliases and the LPSN type-strain designation do not have
a matching BacDive or normalized culture-collection strain row, so they do not
produce a standalone strain section in this generated record.

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
