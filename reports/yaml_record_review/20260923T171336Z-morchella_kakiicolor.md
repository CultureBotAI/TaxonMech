# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_kakiicolor.yaml`
- Taxon: `NCBITaxon:2715921` (`Morchella kakiicolor`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2715921`, label `Morchella kakiicolor`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_kakiicolor.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_fluvialis.yaml ... morchella_kakiicolor.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62985` contains the seeded identifier with reason `attested rule: Morchella kakiicolor, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:546457` matches the YAML parent, rank, exact synonym `Morchella quercus-ilicis f. kakiicolor`, and three related synonyms including `Morchella sp. Mel-11`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:546457` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:25207`, where `NCBITaxon:2715921` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0515922` / `Morchella quercus-ilicis var. kakiicolor PhC 218` and `Go0515923` / `Morchella kakiicolor PhC 280`, linked to four projects `Gp0436670` through `Gp0436673`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:113159-113163` has five holotype aliases for `Morchella quercus-ilicis f. kakiicolor`: `Clowez 117`, `LIP 0900146`, `LIP:0900146`, `LIP:PhC117`, and `PhC117`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:2715921`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:746133` and `NCBITaxon:746153` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- One native GOLD organism still uses the synonym-bearing name `Morchella quercus-ilicis var. kakiicolor`, while NCBI carries `Morchella quercus-ilicis f. kakiicolor` as an exact synonym for the current species.
