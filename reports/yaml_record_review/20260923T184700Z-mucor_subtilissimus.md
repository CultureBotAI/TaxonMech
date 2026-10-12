# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_subtilissimus.yaml`
- Taxon: `NCBITaxon:64621` (`Mucor subtilissimus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64621`, label `Mucor subtilissimus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_subtilissimus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_sp.yaml ... mucor_tenuis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53103` contains the seeded identifier with reason `attested rule: Mucor subtilissimus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8200` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor subtilissimus Berk., 1835`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8200` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40355`, where `NCBITaxon:64621` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0535939` / `Mucor subtilissimus NRRL 6226`, linked to project `Gp0484414`; no native analysis row linked to that project.

## Completeness

- Exact StrainInfo has 16 direct records and 24 deposit rows for `NCBITaxon:64621`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:64621`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:64621`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
