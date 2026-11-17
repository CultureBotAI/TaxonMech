# YAML Record Review

- Target: `data/taxa/eukaryota/neohortaea_acidophila.yaml`
- Taxon: `NCBITaxon:245834` (`Neohortaea acidophila`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:245834`, label `Neohortaea acidophila`.
- It is grounded exactly under `NCBITaxon:2072583` (`Neohortaea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neohortaea`.

## Validation

- `just validate data/taxa/eukaryota/neohortaea_acidophila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neofusicoccum_parvum.yaml data/taxa/eukaryota/neogymnomyces_virgineus.yaml data/taxa/eukaryota/neohortaea_acidophila.yaml data/taxa/eukaryota/neonectria_coccinea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54723` contains the seeded identifier with reason `attested rule: Neohortaea acidophila, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:48251` matches the YAML identity: parent `NCBITaxon:2072583`, rank `SPECIES`, three synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:48251` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:22129`, where `NCBITaxon:245834` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0111655` / `Neohortaea acidophila CBS 113389`.
- That native organism ID links to projects `Gp0110612` and `Gp0113715`; no native GOLD analysis rows were found for the linked projects.

## Completeness

- An exact field scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for `NCBITaxon:245834`, covering variants of `CBS 113389`.
- Exact StrainInfo side inventory found one direct record with exact deposits `CBS 113389` and `VTT D-05374`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:245834`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:245834`; the exact StrainInfo and type-material side inventories did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
