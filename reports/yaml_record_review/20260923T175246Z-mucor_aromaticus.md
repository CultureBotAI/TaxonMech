# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_aromaticus.yaml`
- Taxon: `NCBITaxon:2572689` (`Mucor aromaticus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2572689`, label `Mucor aromaticus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_aromaticus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_ambiguus.yaml ... mucor_azygosporus.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62841` contains the seeded identifier with reason `attested rule: Mucor aromaticus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:532251` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor aromaticus Povah, 1917`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:532251` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23478`, where `NCBITaxon:2572689` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0470808` / `Mucor aromaticus NRRL A-17745`, linked to project `Gp0345296`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:102315-102318` has `MICH 12489` holotype aliases.

## Completeness

- Exact StrainInfo has one direct record and one deposit row for `NCBITaxon:2572689`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:2572689`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:2572689`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The bounded scan fully covered the native GOLD evidence for this target.
