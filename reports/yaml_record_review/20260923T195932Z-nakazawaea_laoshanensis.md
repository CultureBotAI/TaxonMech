# YAML Record Review

- Target: `data/taxa/eukaryota/nakazawaea_laoshanensis.yaml`
- Taxon: `NCBITaxon:1538180` (`Nakazawaea laoshanensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1538180`, label `Nakazawaea laoshanensis`.
- It is grounded exactly under `NCBITaxon:460521` (`Nakazawaea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `26`.
- The YAML carries 13 lineage entries from `root` through `Nakazawaea`.

## Validation

- `just validate data/taxa/eukaryota/nakazawaea_laoshanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakazawaea_ernobii.yaml data/taxa/eukaryota/nakazawaea_holstii.yaml data/taxa/eukaryota/nakazawaea_ishiwadae.yaml data/taxa/eukaryota/nakazawaea_laoshanensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60423` contains the seeded identifier with reason `attested rule: Nakazawaea laoshanensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:396330` matches the YAML identity: parent `NCBITaxon:460521`, rank `SPECIES`, exact synonym `Candida laoshanensis`, three related synonyms, and genetic code `26`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:396330` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12230`, where `NCBITaxon:1538180` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705586` / `Nakazawaea laoshanensis NRRL Y-63634`, linked to project `Gp0831630` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 8 type-material rows for `NCBITaxon:1538180`, covering variants of `AS 2.4030`, `CBS 11389`, `CGMCC 2.4030`, and `NRRL Y-63634`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1538180`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:593425`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.
