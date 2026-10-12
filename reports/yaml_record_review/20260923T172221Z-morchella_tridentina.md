# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_tridentina.yaml`
- Taxon: `NCBITaxon:1582345` (`Morchella tridentina`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1582345`, label `Morchella tridentina`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_tridentina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_steppicola.yaml ... morchella_vulgaris.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60531` contains the seeded identifier with reason `attested rule: Morchella tridentina, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:408395` matches the YAML parent, rank, exact synonyms `Morchella elatoides`, `Morchella elatoides var. elegans`, and `Morchella frustrata`, plus five related synonyms including `Morchella sp. Mel-2`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:408395` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12783`, where `NCBITaxon:1582345` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0568262` / `Morchella tridentina NRRL 54570`, linked to projects `Gp0538664`, `Gp0543297`, and `Gp0620574`; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:1582345` type-material rows.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1582345`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:1174672`, `NCBITaxon:1612314`, `NCBITaxon:1612316`, `NCBITaxon:746142`, and `NCBITaxon:746162` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- `Morchella frustrata` appears as an exact synonym and has one of this record's retired IDs in `data/raw/ncbi_merged_ids.tsv`; no retained retired row is present.
