# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_esculenta.yaml`
- Taxon: `NCBITaxon:39407` (`Morchella esculenta`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:39407`, label `Morchella esculenta`.
- It is grounded exactly under `NCBITaxon:1175439` (`Morchella sect. Morchella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Morchella`.

## Validation

- `just validate data/taxa/eukaryota/morchella_esculenta.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_dunalii.yaml ... morchella_eximia.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52403` contains the seeded identifier with reason `attested rule: Morchella esculenta, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4442` matches the YAML parent, rank, exact synonym `Phallus esculentus`, and related synonyms `Morchella cf. esculenta OSC 100041`, `Morchella esculenta (L.) Pers., 1797`, `Morchella sp. Mes-8`, `Phallus esculentus L., 1753`, and `yellow morel`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4442` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34222`, where `NCBITaxon:39407` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0535696` / `Morchella esculenta PhC 158`, linked to projects `Gp0484077` and `Gp0484099`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:202215-202218` has four holotype aliases for the exact synonym `Phallus esculentus`: `LIP 0900051`, `LIP:0900051`, `LIP:PhC10`, and `PhC10`.

## Completeness

- The exact StrainInfo scan found 41 direct records and 77 deposit rows for `NCBITaxon:39407`, but none joined into generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:39407`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:265111`, `NCBITaxon:746183`, and `NCBITaxon:746198` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the large StrainInfo exact-match side inventory.

## Additional Notes

- The YAML GOLD assertion count follows the transformed aggregate in `data/raw/gold_organisms.tsv`; a direct scan of the native GOLD organism JSONL by the current taxid plus the three locally known retired taxids returned the current `PhC 158` row.
