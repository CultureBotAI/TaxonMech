# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_hiemalis.yaml`
- Taxon: `NCBITaxon:64493` (`Mucor hiemalis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64493`, label `Mucor hiemalis`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_hiemalis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_griseocyanus.yaml ... mucor_hiemalis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53079` contains the seeded identifier with reason `attested rule: Mucor hiemalis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8166` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact synonym `Mucor sp. heimalis`, and related synonyms `Mucor hiemalis Wehmer, 1903` and `Mucor sp. Gr22`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8166` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40305`, where `NCBITaxon:64493` has `organism_count` 29.
- Exact native GOLD expansion found 26 exact current-taxid organism rows linked to 24 projects; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:244326-244327` has the `CBS 201.65` and `CBS:201.65` neotype aliases.

## Completeness

- Exact StrainInfo has 140 direct records and 186 deposit rows for `NCBITaxon:64493`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64493`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1081915` and `NCBITaxon:319164` into this current taxon.
- The bounded retained-row scan found no local retired-ID provenance, so the YAML's empty `replaces` list is consistent.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The source attestation explicitly counts records filed directly under `NCBITaxon:64493`; descendant taxa are not gathered.
