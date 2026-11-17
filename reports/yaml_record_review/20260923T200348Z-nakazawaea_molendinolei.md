# YAML Record Review

- Target: `data/taxa/eukaryota/nakazawaea_molendinolei.yaml`
- Taxon: `NCBITaxon:1538181` (`Nakazawaea molendinolei`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1538181`, label `Nakazawaea molendinolei`.
- It is grounded exactly under `NCBITaxon:460521` (`Nakazawaea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `26`.
- The YAML carries 13 lineage entries from `root` through `Nakazawaea`.

## Validation

- `just validate data/taxa/eukaryota/nakazawaea_molendinolei.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/nakazawaea_molendinolei.yaml data/taxa/eukaryota/nakazawaea_peltata.yaml data/taxa/eukaryota/nakazawaea_pomicola.yaml data/taxa/eukaryota/nakazawaea_populi.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60424` contains the seeded identifier with reason `attested rule: Nakazawaea molendinolei, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:396331` matches the YAML identity: parent `NCBITaxon:460521`, rank `SPECIES`, exact synonyms `Candida molendinolei Cadez, Turchetti & G. Peter, 2011` and `Nakazawaea molendinolei (Cadez, Turchetti & G. Peter) Kurtzman & Robnett, 2014`, three related `Candida sp. DBVPG` synonyms, and genetic code `26`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:396331` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12231`, where `NCBITaxon:1538181` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705041` / `Nakazawaea molendinolei CBS 12508`, linked to project `Gp0831061` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for `NCBITaxon:1538181`, covering variants of `CBS 12508` and `DBVPG 5508`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1538181`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1108740`, `NCBITaxon:1108741`, `NCBITaxon:1108742`, and `NCBITaxon:1171600`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
