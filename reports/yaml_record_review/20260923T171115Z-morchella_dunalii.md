# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_dunalii.yaml`
- Taxon: `NCBITaxon:1582327` (`Morchella dunalii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1582327`, label `Morchella dunalii`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_dunalii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_dunalii.yaml ... morchella_eximia.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60528` contains the seeded identifier with reason `attested rule: Morchella dunalii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:408392` matches the YAML identity: parent `NCBITaxon:1051054`, rank `SPECIES`, no exact synonyms, and related synonyms `Morchella dunalii Boud., 1887` and `Morchella sp. Mel-25`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:408392` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12780`, where `NCBITaxon:1582327` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0535691` / `Morchella dunalii PhC 240`, linked to projects `Gp0484069` and `Gp0484084`; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found six epitype aliases at lines 44275-44280: `LIP 0900128`, `LIP-0900128`, `LIP0900128`, `LIP:0900128`, `LIP:PhC120 `, and `PhC120`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1582327`.
- `data/raw/ncbi_merged_ids.tsv:548` maps retired `NCBITaxon:1009836` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` row, so the retired ID is side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retired-ID provenance to this record.

## Additional Notes

- The six NCBI type-material rows are all raw aliases for the epitype material; they are not currently materialized into this YAML species record.
