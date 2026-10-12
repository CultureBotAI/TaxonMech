# YAML Record Review

- Target: `data/taxa/eukaryota/neocucurbitaria_cava.yaml`
- Taxon: `NCBITaxon:798079` (`Neocucurbitaria cava`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:798079`, label `Neocucurbitaria cava`.
- It is grounded exactly under `NCBITaxon:1986179` (`Neocucurbitaria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Neocucurbitaria`.

## Validation

- `just validate data/taxa/eukaryota/neocucurbitaria_cava.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoconidiobolus_thromboides_fsu_785.yaml data/taxa/eukaryota/neocucurbitaria_cava.yaml data/taxa/eukaryota/neodevriesia_sardiniae.yaml data/taxa/eukaryota/neofusicoccum_brasiliense.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56721` contains the seeded identifier with reason `attested rule: Neocucurbitaria cava, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:180011` matches the YAML identity: parent `NCBITaxon:1986179`, rank `SPECIES`, six synonyms, and genetic code `1`.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:180011` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42850`, where `NCBITaxon:798079` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0678673` / `Neocucurbitaria cava IMI 356814`.
- That native organism ID links to project `Gp0780633`, which has one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact field scan of `data/raw/ncbi_type_material.tsv` found 10 type-material rows for `NCBITaxon:798079`, covering variants of `CBS 257.68`, `CECT 20043`, `IMI 331911`, `FMR 15747`, and `CBS H-20320`.
- Exact StrainInfo side inventory found 23 direct records and 30 exact deposit assertions, including `CBS 257.68`, `CECT 20043`, `IMI 331911`, `CBS 325.63`, and `MUCL 8053`.
- An exact field scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:243024` and `NCBITaxon:318861`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:798079`; the exact StrainInfo and type-material side inventories did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
