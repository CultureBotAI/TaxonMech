# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_vulgaris.yaml`
- Taxon: `NCBITaxon:60348` (`Morchella vulgaris`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:60348`, label `Morchella vulgaris`.
- It is grounded exactly under `NCBITaxon:1175439` (`Morchella sect. Morchella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Morchella`.

## Validation

- `just validate data/taxa/eukaryota/morchella_vulgaris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_steppicola.yaml ... morchella_vulgaris.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53022` contains the seeded identifier with reason `attested rule: Morchella vulgaris, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:7605` matches the YAML parent, rank, exact synonym `Morchella esculenta var. vulgaris`, and related synonyms `Morchella esculenta var. vulgaris Pers., 1801` and `Morchella vulgaris (Pers.) Gray, 1821`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:7605` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39786`, where `NCBITaxon:60348` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0535693` / `Morchella vulgaris PhC 271`, linked to projects `Gp0484071` and `Gp0484096`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:241106-241108` has three holotype aliases for `Morchella esculenta var. vulgaris`: `LIP 0900044`, `LIP:0900044`, and `LIP:PhC3`.

## Completeness

- Exact StrainInfo has three direct records and six deposit rows for `NCBITaxon:60348`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:60348`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:60348`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- This record closes the contiguous Morchella run before the eukaryote cursor moves on to `Mortierella`.
