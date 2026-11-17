# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_ambiguus.yaml`
- Taxon: `NCBITaxon:91626` (`Mucor ambiguus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:91626`, label `Mucor ambiguus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_ambiguus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_ambiguus.yaml ... mucor_azygosporus.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53517` contains the seeded identifier with reason `attested rule: Mucor ambiguus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14828` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and no related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14828` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44467`, where `NCBITaxon:91626` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0117300` / `Mucor ambiguus NBRC 6742`, linked to project `Gp0122235` and one native analysis row, `Mucor ambiguus NBRC 6742`.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:91626` type-material rows.

## Completeness

- Exact StrainInfo has three direct records and seven deposit rows for `NCBITaxon:91626`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:91626`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:91626`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The single native GOLD analysis row links through `AP PROJECT GOLD IDS` to the exact native project `Gp0122235`.
