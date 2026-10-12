# YAML Record Review: Metschnikowia corniflorae

- Record: `data/taxa/eukaryota/metschnikowia_corniflorae.yaml`
- Reviewed: `2026-09-23T15:58:33Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:280591`
- Label: `Metschnikowia corniflorae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_corniflorae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_corniflorae.yaml data/taxa/eukaryota/metschnikowia_cubensis.yaml data/taxa/eukaryota/metschnikowia_dekortorum.yaml data/taxa/eukaryota/metschnikowia_drakensbergensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:57092` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The two related synonyms, `Metschnikowia corniflorae N.H. Nguyen, S.O. Suh, Erbil & M. Blackw., 2006` and `Metschnikowia sp. NRRL Y-27750`, match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54958` includes `NCBITaxon:280591` with reason `attested rule: Metschnikowia corniflorae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:26894` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project pair for `Metschnikowia corniflorae NRRL Y-27750`: `Go0705493` and `Gp0831536`; no linked native GOLD analysis row was found.
- A complete `rg --no-ignore --hidden` scan found 10 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:124671-124680`, covering `NRRL Y-27750`, `NRRL Y-22750`, and `CBS 9905` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:280591`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the ten type-material spellings remain grouped as source aliases.
- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether `Go0705493` should become a concrete `NRRL Y-27750` strain or remain aggregate evidence only.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:280591`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
