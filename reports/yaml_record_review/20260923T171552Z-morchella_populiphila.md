# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_populiphila.yaml`
- Taxon: `NCBITaxon:1174669` (`Morchella populiphila`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1174669`, label `Morchella populiphila`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_populiphila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_norvegiensis.yaml ... morchella_prava.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58190` contains the seeded identifier with reason `attested rule: Morchella populiphila, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:260857` matches the YAML parent, rank, exact synonym `Morchella populiphila M. Kuo, M.C. Carter & J.D. Moore 2012`, and related synonym `Morchella sp. Mel-5`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:260857` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3859`, where `NCBITaxon:1174669` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0568256` / `Morchella populiphila NRRL 22315`, linked to projects `Gp0538654` and `Gp0538655`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:11408-11409` has two holotype aliases, `F 03240401` and `F:03240401`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1174669`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:746148`, `NCBITaxon:746151`, `NCBITaxon:746168`, and `NCBITaxon:746172` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The GOLD source attestation is a single-organism aggregate with the same single exact current-taxid organism in the native GOLD JSONL.
