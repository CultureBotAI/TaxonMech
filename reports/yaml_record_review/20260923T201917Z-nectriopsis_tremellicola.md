# YAML Record Review

- Target: `data/taxa/eukaryota/nectriopsis_tremellicola.yaml`
- Taxon: `NCBITaxon:2545913` (`Nectriopsis tremellicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2545913`, label `Nectriopsis tremellicola`.
- It is grounded exactly under `NCBITaxon:29865` (`Nectriopsis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nectriopsis`.

## Validation

- `just validate data/taxa/eukaryota/nectriopsis_tremellicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nectriaceae_sp.yaml data/taxa/eukaryota/nectriopsis_sporangiicola.yaml data/taxa/eukaryota/nectriopsis_tremellicola.yaml data/taxa/eukaryota/nemania_abortiva.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62771` contains the seeded identifier with reason `attested rule: Nectriopsis tremellicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:529947` matches the YAML identity: parent `NCBITaxon:29865`, rank `SPECIES`, exact synonyms `Hypocrea tremellicola` and `Hypomyces tremellicola`, three related synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:529947` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23139`, where `NCBITaxon:2545913` has `organism_count` 1.
- The current native GOLD catalogs have no exact organism, project, or analysis rows for `NCBITaxon:2545913`; the retained GOLD aggregate in `data/raw/gold_organisms.tsv` supplies the GOLD assertion.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for `NCBITaxon:2545913`.
- Exact StrainInfo side inventory has 5 direct rows and 5 deposit entries for `NCBITaxon:2545913`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:40603`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventory, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from current native GOLD exact rows.
