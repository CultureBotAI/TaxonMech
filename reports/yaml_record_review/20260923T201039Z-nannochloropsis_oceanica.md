# YAML Record Review

- Target: `data/taxa/eukaryota/nannochloropsis_oceanica.yaml`
- Taxon: `NCBITaxon:145522` (`Nannochloropsis oceanica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:145522`, label `Nannochloropsis oceanica`.
- It is grounded exactly under `NCBITaxon:5748` (`Nannochloropsis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Nannochloropsis`.

## Validation

- `just validate data/taxa/eukaryota/nannochloropsis_oceanica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nannochloropsis_gaditana_ccmp526.yaml data/taxa/eukaryota/nannochloropsis_oceanica.yaml data/taxa/eukaryota/nannochloropsis_oceanica_strain_imet1.yaml data/taxa/eukaryota/nannochloropsis_oculata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54030` contains the seeded identifier with reason `attested rule: Nannochloropsis oceanica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:29549` matches the YAML identity: parent `NCBITaxon:5748`, rank `SPECIES`, four related synonyms, and genetic code `1`.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:29549` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11094`, where `NCBITaxon:145522` has `organism_count` 115.
- A complete exact native GOLD scan found 115 current-taxid organism rows for `NCBITaxon:145522`, matching the transformed GOLD aggregate count.
- Those 115 native organism IDs link to 168 native projects and 2 native analyses for `Nannochloropsis oceanica LAMB0001` and `Nannochloropsis oceanica LAMB2011`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for `NCBITaxon:145522`.
- Exact StrainInfo side inventory has 2 direct rows and 2 deposit entries for `NCBITaxon:145522`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1672965`, `NCBITaxon:72521`, and `NCBITaxon:72522`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The GOLD attestation explicitly covers records filed directly under `NCBITaxon:145522`; descendant taxa are not gathered, matching the attestation note.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventory, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
