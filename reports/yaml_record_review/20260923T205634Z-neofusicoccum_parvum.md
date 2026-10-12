# YAML Record Review

- Target: `data/taxa/eukaryota/neofusicoccum_parvum.yaml`
- Taxon: `NCBITaxon:310453` (`Neofusicoccum parvum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:310453`, label `Neofusicoccum parvum`.
- It is grounded exactly under `NCBITaxon:407951` (`Neofusicoccum`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neofusicoccum`.

## Validation

- `just validate data/taxa/eukaryota/neofusicoccum_parvum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neofusicoccum_parvum.yaml data/taxa/eukaryota/neogymnomyces_virgineus.yaml data/taxa/eukaryota/neohortaea_acidophila.yaml data/taxa/eukaryota/neonectria_coccinea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55127` contains the seeded identifier with reason `attested rule: Neofusicoccum parvum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:63550` matches the YAML identity: parent `NCBITaxon:407951`, rank `SPECIES`, eight synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:63550` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:31338`, where `NCBITaxon:310453` has `organism_count` 14.
- The complete native GOLD exact scan found 14 current-taxid organism rows and 14 linked projects.
- The complete native GOLD analysis join found 14 analysis rows linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact field scan of `data/raw/ncbi_type_material.tsv` found 5 type-material rows for `NCBITaxon:310453`, covering `ICMP:8003`, variants of holotype `PDD 45438`, and variants of `CMW 9081`.
- Exact StrainInfo side inventory found 47 direct records and 48 exact deposit assertions, including `ICMP 21539`, `CBS 110301`, `ICMP 2096`, `ICMP 7009`, and `ICMP 10314`.
- An exact field scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1073912`, `NCBITaxon:120390`, `NCBITaxon:1620402`, and `NCBITaxon:223422`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:310453`; the exact StrainInfo and type-material side inventories did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
