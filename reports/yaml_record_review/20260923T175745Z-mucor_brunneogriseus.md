# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_brunneogriseus.yaml`
- Taxon: `NCBITaxon:1084247` (`Mucor brunneogriseus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1084247`, label `Mucor brunneogriseus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_brunneogriseus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_bainieri.yaml ... mucor_circinatus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57566` contains the seeded identifier with reason `attested rule: Mucor brunneogriseus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:232875` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact synonym `Mucor brunneus`, and related synonyms `Mucor brunneogriseus A.K. Sarbhoy 1968` and `Mucor brunneus Naumov 1935`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:232875` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1550`, where `NCBITaxon:1084247` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0470809` / `Mucor brunneus NRRL 2351`, linked to project `Gp0345297`; no native analysis row linked to that project.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found eight `NCBITaxon:1084247` type-material aliases: `ATCC 18468`, `ATCC:18468`, `CBS 129.41`, `CBS:129.41`, `IMI 116944`, `IMI:116944`, `NRRL 2630`, and `NRRL:2630`.

## Completeness

- Exact StrainInfo direct and deposit rows were empty for `NCBITaxon:1084247`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1084247`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1084247`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strain rows or an analysis row for the exact native GOLD project.

## Additional Notes

- Native GOLD uses the synonym-bearing organism name `Mucor brunneus NRRL 2351`, which is compatible with the NCBI exact synonym `Mucor brunneus`.
