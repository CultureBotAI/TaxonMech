# YAML Record Review: Metschnikowia zobellii

- Record: `data/taxa/eukaryota/metschnikowia_zobellii.yaml`
- Reviewed: `2026-09-23T16:25:03Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27328`
- Label: `Metschnikowia zobellii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_zobellii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_torresii.yaml data/taxa/eukaryota/metschnikowia_vanudenii.yaml data/taxa/eukaryota/metschnikowia_viticola.yaml data/taxa/eukaryota/metschnikowia_zobellii.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2739` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The `Metschnikowia zobelli` misspelling, `Metschnikowiella zobellii` basionym, and authority-bearing related synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52156` includes `NCBITaxon:27328` with reason `attested rule: Metschnikowia zobellii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25475` reports GOLD organism count `8`, matching the YAML GOLD `assertion_count`.
- A complete exact scan of the native GOLD snapshot contains six exact organism rows for `NRRL Y-5387`, `NBRC 1680`, `IFO 1680`, `DSM 3435`, `CBS 4821`, and `ATCC 22302`, with one exact project for `Go0615267` / `Gp0831616`.
- No native analysis rows join through that GOLD project.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:115263-115269`, covering `NRRL Y-5387` and `CBS 4821` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:27328`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:28689` maps side-inventory old ID `NCBITaxon:1807434` into `NCBITaxon:27328`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hit set for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:1807434` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27328`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
- GOLD aggregate rows can differ from local native exact rows; for `NCBITaxon:27328`, the generated aggregate count is `8`, while the exact native GOLD files currently contain six matching organism rows.
