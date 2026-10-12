# YAML Record Review

- Target: `data/taxa/eukaryota/neocamarosporium_betae.yaml`
- Taxon: `NCBITaxon:1979465` (`Neocamarosporium betae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1979465`, label `Neocamarosporium betae`.
- It is grounded exactly under `NCBITaxon:1508285` (`Neocamarosporium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Neocamarosporium`.

## Validation

- `just validate data/taxa/eukaryota/neocamarosporium_betae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocallimastix_patriciarum.yaml data/taxa/eukaryota/neocallimastix_sp.yaml data/taxa/eukaryota/neocallimastix_sp_constans.yaml data/taxa/eukaryota/neocamarosporium_betae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61805` contains the seeded identifier with reason `attested rule: Neocamarosporium betae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:507584` matches the YAML identity: parent `NCBITaxon:1508285`, rank `SPECIES`, six synonyms, and genetic code `1`.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:507584` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:18313`, where `NCBITaxon:1979465` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0590581` / `Neocamarosporium betae Pb1`.
- That native organism ID links to project `Gp0604526`, which has one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1979465`.
- Exact StrainInfo side inventory found 14 direct records and 18 exact deposit assertions across 15 matching records, including `ICMP 22602`, `CBS 264.55`, `CBS 111.85`, `CBS 625.68`, `DSM 63181`, `ATCC 6504`, `ATCC 7892`, and `CGMCC 3.3698`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:137527`, `NCBITaxon:2082003`, and `NCBITaxon:45304`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1979465`; the exact StrainInfo side inventory did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
