# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_peruviana.yaml`
- Taxon: `NCBITaxon:2382058` (`Morchella peruviana`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2382058`, label `Morchella peruviana`.
- It is grounded exactly under `NCBITaxon:1175439` (`Morchella sect. Morchella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Morchella`.

## Validation

- `just validate data/taxa/eukaryota/morchella_peruviana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_norvegiensis.yaml ... morchella_prava.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62568` contains the seeded identifier with reason `attested rule: Morchella peruviana, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:525267` matches the YAML identity: parent `NCBITaxon:1175439`, rank `SPECIES`, no exact synonyms, and related synonyms `Morchella peruviana Holgado, Aguilar, Quispe & T.J. Baroni, 2018` and `Morchella sp. TJB-2018d`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:525267` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:21950`, where `NCBITaxon:2382058` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0513061` / `Morchella peruviana NRRL 66754`, linked to projects `Gp0405456` and `Gp0405471`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:93949-93951` has two `culture from holotype` aliases, `NRRL 66754` and `NRRL:66754`, plus holotype alias `NY:02861412`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:2382058`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:2382058`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The native GOLD organism uses the `NRRL 66754` culture-from-holotype alias as its strain.
