# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_steppicola.yaml`
- Taxon: `NCBITaxon:743781` (`Morchella steppicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:743781`, label `Morchella steppicola`.
- It is grounded exactly under `NCBITaxon:1175439` (`Morchella sect. Morchella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Morchella`.

## Validation

- `just validate data/taxa/eukaryota/morchella_steppicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_steppicola.yaml ... morchella_vulgaris.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56586` contains the seeded identifier with reason `attested rule: Morchella steppicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:171379` matches the YAML identity: parent `NCBITaxon:1175439`, rank `SPECIES`, no exact synonyms, and related synonyms `Morchella sp. Mes-1` and `Morchella steppicola Zerova, 1941`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:171379` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42159`, where `NCBITaxon:743781` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0515921` / `Morchella steppicola PhC 289` and `Go0535695` / `Morchella steppicola PhC 149`, linked to projects `Gp0436668`, `Gp0436669`, `Gp0484073`, and `Gp0484098`; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found nine type-material rows at lines 261412-261420, covering five `TAAM 204905` culture-from-epitype aliases and four `CWU D0208` epitype aliases.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:743781`.
- `data/raw/ncbi_merged_ids.tsv:3531` maps retired `NCBITaxon:1105050` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` row, so the retired ID is side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The GOLD source is richer than most neighboring Morchella records here, with two native organism IDs and four exact native projects.
