# YAML Record Review: Acholeplasma sp. OttesenSCG-928-E16

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_sp_ottesenscg_928_e16.yaml
- Started UTC: 2026-09-26T19:31:44Z
- Finished UTC: 2026-09-26T19:31:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_sp_ottesenscg_928_e16.yaml` |
| Identifier | `NCBITaxon:2885269` |
| Label | `Acholeplasma sp. OttesenSCG-928-E16` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2644011` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:388604`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_sp_ottesenscg_928_e16.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_sp_jgi_sa12_e04_024.yaml data/taxa/bacteria/acholeplasma_sp_kda_feline.yaml data/taxa/bacteria/acholeplasma_sp_ord1043.yaml data/taxa/bacteria/acholeplasma_sp_ottesenscg_928_e16.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact generated shape: 73 YAML lines, 10 lineage entries, 2 source attestations, 0 nomenclature entries, 1 GTDB `skos:closeMatch` mapping, 1 GTDB exact synonym, 1 xref, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:567872`, 10 checked lineage entries with no missing rows or mismatches, 1 GTDB mapping row, 0 NCBI merge rows, and 0 LPSN, BacDive, StrainInfo, GOLD, Madin, MediaDive, BactoTraits, type-material, AllTheBacteria, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2885269` resolves in the committed NCBI inventory to label
`Acholeplasma sp. OttesenSCG-928-E16`, rank `SPECIES`, parent
`NCBITaxon:2644011`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2644011` unclassified
Acholeplasma. There are no retained old identifiers for this target in the NCBI
merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:2885269`, source label `Acholeplasma sp. OttesenSCG-928-E16`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB mapping to `GTDB:s__JAJDIT01_sp030266845` is the committed
`skos:closeMatch` row at `data/raw/gtdb_mappings.tsv:229066` with
`genome_count: 1`. The GTDB exact synonym, GTDB xref, and source attestation
all use the same species identifier.

The seed event is supported by `curation/seed_scope.tsv:107885`, which records
`NCBITaxon:2885269` as added on `2026-09-13` with reason `attested rule:
Acholeplasma sp. OttesenSCG-928-E16, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated compact record.
The exact and bounded scans account for the expected NCBI, GTDB, and generated
YAML inputs, and found no NCBI merge, LPSN, BacDive, StrainInfo, GOLD, Madin,
MediaDive, BactoTraits, type-material, AllTheBacteria, normalized assembly,
normalized genome, or normalized related-record row that would require an
enriched YAML section.

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
