# YAML Record Review: Metschnikowia chrysoperlae

- Record: `data/taxa/eukaryota/metschnikowia_chrysoperlae.yaml`
- Reviewed: `2026-09-23T15:56:34Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:261276`
- Label: `Metschnikowia chrysoperlae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_chrysoperlae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_chrysomelidarum.yaml data/taxa/eukaryota/metschnikowia_chrysoperlae.yaml data/taxa/eukaryota/metschnikowia_colocasiae.yaml data/taxa/eukaryota/metschnikowia_continentalis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:53381` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The eight related synonyms in the YAML match the NCBI row, including the six `Candida sp. Gibson-*` names; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54840` includes `NCBITaxon:261276` with reason `attested rule: Metschnikowia chrysoperlae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:24101` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project pair for `Metschnikowia chrysoperlae NRRL Y-27615`: `Go0705461` and `Gp0831504`; no linked native GOLD analysis row was found.
- A complete `rg --no-ignore --hidden` scan found nine NCBI type-material rows at `data/raw/ncbi_type_material.tsv:106107-106115`, covering `ATCC MYA-4304`, `CBS 9803`, `Gibson-A`, and `NRRL Y-27615` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:46395-46399` maps side-inventory old IDs `NCBITaxon:261277`, `NCBITaxon:261278`, `NCBITaxon:261279`, `NCBITaxon:261280`, and `NCBITaxon:261281` into `NCBITaxon:261276`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the nine type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the five omitted Gibson old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:261276`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
