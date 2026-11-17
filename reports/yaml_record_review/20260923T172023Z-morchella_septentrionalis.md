# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_septentrionalis.yaml`
- Taxon: `NCBITaxon:1174675` (`Morchella septentrionalis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1174675`, label `Morchella septentrionalis`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_septentrionalis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_septentrionalis.yaml ... morchella_sp.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58195` contains the seeded identifier with reason `attested rule: Morchella septentrionalis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:260862` matches the YAML identity: parent `NCBITaxon:1051054`, rank `SPECIES`, no exact synonyms, and related synonyms `Morchella septentrionalis M. Kuo, J.D. Moore & Zordani, 2012` and `Morchella sp. Mel-24`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:260862` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3864`, where `NCBITaxon:1174675` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0568261` / `Morchella septentrionalis NRRL 54509`, linked to projects `Gp0538663` and `Gp0543298`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:11426-11427` has two holotype aliases, `F 05110405` and `F:05110405`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1174675`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:746147` and `NCBITaxon:746167` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The bounded scan fully covered the GOLD, type-material, and NCBI merge evidence for this target.
