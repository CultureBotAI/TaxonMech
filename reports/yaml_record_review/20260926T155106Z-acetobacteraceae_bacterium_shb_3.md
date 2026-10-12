# YAML Record Review: Acetobacteraceae bacterium SHB-3

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteraceae_bacterium_shb_3.yaml
- Started UTC: 2026-09-26T15:51:06Z
- Finished UTC: 2026-09-26T15:51:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacteraceae_bacterium_shb_3.yaml` |
| Identifier | `NCBITaxon:946048` |
| Label | `Acetobacteraceae bacterium SHB-3` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:41293` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:618425`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium_shb_3.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium_se1pw_3067.yaml data/taxa/bacteria/acetobacteraceae_bacterium_se2pw_3359.yaml data/taxa/bacteria/acetobacteraceae_bacterium_shb_3.yaml data/taxa/bacteria/acetobacteraceae_bacterium_so1pw_988.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact NCBI-only shape: 9 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 0 synonyms, 0 nomenclature rows, 0 GTDB mappings, 0 xrefs, 0 strains, 0 definitions, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier and exact label only in `curation/seed_scope.tsv` and `data/raw/ncbitaxon_taxa.tsv` across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:202565`, 9 checked lineage entries with no missing rows or mismatches, and no rows in LPSN, GTDB, BacDive, GOLD, StrainInfo, strain, NCBI merged, MediaDive, Madin, or BactoTraits inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:946048` resolves in the committed NCBI inventory to label
`Acetobacteraceae bacterium SHB-3`, rank `SPECIES`, parent `NCBITaxon:41293`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries those
same identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:41293` unclassified
Acetobacteraceae. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The sole `source_attestations` entry is supported by the raw NCBI row: source
`NCBITAXON`, source ID `NCBITaxon:946048`, source label
`Acetobacteraceae bacterium SHB-3`, `assertion_count: 1`,
`assertion_unit: NAME`, and the 2026-09-13 snapshot note all match.

The seed event is supported by `curation/seed_scope.tsv:304662`, which records
`NCBITaxon:946048` as added on `2026-09-13` with reason
`attested rule: Acetobacteraceae bacterium SHB-3, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for the generated NCBI-only record.
The bounded scan found no rows for this target in the LPSN, GTDB, BacDive,
GOLD, StrainInfo, strain, NCBI merged, MediaDive, Madin, or BactoTraits inputs,
so the empty synonym, nomenclature, taxonomy mapping, xref, strain, definition,
and causal graph sections are consistent with the inspected local sources.

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
