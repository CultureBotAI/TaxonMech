# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_prava.yaml`
- Taxon: `NCBITaxon:1174674` (`Morchella prava`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1174674`, label `Morchella prava`.
- It is grounded exactly under `NCBITaxon:1175439` (`Morchella sect. Morchella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Morchella`.

## Validation

- `just validate data/taxa/eukaryota/morchella_prava.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_norvegiensis.yaml ... morchella_prava.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58194` contains the seeded identifier with reason `attested rule: Morchella prava, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:260861` matches the YAML parent, rank, exact synonym `Morchella prava Dewsbury, Moncalvo, J.D. Moore & M. Kuo 2012`, and related synonym `Morchella sp. Mes-7`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:260861` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3863`, where `NCBITaxon:1174674` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0513057` / `Morchella prava NRRL 20872`, linked to projects `Gp0405452` and `Gp0405467`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:11422-11425` has four holotype aliases: `F 05100602`, `F-05100602`, `F05100602`, and `F:05100602`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1174674`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:1191131`, `NCBITaxon:746182`, and `NCBITaxon:746197` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The native GOLD organism keeps `NRRL 20872` in its name and `NRRL 20872-7` in its strain field; that does not affect the species-level GOLD organism count in the generated YAML.
