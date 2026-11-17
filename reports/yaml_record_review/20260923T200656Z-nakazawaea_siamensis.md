# YAML Record Review

- Target: `data/taxa/eukaryota/nakazawaea_siamensis.yaml`
- Taxon: `NCBITaxon:1449382` (`Nakazawaea siamensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1449382`, label `Nakazawaea siamensis`.
- It is grounded exactly under `NCBITaxon:460521` (`Nakazawaea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `26`.
- The YAML carries 13 lineage entries from `root` through `Nakazawaea`.

## Validation

- `just validate data/taxa/eukaryota/nakazawaea_siamensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakazawaea_siamensis.yaml data/taxa/eukaryota/nakazawaea_wickerhamii.yaml data/taxa/eukaryota/nakazawaea_wyomingensis.yaml data/taxa/eukaryota/nannochloropsis_gaditana.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60183` contains the seeded identifier with reason `attested rule: Nakazawaea siamensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:365778` matches the YAML identity: parent `NCBITaxon:460521`, rank `SPECIES`, three related synonyms, and genetic code `26`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:365778` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:10939`, where `NCBITaxon:1449382` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705047` / `Nakazawaea siamensis CBS 12569`, linked to project `Gp0831067` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 10 type-material rows for `NCBITaxon:1449382`, covering variants of `DMKU RK467`, `BCC 50734`, `BCC<THA>:50734`, `CBS 12569`, and `NBRC 108903`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1449382`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:1274392`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.
