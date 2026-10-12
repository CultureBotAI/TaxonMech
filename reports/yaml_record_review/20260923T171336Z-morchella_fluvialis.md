# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_fluvialis.yaml`
- Taxon: `NCBITaxon:1611433` (`Morchella fluvialis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1611433`, label `Morchella fluvialis`.
- It is grounded exactly under `NCBITaxon:1175439` (`Morchella sect. Morchella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Morchella`.

## Validation

- `just validate data/taxa/eukaryota/morchella_fluvialis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_fluvialis.yaml ... morchella_kakiicolor.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60571` contains the seeded identifier with reason `attested rule: Morchella fluvialis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:416280` matches the YAML identity: parent `NCBITaxon:1175439`, rank `SPECIES`, no exact synonyms, and related synonyms `Morchella fluvialis Clowez, P. Alvarado, M. Becerra, Bilbao & P.-A. Moreau, 2014` and `Morchella sp. Mes-18`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:416280` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:13066`, where `NCBITaxon:1611433` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0515924` / `Morchella fluvialis PhC 265`, linked to projects `Gp0436674` and `Gp0436675`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:46657-46659` has holotype aliases `LIP 0900033` and `LIP:0900033`, plus `PhC165` as `type material`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1611433`.
- `data/raw/ncbi_merged_ids.tsv:3532` maps retired `NCBITaxon:1105051` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` row, so the retired ID is side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The type-material rows are raw NCBI aliases and are not currently materialized into this YAML species record.
