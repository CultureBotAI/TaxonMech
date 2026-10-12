# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_ulmaria.yaml`
- Taxon: `NCBITaxon:1582346` (`Morchella ulmaria`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1582346`, label `Morchella ulmaria`.
- It is grounded exactly under `NCBITaxon:1175439` (`Morchella sect. Morchella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Morchella`.

## Validation

- `just validate data/taxa/eukaryota/morchella_ulmaria.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_steppicola.yaml ... morchella_vulgaris.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60532` contains the seeded identifier with reason `attested rule: Morchella ulmaria, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:408396` matches the YAML parent, rank, exact synonym `Morchella cryptica`, and related synonyms `Morchella cryptica M. Kuo & J.D. Moore 2012`, `Morchella sp. Mes-11`, and `Morchella ulmaria Clowez, 2012`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:408396` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12784`, where `NCBITaxon:1582346` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0568255` / `Morchella ulmaria NRRL 36825`, linked to projects `Gp0538652` and `Gp0538653`; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found six holotype aliases at lines 44305-44310, covering `LIP 0900152`, hyphen/colon/no-space variants, `LIP:PhC124`, and `PhC124`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1582346`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:746173` and `NCBITaxon:746186` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The exact synonym `Morchella cryptica` is represented in the NCBI synonym split but has no retained retired taxon row in this local snapshot.
