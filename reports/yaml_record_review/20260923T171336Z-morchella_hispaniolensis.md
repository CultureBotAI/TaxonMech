# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_hispaniolensis.yaml`
- Taxon: `NCBITaxon:2382056` (`Morchella hispaniolensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2382056`, label `Morchella hispaniolensis`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_hispaniolensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_fluvialis.yaml ... morchella_kakiicolor.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62567` contains the seeded identifier with reason `attested rule: Morchella hispaniolensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:525266` matches the YAML identity: parent `NCBITaxon:1051054`, rank `SPECIES`, no exact synonyms, and related synonyms `Morchella hispaniolensis S.A. Cantrell, Lodge, T.J. Baroni & O'Donnell, 2018`, `Morchella sp. Mel-18`, and `Morchella sp. TJB-2018b`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:525266` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:21949`, where `NCBITaxon:2382056` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0513059` / `Morchella hispaniolensis NRRL 26637`, linked to projects `Gp0405454` and `Gp0405469`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:93944-93948` has four `culture from holotype` aliases for `NRRL 26636` and `NRRL 26637`, plus holotype alias `NY:02861410`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:2382056`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:746140` and `NCBITaxon:746160` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The native GOLD organism uses one of the culture-from-holotype aliases, `NRRL 26637`, as its strain.
