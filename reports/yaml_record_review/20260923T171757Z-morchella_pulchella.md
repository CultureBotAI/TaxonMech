# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_pulchella.yaml`
- Taxon: `NCBITaxon:1579549` (`Morchella pulchella`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1579549`, label `Morchella pulchella`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_pulchella.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_pulchella.yaml ... morchella_semilibera.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60509` contains the seeded identifier with reason `attested rule: Morchella pulchella, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:407150` matches the YAML identity: parent `NCBITaxon:1051054`, rank `SPECIES`, no exact synonyms, and related synonyms `Morchella pulchella Clowez & F. Petit, 2012` and `Morchella sp. Mel-31`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:407150` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12739`, where `NCBITaxon:1579549` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0513062` / `Morchella pulchella NRRL 53822`, linked to projects `Gp0405457` and `Gp0405472`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:44024-44027` has four holotype aliases: `LIP 0900011`, `LIP:0900011`, `LIP:PhC56`, and `PhC56`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1579549`.
- `data/raw/ncbi_merged_ids.tsv:544` maps retired `NCBITaxon:1009832` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` row, so the retired ID is side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The bounded scan fully covered the NCBI type-material evidence for this target.
