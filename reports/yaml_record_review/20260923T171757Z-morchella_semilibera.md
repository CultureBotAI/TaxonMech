# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_semilibera.yaml`
- Taxon: `NCBITaxon:62758` (`Morchella semilibera`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:62758`, label `Morchella semilibera`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_semilibera.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_pulchella.yaml ... morchella_semilibera.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53051` contains the seeded identifier with reason `attested rule: Morchella semilibera, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:7925` matches the YAML parent, rank, eight exact synonyms, and ten related synonyms, including `Morchella sp. Mel-3`, `Morchella sp. Mel-39`, and `semifree morel`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:7925` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40012`, where `NCBITaxon:62758` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0553124` / `Morchella crassipes M84`, linked to projects `Gp0543365` and `Gp0543366`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:242717-242720` has four neotype aliases: `LIP 0900126`, `LIP:0900126`, `PhC 99 (LIP)`, and `PhC99`.

## Completeness

- The exact StrainInfo scan found 12 direct records and 24 deposit rows for `NCBITaxon:62758`, but none joined into generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:62758`.
- A complete ignored-file-inclusive scan of `data/raw/ncbi_merged_ids.tsv` found six retired IDs mapping into this target: `NCBITaxon:1009838`, `NCBITaxon:1222196`, `NCBITaxon:1616672`, `NCBITaxon:221242`, `NCBITaxon:2976714`, and `NCBITaxon:62754`.
- A complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows for those retired IDs, so they are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- Native GOLD uses `Morchella crassipes`, one of the current record's exact synonyms, for the single current-taxid organism row.
