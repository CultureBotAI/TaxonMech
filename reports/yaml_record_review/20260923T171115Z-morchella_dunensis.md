# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_dunensis.yaml`
- Taxon: `NCBITaxon:1810709` (`Morchella dunensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1810709`, label `Morchella dunensis`.
- It is grounded exactly under `NCBITaxon:1175439` (`Morchella sect. Morchella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Morchella`.

## Validation

- `just validate data/taxa/eukaryota/morchella_dunensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_dunalii.yaml ... morchella_eximia.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61300` contains the seeded identifier with reason `attested rule: Morchella dunensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:473441` matches the YAML parent, rank, and synonym split: exact synonyms `Morchella esculenta f. dunensis`, `Morchella spongiola var. dunensis`, and `Morchella vulgaris var. dunensis`, plus five related synonyms including `Morchella sp. Mes-17` and `Morchella sp. PA-2020a`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:473441` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:16000`, where `NCBITaxon:1810709` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0568260` / `Morchella vulgaris Mes-17` with culture collection `NRRL 53840`, linked to projects `Gp0538662` and `Gp0543299`; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:1810709` type-material rows.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1810709`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:1009839`, `NCBITaxon:2793119`, and `NCBITaxon:62756` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retired-ID provenance to this record.

## Additional Notes

- The native GOLD organism name still uses `Morchella vulgaris Mes-17`, while NCBI now represents `Morchella vulgaris var. dunensis` as an exact synonym of the current `Morchella dunensis` species.
