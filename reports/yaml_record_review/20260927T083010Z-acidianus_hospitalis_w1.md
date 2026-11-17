# YAML Record Review: Acidianus hospitalis W1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_hospitalis_w1.yaml
- Started UTC: 2026-09-27T08:30:10Z
- Finished UTC: 2026-09-27T08:30:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_hospitalis_w1.yaml` |
| Identifier | `NCBITaxon:933801` |
| Label | `Acidianus hospitalis W1` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:563177` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is generated from NCBI, GTDB, and MADIN inputs, with native GOLD side
evidence only; its path is pinned by `data/taxa/PATHS.tsv:612764`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_hospitalis_w1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_hospitalis.yaml data/taxa/archaea/acidianus_hospitalis_w1.yaml data/taxa/archaea/acidianus_infernus.yaml data/taxa/archaea/acidianus_manzaensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 84 YAML lines, 10 lineage entries, 3 source attestations, 1 GTDB `skos:closeMatch`, 3 exact synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:933801` in the expected seed, NCBI, GTDB mapping, path, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:197221`, 10 checked lineage entries with no missing rows or mismatches, 1 GTDB closeMatch row, 1 MADIN row with 4 assertions, 1 exact native GOLD organism, 1 native GOLD project, 1 native GOLD analysis, 0 GOLD aggregate rows, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no LPSN, MediaDive, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, no direct StrainInfo or StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:933801` resolves to label `Acidianus hospitalis W1`, rank `STRAIN`,
parent `NCBITaxon:563177`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`. The generated
record carries those same fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through parent species `NCBITaxon:563177`
Acidianus hospitalis. The bounded scan found no NCBI merge row and no retained
old-id row.

## Evidence

The NCBI row supports two exact synonyms, `Acidianus hospitalis str. W1` and
`Acidianus hospitalis strain W1`. The GTDB row
`data/raw/gtdb_mappings.tsv:320834` maps the strain record to
`GTDB:s__Acidianus_hospitalis` as `skos:closeMatch` with genome count 7.

The exact native GOLD rows for organism `Go0009250`, project `Gp0009250`, and
analysis `Acidianus hospitalis W1` are present side evidence only: no retained
GOLD aggregate row and no normalized strain row are filed under this target.
MADIN contributes 4 trait assertions through `data/raw/madin_taxa.tsv:33029`.

The seed event is supported by `curation/seed_scope.tsv:35257`, which records
`NCBITaxon:933801` as added on `2026-09-12` with reason `attested rule:
Acidianus hospitalis W1, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. Exact and
bounded scans accounted for NCBI, GTDB, native GOLD, MADIN, seed, path, and
YAML inputs, and found no omitted NCBI merge, NCBI type-material, LPSN, GOLD
aggregate, BacDive, MediaDive, BactoTraits, StrainInfo, normalized strain, or
StrainInfo exclusion row for this taxon.

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

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
Its native GOLD organism, project, and analysis rows are evidence leads only:
the generated record has no GOLD source attestation because no retained GOLD
aggregate row is filed under `NCBITaxon:933801`.
No generated strain row is present.
