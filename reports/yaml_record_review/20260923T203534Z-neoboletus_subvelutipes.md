# YAML Record Review

- Target: `data/taxa/eukaryota/neoboletus_subvelutipes.yaml`
- Taxon: `NCBITaxon:2717575` (`Neoboletus subvelutipes`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2717575`, label `Neoboletus subvelutipes`.
- It is grounded exactly under `NCBITaxon:1629869` (`Neoboletus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Neoboletus`.

## Validation

- `just validate data/taxa/eukaryota/neoboletus_subvelutipes.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoboletus_erythropus.yaml data/taxa/eukaryota/neoboletus_magnificus.yaml data/taxa/eukaryota/neoboletus_subvelutipes.yaml data/taxa/eukaryota/neobulgaria_alba.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62986` contains the seeded identifier with reason `attested rule: Neoboletus subvelutipes, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:546833` matches the YAML identity: parent `NCBITaxon:1629869`, rank `SPECIES`, six synonyms, and genetic code `1`.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:546833` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:25230`, where `NCBITaxon:2717575` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows: `Go0518049` / `Boletus subvelutipes MG31` and `Go0676964` / `Boletus subvelutipes KM-2022`.
- Those native organism IDs link to projects `Gp0442118` and `Gp0778770`, each with one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for `NCBITaxon:2717575`, covering holotype `NYS:f3093` and isotype `DAOM:43225`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:2717575`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1985684`, `NCBITaxon:279509`, and `NCBITaxon:2950493`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
