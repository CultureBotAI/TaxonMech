# YAML Record Review

- Target: `data/taxa/eukaryota/neonectria_coccinea.yaml`
- Taxon: `NCBITaxon:57153` (`Neonectria coccinea`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:57153`, label `Neonectria coccinea`.
- It is grounded exactly under `NCBITaxon:140106` (`Neonectria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neonectria`.

## Validation

- `just validate data/taxa/eukaryota/neonectria_coccinea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neofusicoccum_parvum.yaml data/taxa/eukaryota/neogymnomyces_virgineus.yaml data/taxa/eukaryota/neohortaea_acidophila.yaml data/taxa/eukaryota/neonectria_coccinea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52977` contains the seeded identifier with reason `attested rule: Neonectria coccinea, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:7266` matches the YAML identity: parent `NCBITaxon:140106`, rank `SPECIES`, five synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:7266` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39154`, where `NCBITaxon:57153` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0678571` / `Neonectria coccinea CBS 119158`.
- That native organism ID links to project `Gp0780531`, which has one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:57153`.
- Exact StrainInfo side inventory found 27 direct records and 42 exact deposit assertions, including `MUCL 8081`, `CBS 476.63`, `CBS 125.24`, `KCTC 16046`, and `CBS 580.89`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:57153`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:57153`; the exact StrainInfo side inventory did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
