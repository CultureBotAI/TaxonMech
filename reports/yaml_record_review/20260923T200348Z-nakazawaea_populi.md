# YAML Record Review

- Target: `data/taxa/eukaryota/nakazawaea_populi.yaml`
- Taxon: `NCBITaxon:1538184` (`Nakazawaea populi`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1538184`, label `Nakazawaea populi`.
- It is grounded exactly under `NCBITaxon:460521` (`Nakazawaea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `26`.
- The YAML carries 13 lineage entries from `root` through `Nakazawaea`.

## Validation

- `just validate data/taxa/eukaryota/nakazawaea_populi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakazawaea_molendinolei.yaml data/taxa/eukaryota/nakazawaea_peltata.yaml data/taxa/eukaryota/nakazawaea_pomicola.yaml data/taxa/eukaryota/nakazawaea_populi.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60427` contains the seeded identifier with reason `attested rule: Nakazawaea populi, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:396334` matches the YAML identity: parent `NCBITaxon:460521`, rank `SPECIES`, exact synonym `Candida populi`, two related synonyms, and genetic code `26`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:396334` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12234`, where `NCBITaxon:1538184` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705335` / `Nakazawaea populi NRRL Y-17681`, linked to project `Gp0831371` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 16 type-material rows for `NCBITaxon:1538184`, covering variants of `ATCC 64933`, `BCRC 22266`, `CBS 7351`, `CCRC 22266`, `JCM 9833`, `NRRL Y-17681`, `UCD 68-675.2`, and `UCD 68-675B`.
- Exact StrainInfo side inventory has 3 direct rows and 16 deposit entries for `NCBITaxon:1538184`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:51935`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.
