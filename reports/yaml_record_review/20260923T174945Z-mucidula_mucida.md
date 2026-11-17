# YAML Record Review

- Target: `data/taxa/eukaryota/mucidula_mucida.yaml`
- Taxon: `NCBITaxon:139077` (`Mucidula mucida`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:139077`, label `Mucidula mucida`.
- It is grounded exactly under `NCBITaxon:937601` (`Mucidula`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mucidula`.

## Validation

- `just validate data/taxa/eukaryota/mucidula_mucida.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucidula_mucida.yaml ... mucor_alternans.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53996` contains the seeded identifier with reason `attested rule: Mucidula mucida, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:28089` matches the YAML identity: parent `NCBITaxon:937601`, rank `SPECIES`, five exact synonyms, and four related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:28089` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9224`, where `NCBITaxon:139077` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows, `Go0111941`, `Go0111942`, and `Go0369094`, linked to three projects; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:27910-27913` has `TENN 062246` neotype aliases and `TENN 62246` type-material aliases under the former `Agaricus mucidus` name.

## Completeness

- Exact StrainInfo has 22 direct records and 27 deposit rows for `NCBITaxon:139077`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:139077`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:139077`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The local native GOLD evidence includes one retained former-name organism row for `Oudemansiella mucida` and two current-name `Mucidula mucida` rows.
