# YAML Record Review: Acetobacteraceae bacterium B3987

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteraceae_bacterium_b3987.yaml
- Started UTC: 2026-09-26T13:21:39Z
- Finished UTC: 2026-09-26T13:21:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacteraceae_bacterium_b3987.yaml` |
| Identifier | `NCBITaxon:2817958` |
| Label | `Acetobacteraceae bacterium B3987` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:41293` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13 with one seeded GTDB close match. Its path is pinned by
`data/taxa/PATHS.tsv:379660`, and all seeded fields are owned by the seeder,
`curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than the YAML
file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium_b3987.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium_b3987.yaml data/taxa/bacteria/acetobacteraceae_bacterium_b3_1so2.yaml data/taxa/bacteria/acetobacteraceae_bacterium_b3_1tco2.yaml data/taxa/bacteria/acetobacteraceae_bacterium_b3_2co2.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected NCBI+GTDB seeded shape: 9 lineage entries, 1 `skos:closeMatch` GTDB mapping, 1 GTDB exact synonym, 1 GTDB xref, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, 0 nomenclature rows, 0 strains, 0 definitions, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found the NCBI identifier and label in `curation/seed_scope.tsv` and `data/raw/ncbitaxon_taxa.tsv`; found `GTDB:s__Bombella_sp026537415` in `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv`; found no prior history or ignored report row for this target across the scanned local sources. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:559477`, the matching GTDB close-match row at `data/raw/gtdb_mappings.tsv:221442`, 9 checked lineage entries with no missing rows or mismatches, and no rows in LPSN, BacDive, GOLD, StrainInfo, strain, NCBI merged, MediaDive, Madin, or BactoTraits inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2817958` resolves in the committed NCBI inventory to label
`Acetobacteraceae bacterium B3987`, rank `SPECIES`, parent `NCBITaxon:41293`,
genetic code `11`, attestation sources `ncbitaxon|gtdb`, and taxonomy snapshot
`2026-09-13`. The record carries those same identity fields and correctly lands
in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:41293` unclassified
Acetobacteraceae. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:2817958`, source label `Acetobacteraceae bacterium B3987`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB rows support the close match, synonym, xref, and GTDB source
attestation. `data/raw/gtdb_mappings.tsv:221442` maps
`GTDB:s__Bombella_sp026537415` to `NCBITaxon:2817958` via `skos:closeMatch`
with `genome_count: 2`, and `data/raw/gtdb_species.tsv:19138` carries the same
species ID, label, parent `GTDB:g__Bombella`, and genome count. The exact scan
also saw `data/raw/gtdb_mappings.tsv:49555`, but that is the same GTDB species'
`skos:broadMatch` to `NCBITaxon:169975`, not a mapping to this target record.

The seed event is supported by `curation/seed_scope.tsv:104818`, which records
`NCBITaxon:2817958` as added on `2026-09-13` with reason
`attested rule: Acetobacteraceae bacterium B3987, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for the generated NCBI+GTDB record.
The bounded scan found the expected GTDB close match and no rows for this target
in the LPSN, BacDive, GOLD, StrainInfo, strain, NCBI merged, MediaDive, Madin,
or BactoTraits inputs, so the empty nomenclature, strain, definition, and causal
graph sections are consistent with the inspected local sources.

The exact ignored-aware source scan found no prior history or ignored review
report mentioning this target before this report was written; ignored files
under `reports/` were included.

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
