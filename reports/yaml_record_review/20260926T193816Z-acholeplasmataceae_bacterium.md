# YAML Record Review: Acholeplasmataceae bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasmataceae_bacterium.yaml
- Started UTC: 2026-09-26T19:38:16Z
- Finished UTC: 2026-09-26T19:38:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasmataceae_bacterium.yaml` |
| Identifier | `NCBITaxon:1898209` |
| Label | `Acholeplasmataceae bacterium` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1898208` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, and GOLD inputs. Its
path is pinned by `data/taxa/PATHS.tsv:299535`, and all seeded fields are owned
by the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasmataceae_bacterium.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_sp_t6_6_76.yaml data/taxa/bacteria/acholeplasma_sp_t6_8_42.yaml data/taxa/bacteria/acholeplasma_sp_zj2005.yaml data/taxa/bacteria/acholeplasmataceae_bacterium.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 561 YAML lines, 9 lineage entries, 3 source attestations, 0 nomenclature entries, 71 GTDB `skos:broadMatch` mappings, 0 synonyms, 0 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `curation/legacy_page_paths.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:491774`, 9 checked lineage entries with no missing rows or mismatches, 71 GTDB broadMatch rows at `data/raw/gtdb_mappings.tsv:85672-85742`, 1 GOLD aggregate row, 1 native GOLD organism and 1 native GOLD project, 0 NCBI merge rows, and 0 LPSN, BacDive, StrainInfo, Madin, MediaDive, BactoTraits, type-material, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1898209` resolves in the committed NCBI inventory to label
`Acholeplasmataceae bacterium`, rank `SPECIES`, parent `NCBITaxon:1898208`,
genetic code `11`, source set `ncbitaxon|gtdb|gold`, and taxonomy snapshot
`2026-09-13`. The record carries those same identity fields and correctly lands
in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1898208` unclassified
Acholeplasmataceae. There are no retained old identifiers for this target in
the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1898209`, source label `Acholeplasmataceae bacterium`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB evidence is supported by 71 committed `skos:broadMatch` rows. The YAML
preserves all 71 broadMatch mappings, records `GTDB:s__UBA5409_sp002410615` as
the representative source attestation with `assertion_count: 25`, and notes
that 70 further GTDB species pool onto this taxon.

The GOLD evidence is supported by the aggregate
`data/raw/gold_organisms.tsv:17144` row with `organism_count: 1` and by the
native GOLD payload for organism `Go0389752` and project `Gp0251576`. There are
no matching native GOLD analysis rows.

The seed event is supported by `curation/seed_scope.tsv:61501`, which records
`NCBITaxon:1898209` as added on `2026-09-12` with reason `attested rule:
Acholeplasmataceae bacterium, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBI, GTDB, and
GOLD record. The exact and bounded scans account for the expected NCBI, GOLD,
GTDB, and generated YAML inputs, and found no NCBI merge, LPSN, BacDive,
StrainInfo, Madin, MediaDive, BactoTraits, type-material, normalized assembly,
normalized genome, or normalized related-record row that would require an
enriched YAML section.

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
