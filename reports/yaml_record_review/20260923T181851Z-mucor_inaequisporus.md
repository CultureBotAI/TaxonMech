# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_inaequisporus.yaml`
- Taxon: `NCBITaxon:1196534` (`Mucor inaequisporus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1196534`, label `Mucor inaequisporus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_inaequisporus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_hiemalis_f_silvaticus.yaml ... mucor_indicus_b7402.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58291` contains the seeded identifier with reason `attested rule: Mucor inaequisporus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:269147` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor inaequisporus Dade, 1937`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:269147` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4739`, where `NCBITaxon:1196534` has `organism_count` 7.
- Exact native GOLD expansion found seven exact current-taxid organism rows; only `Go0470957` and `Go0535970` joined to native projects, and no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found eight `NCBITaxon:1196534` type-material aliases for `CBS 255.36`, `CCF 2015`, `DSM 2187`, and `IFO 8635`.

## Completeness

- Exact StrainInfo has seven direct records and 22 deposit rows for `NCBITaxon:1196534`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1196534`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1196534`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The native GOLD project join is narrower than the exact organism set; the local snapshot has seven exact organisms but only two joined projects.
