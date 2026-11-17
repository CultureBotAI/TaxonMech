# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_importuna.yaml`
- Taxon: `NCBITaxon:1174673` (`Morchella importuna`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1174673`, label `Morchella importuna`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_importuna.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_fluvialis.yaml ... morchella_kakiicolor.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58193` contains the seeded identifier with reason `attested rule: Morchella importuna, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:260860` matches the YAML parent, rank, exact synonym `Morchella importuna M. Kuo, O'Donnell & T.J. Volk 2012`, and related synonym `Morchella sp. Mel-10`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:260860` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3862`, where `NCBITaxon:1174673` has `organism_count` 4.
- Native GOLD has four exact current-taxid organism rows: `Go0044465` / `Morchella importuna CCBAS932`, `Go0111690` / `Morchella importuna SCYDJ1-A1`, `Go0593705` / `Morchella importuna M04M24`, and `Go0593706` / `Morchella importuna M04M26`.
- Complete native GOLD project expansion found six exact linked projects: `Gp0044465`, `Gp0044466`, `Gp0113789`, `Gp0113790`, `Gp0607650`, and `Gp0607651`.
- Native GOLD has three linked analyses, each joined through `AP PROJECT GOLD IDS` for `Gp0044465`, `Gp0607650`, or `Gp0607651`.
- `data/raw/ncbi_type_material.tsv:11420-11421` has two holotype aliases, `F 04130401` and `F:04130401`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1174673`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:746132` and `NCBITaxon:746152` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- GOLD currently supplies the broadest evidence footprint in this batch for this taxon: four native organism IDs, six projects, and three native analyses.
