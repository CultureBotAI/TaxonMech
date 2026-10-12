# YAML Record Review: Acholeplasmatales bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasmatales_bacterium.yaml
- Started UTC: 2026-09-26T20:11:02Z
- Finished UTC: 2026-09-26T20:11:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasmatales_bacterium.yaml` |
| Identifier | `NCBITaxon:2053494` |
| Label | `Acholeplasmatales bacterium` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1151603` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI and GTDB inputs. Its path is
pinned by `data/taxa/PATHS.tsv:323648`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasmatales_bacterium.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasmataceae_bacterium_uba7643.yaml data/taxa/bacteria/acholeplasmatales_bacterium.yaml data/taxa/bacteria/acholeplasmatales_bacterium_canine_oral_taxon_172.yaml data/taxa/bacteria/acholeplasmatales_bacterium_canine_oral_taxon_256.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 329 YAML lines, 8 lineage entries, 2 source attestations, 0 nomenclature entries, 39 GTDB `skos:broadMatch` mappings, 0 synonyms, 0 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, 39 `data/raw/gtdb_mappings.tsv` rows, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:514108`, 8 checked lineage entries with no missing rows or mismatches, 39 GTDB broadMatch rows at `data/raw/gtdb_mappings.tsv:158932-158970`, 0 NCBI merge rows, and 0 GOLD, LPSN, BacDive, StrainInfo, Madin, MediaDive, BactoTraits, type-material, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2053494` resolves in the committed NCBI inventory to label
`Acholeplasmatales bacterium`, rank `SPECIES`, parent `NCBITaxon:1151603`,
genetic code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 8 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1151603` unclassified
Acholeplasmatales. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:2053494`, source label `Acholeplasmatales bacterium`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB evidence is supported by 39 committed `skos:broadMatch` rows. The YAML
preserves all 39 broadMatch mappings, records
`GTDB:s__Pelethenecus_sp910579215` as the representative source attestation
with `assertion_count: 320`, and notes that 38 further GTDB species pool onto
this NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:91352`, which records
`NCBITaxon:2053494` as added on `2026-09-13` with reason `attested rule:
Acholeplasmatales bacterium, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBI and GTDB
record. The exact and bounded scans account for the expected NCBI, GTDB, and
generated YAML inputs, and found no NCBI merge, LPSN, GOLD, BacDive,
StrainInfo, Madin, MediaDive, BactoTraits, type-material, normalized assembly,
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
