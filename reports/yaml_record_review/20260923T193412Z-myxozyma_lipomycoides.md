# YAML Record Review

- Target: `data/taxa/eukaryota/myxozyma_lipomycoides.yaml`
- Taxon: `NCBITaxon:54097` (`Myxozyma lipomycoides`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:54097`, label `Myxozyma lipomycoides`.
- It is grounded exactly under `NCBITaxon:54096` (`Myxozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Myxozyma`.

## Validation

- `just validate data/taxa/eukaryota/myxozyma_lipomycoides.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_lipomycoides.yaml data/taxa/eukaryota/myxozyma_melibiosi.yaml data/taxa/eukaryota/myxozyma_monticola.yaml data/taxa/eukaryota/myxozyma_mucilagina.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52911` contains the seeded identifier with reason `attested rule: Myxozyma lipomycoides, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6841` matches the YAML identity: parent `NCBITaxon:54096`, rank `SPECIES`, and related synonym `Myxozyma lipomycoides Van der Walt, Y. Yamada & Nakase, 1987`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6841` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38301`, where `NCBITaxon:54097` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705276` / `Myxozyma lipomycoides NRRL Y-17253`, linked to project `Gp0831311` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 14 type-material rows for `NCBITaxon:54097`, covering variants of `ATCC 52276`, `BCRC 22181`, `CCRC 22181`, `CBS 7038`, `CSIR Y-906`, `JCM 5198`, and `NRRL Y-17253`.
- Exact StrainInfo has 1 direct record and 11 deposit rows for `NCBITaxon:54097`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:54097`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:54097`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
