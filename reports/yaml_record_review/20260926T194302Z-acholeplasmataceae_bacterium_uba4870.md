# YAML Record Review: Acholeplasmataceae bacterium UBA4870

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasmataceae_bacterium_uba4870.yaml
- Started UTC: 2026-09-26T19:43:02Z
- Finished UTC: 2026-09-26T19:43:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasmataceae_bacterium_uba4870.yaml` |
| Identifier | `NCBITaxon:1951311` |
| Label | `Acholeplasmataceae bacterium UBA4870` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1898208` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:310484`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasmataceae_bacterium_uba4870.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasmataceae_bacterium_uba2284.yaml data/taxa/bacteria/acholeplasmataceae_bacterium_uba4853.yaml data/taxa/bacteria/acholeplasmataceae_bacterium_uba4870.yaml data/taxa/bacteria/acholeplasmataceae_bacterium_uba4904.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected NCBI-only generated shape: 51 YAML lines, 9 lineage entries, 1 `NCBITAXON` source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:502099`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, and 0 LPSN, GTDB, BacDive, StrainInfo, GOLD, Madin, MediaDive, BactoTraits, type-material, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1951311` resolves in the committed NCBI inventory to label
`Acholeplasmataceae bacterium UBA4870`, rank `SPECIES`, parent
`NCBITaxon:1898208`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1898208` unclassified
Acholeplasmataceae. There are no retained old identifiers for this target in
the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1951311`, source label `Acholeplasmataceae bacterium UBA4870`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The compact YAML has no nomenclature, GTDB mapping, synonym, xref, strain,
assembly, genome, or related-record sections, matching the NCBI-only source
attestation and the absence of exact rows in the checked auxiliary source
tables.

The seed event is supported by `curation/seed_scope.tsv:551321`, which records
`NCBITaxon:1951311` as added on `2026-09-13` with reason `attested rule:
Acholeplasmataceae bacterium UBA4870, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBI-only record.
The exact and bounded scans account for the expected NCBI and generated YAML
inputs, and found no NCBI merge, LPSN, GTDB, BacDive, StrainInfo, GOLD, Madin,
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
