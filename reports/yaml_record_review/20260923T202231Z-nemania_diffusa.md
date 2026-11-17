# YAML Record Review

- Target: `data/taxa/eukaryota/nemania_diffusa.yaml`
- Taxon: `NCBITaxon:389665` (`Nemania diffusa`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:389665`, label `Nemania diffusa`.
- It is grounded exactly under `NCBITaxon:109374` (`Nemania`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nemania`.

## Validation

- `just validate data/taxa/eukaryota/nemania_diffusa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nemania_diffusa.yaml data/taxa/eukaryota/nemania_maritima.yaml data/taxa/eukaryota/nemania_serpens.yaml data/taxa/eukaryota/nematocida_ausubeli.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55469` contains the seeded identifier with reason `attested rule: Nemania diffusa, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:82357` matches the YAML identity: parent `NCBITaxon:109374`, rank `SPECIES`, exact synonym `Sphaeria diffusa`, three related synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:82357` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34071`, where `NCBITaxon:389665` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0498790` / `Nemania diffusa NC0034`.
- A complete exact native GOLD project join found 22 projects for `Go0498790` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for `NCBITaxon:389665`.
- Exact StrainInfo side inventory has 5 direct rows and 5 deposit entries for `NCBITaxon:389665`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:1181067`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventory, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.
