# YAML Record Review

- Target: `data/taxa/eukaryota/mucochytrium_quahogii.yaml`
- Taxon: `NCBITaxon:96639` (`Mucochytrium quahogii`)
- Verdict: pass

## Target

- The record is the seeded stramenopile species `NCBITaxon:96639`, label `Mucochytrium quahogii`.
- It is grounded exactly under `NCBITaxon:3032531` (`Mucochytrium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Mucochytrium`.

## Validation

- `just validate data/taxa/eukaryota/mucochytrium_quahogii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucidula_mucida.yaml ... mucor_alternans.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53569` contains the seeded identifier with reason `attested rule: Mucochytrium quahogii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:16312` matches the YAML identity: parent `NCBITaxon:3032531`, rank `SPECIES`, no exact synonyms, and all three related synonyms represented in YAML.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:16312` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45120`, where `NCBITaxon:96639` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0039305` / `Mucochytrium quahogii parasite QPX`, linked to project `Gp0039305`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:275549-275552` has `ATCC 50749` culture-from-paratype aliases.

## Completeness

- Exact StrainInfo had no direct records or deposit rows for `NCBITaxon:96639`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:96639`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:96639`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strain rows for `Mucochytrium quahogii parasite QPX`.

## Additional Notes

- This target is the only Stramenopiles record in the reviewed batch; its shorter 10-row lineage matched the NCBI lineage cache.
