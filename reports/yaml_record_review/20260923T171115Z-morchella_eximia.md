# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_eximia.yaml`
- Taxon: `NCBITaxon:1582338` (`Morchella eximia`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1582338`, label `Morchella eximia`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_eximia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_dunalii.yaml ... morchella_eximia.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60529` contains the seeded identifier with reason `attested rule: Morchella eximia, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:408393` matches the YAML parent, rank, exact synonym `Morchella septimelata`, and related synonyms `Morchella eximia Boud., 1910`, `Morchella septimelata M. Kuo, 2012`, and `Morchella sp. Mel-7`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:408393` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12781`, where `NCBITaxon:1582338` has `organism_count` 5.
- Native GOLD has three exact current-taxid organism rows: `Go0401822` / `Morchella eximia CBS 144461`, `Go0518079` / `Morchella eximia MG90`, and `Go0568258` / `Morchella eximia NRRL 26621`.
- The current native GOLD organism IDs have 20 exact linked projects: `Gp0272392`, `Gp0442148`, `Gp0538658`, `Gp0538659`, `Gp0595939`, and `Gp0851308` through `Gp0851322`; native analysis `Morchella eximia MG90` links through `AP PROJECT GOLD IDS` `Gp0442148`.
- Native GOLD also has two `Morchella septimelata` rows still tagged with retired `1174676`, accounting for the transformed aggregate's five-organism count.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found eight type-material rows at lines 44281-44288, covering six `Morchella eximia` epitype aliases and two `Morchella septimelata` holotype aliases.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1582338`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:1174676`, `NCBITaxon:746150`, and `NCBITaxon:746170` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retired-ID provenance to this record.

## Additional Notes

- The GOLD aggregate count spans both current `Morchella eximia` rows and native `Morchella septimelata` rows whose NCBI taxid has since merged into `NCBITaxon:1582338`.
