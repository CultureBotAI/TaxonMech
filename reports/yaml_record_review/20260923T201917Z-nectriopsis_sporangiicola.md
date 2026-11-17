# YAML Record Review

- Target: `data/taxa/eukaryota/nectriopsis_sporangiicola.yaml`
- Taxon: `NCBITaxon:1155948` (`Nectriopsis sporangiicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1155948`, label `Nectriopsis sporangiicola`.
- It is grounded exactly under `NCBITaxon:29865` (`Nectriopsis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nectriopsis`.

## Validation

- `just validate data/taxa/eukaryota/nectriopsis_sporangiicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nectriaceae_sp.yaml data/taxa/eukaryota/nectriopsis_sporangiicola.yaml data/taxa/eukaryota/nectriopsis_tremellicola.yaml data/taxa/eukaryota/nemania_abortiva.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58040` contains the seeded identifier with reason `attested rule: Nectriopsis sporangiicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:253099` matches the YAML identity: parent `NCBITaxon:29865`, rank `SPECIES`, exact synonyms `Nectria sporangiicola` and `Rhopalocladium myxophilum`, two related synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:253099` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3142`, where `NCBITaxon:1155948` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0019246` / `Nectriopsis sporangiicola NRRL 22127`, linked to projects `Gp0019246` and `Gp0019314`.
- A native GOLD analysis for `Nectriopsis sporangiicola NRRL 22127` is linked through `AP PROJECT GOLD IDS` to `Gp0019246`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for `NCBITaxon:1155948`.
- Exact StrainInfo side inventory has 2 direct rows and 3 deposit entries for `NCBITaxon:1155948`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:29866`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventory, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.
