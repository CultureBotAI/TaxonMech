# YAML Record Review: Acetobacteraceae bacterium ESL0709

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteraceae_bacterium_esl0709.yaml
- Started UTC: 2026-09-26T14:12:03Z
- Finished UTC: 2026-09-26T14:12:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacteraceae_bacterium_esl0709.yaml` |
| Identifier | `NCBITaxon:2983245` |
| Label | `Acetobacteraceae bacterium ESL0709` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:41293` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:403562`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium_esl0709.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium_esl0697.yaml data/taxa/bacteria/acetobacteraceae_bacterium_esl0709.yaml data/taxa/bacteria/acetobacteraceae_bacterium_esl0710.yaml data/taxa/bacteria/acetobacteraceae_bacterium_eva_to.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB-backed compact shape: 9 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, 1 `skos:closeMatch` GTDB mapping, 1 GTDB exact synonym, 1 GTDB xref, 0 strains, 0 definitions, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, or exact GTDB ID in the expected `curation/seed_scope.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/raw/ncbitaxon_taxa.tsv` rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:582086`, the matching GTDB mapping row at `data/raw/gtdb_mappings.tsv:245272`, 9 checked lineage entries with no missing rows or mismatches, and no rows in LPSN, BacDive, StrainInfo, strain, NCBI merged, MediaDive, Madin, or BactoTraits inputs. It also found a native GOLD organism/project/analysis chain that has no normalized `data/raw/gold_organisms.tsv` aggregate row. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2983245` resolves in the committed NCBI inventory to label
`Acetobacteraceae bacterium ESL0709`, rank `SPECIES`, parent
`NCBITaxon:41293`, genetic code `11`, and taxonomy snapshot `2026-09-13`. The
record carries those same identity fields and correctly lands in the `bacteria`
path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:41293` unclassified
Acetobacteraceae. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:2983245`, source label `Acetobacteraceae bacterium ESL0709`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB mapping is supported by `data/raw/gtdb_mappings.tsv:245272`, which
maps `GTDB:s__Aristophania_sp029433415` / `s__Aristophania_sp029433415` to
`NCBITaxon:2983245` with predicate `skos:closeMatch` and `genome_count` 2. The
same row supports the `GTDB` source attestation with assertion count 2 and unit
`GENOME`; `data/raw/gtdb_species.tsv:12770` carries the same GTDB species ID,
label, parent, and genome count.

The `Aristophania sp029433415` exact synonym is the normalized GTDB label from
the supported `skos:closeMatch` mapping, and the lone xref is the same GTDB
species CURIE.

The seed event is supported by `curation/seed_scope.tsv:114153`, which records
`NCBITaxon:2983245` as added on `2026-09-13` with reason
`attested rule: Acetobacteraceae bacterium ESL0709, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for the generated GTDB-backed record.
The bounded scan found no rows for this target in the LPSN, BacDive,
StrainInfo, strain, NCBI merged, MediaDive, Madin, or BactoTraits inputs, so
the empty nomenclature, strain, definition, and causal graph sections are
consistent with the inspected local sources.

The source-native GOLD workbook projection has `Go0680971`, `Gp0782999`, and an
analysis row for `Acetobacteraceae bacterium ESL0709`, but that chain has no
corresponding `data/raw/gold_organisms.tsv` aggregate row and no
culture-collection strain row to join against, so it does not currently seed a
`GOLD` taxon attestation, strain, genome record, or related record.

The exact ignored-aware source scan also found no prior history or ignored
review report mentioning this target before this report was written; ignored
files under `reports/` were included.

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
