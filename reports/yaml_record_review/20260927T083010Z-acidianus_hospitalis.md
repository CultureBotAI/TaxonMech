# YAML Record Review: Acidianus hospitalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_hospitalis.yaml
- Started UTC: 2026-09-27T08:30:10Z
- Finished UTC: 2026-09-27T08:30:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_hospitalis.yaml` |
| Identifier | `NCBITaxon:563177` |
| Label | `Acidianus hospitalis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:12914` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is generated from NCBI, GTDB, GOLD, and MADIN inputs; its path is
pinned by `data/taxa/PATHS.tsv:540961`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_hospitalis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_hospitalis.yaml data/taxa/archaea/acidianus_hospitalis_w1.yaml data/taxa/archaea/acidianus_infernus.yaml data/taxa/archaea/acidianus_manzaensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 81 YAML lines, 9 lineage entries, 4 source attestations, 1 GTDB `skos:closeMatch`, 1 NCBI related synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:563177` in the expected seed, NCBI, GTDB mapping, path, generated target YAML, and strain-child YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:132206`, 9 checked lineage entries with no missing rows or mismatches, 1 GTDB closeMatch row, 1 GOLD aggregate row, 1 MADIN row with 2 assertions, 0 NCBI merge rows, 0 NCBI type-material rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, no direct StrainInfo or StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:563177` resolves to label `Acidianus hospitalis`, rank `SPECIES`,
parent `NCBITaxon:12914`, genetic code `11`, source set
`ncbitaxon|gtdb|gold|madin_etal`, and taxonomy snapshot `2026-09-13`. The
generated record carries those same fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:12914` Acidianus. The bounded
scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the related synonym `"Acidianus hospitalis" Bettstetter
et al. 2003`. The GTDB row `data/raw/gtdb_mappings.tsv:296668` supports
`GTDB:s__Acidianus_hospitalis` as a `skos:closeMatch` with genome count 7, and
the generated record retains it as both taxonomy mapping and xref.

The GOLD aggregate row at `data/raw/gold_taxa.tsv:38889` contributes one
organism assertion, while the committed native GOLD snapshot has no exact
organism, project, or analysis row for `NCBITaxon:563177`. MADIN contributes 2
trait assertions through the row at `data/raw/madin_taxa.tsv:26972`.

The seed event is supported by `curation/seed_scope.tsv:24866`, which records
`NCBITaxon:563177` as added on `2026-09-12` with reason `attested rule:
Acidianus hospitalis, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. Exact and
bounded scans accounted for the expected NCBI, GTDB, GOLD aggregate, MADIN,
seed, path, and YAML inputs, and found no omitted NCBI merge, NCBI
type-material, LPSN, BacDive, MediaDive, BactoTraits, StrainInfo, normalized
strain, or StrainInfo exclusion row for this taxon.

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
The retained GOLD aggregate row has no exact native GOLD organism in the local
snapshot, so this report treats the GOLD attestation as aggregate evidence
only. If a future GOLD refresh restores an exact organism row, rerun the
bounded scan before deciding whether it should remain an attestation or become
normalized strain evidence.
