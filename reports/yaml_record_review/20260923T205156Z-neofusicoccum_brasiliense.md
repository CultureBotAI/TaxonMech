# YAML Record Review

- Target: `data/taxa/eukaryota/neofusicoccum_brasiliense.yaml`
- Taxon: `NCBITaxon:1389135` (`Neofusicoccum brasiliense`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1389135`, label `Neofusicoccum brasiliense`.
- It is grounded exactly under `NCBITaxon:407951` (`Neofusicoccum`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neofusicoccum`.

## Validation

- `just validate data/taxa/eukaryota/neofusicoccum_brasiliense.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoconidiobolus_thromboides_fsu_785.yaml data/taxa/eukaryota/neocucurbitaria_cava.yaml data/taxa/eukaryota/neodevriesia_sardiniae.yaml data/taxa/eukaryota/neofusicoccum_brasiliense.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59822` contains the seeded identifier with reason `attested rule: Neofusicoccum brasiliense, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:340555` matches the YAML identity: parent `NCBITaxon:407951`, rank `SPECIES`, four related synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:340555` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9200`, where `NCBITaxon:1389135` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0535708` / `Neofusicoccum brasiliense LGMF1535`.
- That native organism ID links to projects `Gp0484094`, `Gp0487791`, and `Gp0620576`; no native GOLD analysis rows were found for the linked projects.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1389135`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1389135`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1260370`, `NCBITaxon:1260371`, and `NCBITaxon:1260442`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
