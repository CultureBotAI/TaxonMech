# YAML Record Review

- Target: `data/taxa/eukaryota/nakaseomyces_nivariensis.yaml`
- Taxon: `NCBITaxon:418086` (`Nakaseomyces nivariensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:418086`, label `Nakaseomyces nivariensis`.
- It is grounded exactly under `NCBITaxon:374468` (`Nakaseomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nakaseomyces`.

## Validation

- `just validate data/taxa/eukaryota/nakaseomyces_nivariensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakaseomyces_glabratus_m202019.yaml data/taxa/eukaryota/nakaseomyces_glabratus_uob301.yaml data/taxa/eukaryota/nakaseomyces_kungkrabaensis.yaml data/taxa/eukaryota/nakaseomyces_nivariensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55580` contains the seeded identifier with reason `attested rule: Nakaseomyces nivariensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:91515` matches the YAML identity: parent `NCBITaxon:374468`, rank `SPECIES`, exact synonym `Candida nivariensis`, and three related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:91515` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34959`, where `NCBITaxon:418086` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705535` / `Nakaseomyces nivariensis NRRL Y-48269`, linked to project `Gp0831578` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 10 culture-from-holotype or holotype rows for `NCBITaxon:418086`, under synonym name `Candida nivariensis`.
- Exact StrainInfo side inventory has 7 direct rows and 9 deposit entries for `NCBITaxon:418086`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:150220`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- The YAML correctly files only records directly under `NCBITaxon:418086`; descendant taxa are not gathered into this species record.
