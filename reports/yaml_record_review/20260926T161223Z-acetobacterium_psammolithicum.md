# YAML Record Review: Acetobacterium psammolithicum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_psammolithicum.yaml
- Started UTC: 2026-09-26T16:12:23Z
- Finished UTC: 2026-09-26T16:12:23Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_psammolithicum.yaml` |
| Identifier | `NCBITaxon:93718` |
| Label | `Acetobacterium psammolithicum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33951` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:614473`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_psammolithicum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_psammolithicum.yaml data/taxa/bacteria/acetobacterium_sp.yaml data/taxa/bacteria/acetobacterium_sp_ac1.yaml data/taxa/bacteria/acetobacterium_sp_ag.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact NCBITaxon-only shape: 58 YAML lines, 9 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 1 exact synonym, 1 related synonym, 0 taxonomy mappings, 0 strains, 0 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier and exact label in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/ncbi_type_material.tsv`, and `data/taxa/PATHS.tsv` rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. A line-anchored rerun disambiguated fixed-string prefix hits such as `NCBITaxon:937180`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:15470`, 3 matching NCBI type-material rows at `data/raw/ncbi_type_material.tsv:274362` through `data/raw/ncbi_type_material.tsv:274364`, 9 checked lineage entries with no missing rows or mismatches, and no rows in LPSN, GTDB, BacDive, StrainInfo, strain, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:93718` resolves in the committed NCBI inventory to label
`Acetobacterium psammolithicum`, rank `SPECIES`, parent `NCBITaxon:33951`,
genetic code `11`, one exact synonym, one related synonym, and taxonomy
snapshot `2026-09-13`. The record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through the `Acetobacterium` genus. There are no
retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:93718`, source label `Acetobacterium psammolithicum`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The two YAML synonyms are exactly the NCBI normalized synonyms at
`data/raw/ncbitaxon_taxa.tsv:15470`: exact synonym `'Acetobacterium
psammolithicum'` and related synonym `"Acetobacterium psammolithicum" Krumholz
et al.`

NCBI also records three type-material designations for the same target at
`data/raw/ncbi_type_material.tsv:274362` through
`data/raw/ncbi_type_material.tsv:274364`: `SMCC/W 751`, `personal::CN-E`, and
`strain CN-E`.

The seed event is supported by `curation/seed_scope.tsv:141605`, which records
`NCBITaxon:93718` as added on `2026-09-13` with reason
`attested rule: Acetobacterium psammolithicum, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for the generated NCBITaxon-only
record. The bounded scan found the target only in NCBI and seed rows and found
no LPSN, GTDB, BacDive, StrainInfo, normalized strain, GOLD, MediaDive, Madin,
or BactoTraits row that would support additional nomenclature, mapping, strain,
xref, definition, genome, or causal graph sections.

The NCBI type-material designations are present in `ncbi_type_material.tsv`,
but no normalized BacDive, StrainInfo, or LPSN strain input turns them into
generated `strains` entries. The YAML's `strain_count: 0` is therefore
consistent with the inspected processed inputs.

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
