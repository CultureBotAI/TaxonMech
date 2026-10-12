# YAML Record Review: Achromatium oxaliferum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromatium_oxaliferum.yaml
- Started UTC: 2026-09-26T20:18:31Z
- Finished UTC: 2026-09-26T20:18:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromatium_oxaliferum.yaml` |
| Identifier | `NCBITaxon:44938` |
| Label | `Achromatium oxaliferum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:44937` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, LPSN, and MADIN inputs. Its
path is pinned by `data/taxa/PATHS.tsv:507802`, and all reviewed fields are
owned by the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs
rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromatium_oxaliferum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasmatales_bacterium_feline_oral_taxon_303.yaml data/taxa/bacteria/acholeplasmatales_bacterium_tener_01.yaml data/taxa/bacteria/achromatium_minus.yaml data/taxa/bacteria/achromatium_oxaliferum.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 100 YAML lines, 9 lineage entries, 3 source attestations, 1 LPSN nomenclature entry, 0 taxonomy mappings, 3 NCBI exact synonyms, 4 NCBI related synonyms, 1 LPSN xref, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `curation/legacy_page_paths.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:5464`, 9 checked lineage entries with no missing rows or mismatches, 1 LPSN row at `data/raw/lpsn_names.tsv:21379`, 1 MADIN row at `data/raw/madin_taxa.tsv:24453`, 0 NCBI merge rows, and 0 GTDB, GOLD, BacDive, StrainInfo, MediaDive, BactoTraits, type-material, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:44938` resolves in the committed NCBI inventory to label
`Achromatium oxaliferum`, rank `SPECIES`, parent `NCBITaxon:44937`, genetic
code `11`, source set `ncbitaxon|lpsn|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:44937` genus `Achromatium`.
There are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:44938`, source label `Achromatium oxaliferum`, `assertion_count: 1`,
`assertion_unit: NAME`, and the 2026-09-13 snapshot note all match. The YAML
also preserves 3 exact synonyms and 4 related synonyms from the NCBI row.

The LPSN evidence is supported by `data/raw/lpsn_names.tsv:21379`: LPSN ID
`lpsn:783263`, name `Achromatium oxaliferum`, rank `SPECIES`, authority
`Schewiakoff 1893 (Approved Lists 1980)`, validly-published and legitimate
flags, correct-name status, the LPSN URL, and DOI
`10.1099/00207713-30-1-225`. The YAML preserves that nomenclature row, the LPSN
source attestation, and the `lpsn:783263` xref.

The MADIN evidence is supported by `data/raw/madin_taxa.tsv:24453`, whose 2
trait assertions are preserved as the `MADIN` source attestation with source
ID `NCBITaxon:44938`, source label `Achromatium oxaliferum`, and
`assertion_unit: TRAIT_ASSERTION`.

The seed event is supported by `curation/seed_scope.tsv:31479`, which records
`NCBITaxon:44938` as added on `2026-09-12` with reason `attested rule:
Achromatium oxaliferum, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBI, LPSN, and
MADIN record. The exact and bounded scans account for the expected NCBI, LPSN,
MADIN, and generated YAML inputs, and found no NCBI merge, GTDB, GOLD,
BacDive, StrainInfo, MediaDive, BactoTraits, type-material, normalized
assembly, normalized genome, or normalized related-record row that would
require an enriched YAML section.

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
