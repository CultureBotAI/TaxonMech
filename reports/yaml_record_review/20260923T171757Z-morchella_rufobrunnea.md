# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_rufobrunnea.yaml`
- Taxon: `NCBITaxon:368404` (`Morchella rufobrunnea`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:368404`, label `Morchella rufobrunnea`.
- It is grounded exactly under `NCBITaxon:3367357` (`Morchella sect. Rufobrunnea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Rufobrunnea`.

## Validation

- `just validate data/taxa/eukaryota/morchella_rufobrunnea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_pulchella.yaml ... morchella_semilibera.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55376` contains the seeded identifier with reason `attested rule: Morchella rufobrunnea, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:77292` matches the YAML identity: parent `NCBITaxon:3367357`, rank `SPECIES`, no exact synonyms, and related synonyms `Morchella rufobrunnea Guzman & F. Tapia, 1998`, `blushing morel`, and `woodchip morel`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:77292` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33506`, where `NCBITaxon:368404` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0609063` / `Morchella rufobrunnea NRRL 28464`, linked to projects `Gp0620589` and `Gp0620590`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:195759-195761` has three holotype aliases, including `Guzman31565` and `XAL31565`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:368404`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:368404`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- This target sits in `Morchella sect. Rufobrunnea`; the lineage scan confirmed the section parent and all ancestors.
