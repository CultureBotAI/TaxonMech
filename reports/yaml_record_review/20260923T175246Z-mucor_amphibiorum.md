# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_amphibiorum.yaml`
- Taxon: `NCBITaxon:90263` (`Mucor amphibiorum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:90263`, label `Mucor amphibiorum`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_amphibiorum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_ambiguus.yaml ... mucor_azygosporus.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53499` contains the seeded identifier with reason `attested rule: Mucor amphibiorum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14503` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor amphibiorum Schipper, 1978`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14503` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44108`, where `NCBITaxon:90263` has `organism_count` 4.
- Native GOLD has four exact current-taxid organism rows, `Go0607782`, `Go0607783`, `Go0607784`, and `Go0607785`; no native project rows were linked to those organism IDs.
- A complete exact `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found nine rows for `NCBITaxon:90263`: `CBS 763.74` culture-from-type-material aliases plus `CCF 2018`, `DSM 2190`, and `VKM F-3179` type-material aliases.

## Completeness

- Exact StrainInfo has six direct records and 10 deposit rows for `NCBITaxon:90263`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:90263`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:90263`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The local native GOLD organism evidence is present, but the current native exact scan found no project rows for the four exact organism IDs.
