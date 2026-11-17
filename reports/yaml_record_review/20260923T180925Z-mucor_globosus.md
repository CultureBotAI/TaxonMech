# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_globosus.yaml`
- Taxon: `NCBITaxon:2184028` (`Mucor globosus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2184028`, label `Mucor globosus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_globosus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_fuscus.yaml ... mucor_griseo_ochraceus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62461` contains the seeded identifier with reason `attested rule: Mucor globosus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:521115` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor globosus Schreb., 1771`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:521115` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:20808`, where `NCBITaxon:2184028` has `organism_count` 4.
- Native GOLD has three exact current-taxid organism rows, `Go0402566`, `Go0470851`, and `Go0470933`, linked to three projects; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:2184028` type-material rows.

## Completeness

- Exact StrainInfo direct and deposit rows were empty for `NCBITaxon:2184028`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:2184028`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:2184028`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strain rows or an analysis row for the exact native GOLD projects.

## Additional Notes

- The transformed GOLD aggregate count is 4, while the local native GOLD exact scan found three current-taxid organism rows.
