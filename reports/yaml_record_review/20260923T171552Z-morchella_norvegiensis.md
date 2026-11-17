# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_norvegiensis.yaml`
- Taxon: `NCBITaxon:1582341` (`Morchella norvegiensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1582341`, label `Morchella norvegiensis`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_norvegiensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_norvegiensis.yaml ... morchella_prava.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60530` contains the seeded identifier with reason `attested rule: Morchella norvegiensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:408394` matches the YAML parent, rank, exact synonym `Morchella eohespera`, and related synonyms `Morchella eohespera Beug, M.W., Voitk, A., O'Donnell, K., 2016`, `Morchella norvegiensis Jacquet., 1985`, `Morchella sp. KOD-2015b`, and `Morchella sp. Mel-19`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:408394` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12782`, where `NCBITaxon:1582341` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0513060` / `Morchella norvegiensis NRRL 20850`, linked to projects `Gp0405455` and `Gp0405470`; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found 16 rows at lines 44289-44304, covering `Morchella eohespera` culture-from-holotype and holotype aliases plus `Morchella norvegiensis` epitype and holotype aliases.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1582341`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:1729728`, `NCBITaxon:746141`, and `NCBITaxon:746161` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The type-material evidence spans both the current label and its exact synonym `Morchella eohespera`; those raw rows are not currently materialized into the YAML species record.
