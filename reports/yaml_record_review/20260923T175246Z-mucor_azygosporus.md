# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_azygosporus.yaml`
- Taxon: `NCBITaxon:1196528` (`Mucor azygosporus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1196528`, label `Mucor azygosporus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_azygosporus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_ambiguus.yaml ... mucor_azygosporus.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58290` contains the seeded identifier with reason `attested rule: Mucor azygosporus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:269146` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor azygosporus R.K. Benj., 1963`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:269146` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4738`, where `NCBITaxon:1196528` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0470908` / `Mucor azygosporus Benjamin NRRL 3068`, linked to project `Gp0345396`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:12962-12963` has `CBS 292.63` culture-from-isotype aliases.

## Completeness

- Exact StrainInfo has two direct records and eight deposit rows for `NCBITaxon:1196528`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1196528`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1196528`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The native GOLD culture collection ID is `ATCC 15087`, while the NCBI type-material evidence for this target is the `CBS 292.63` isotype culture pair.
