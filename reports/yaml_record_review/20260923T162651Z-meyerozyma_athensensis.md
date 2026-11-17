# YAML Record Review: Meyerozyma athensensis

- Record: `data/taxa/eukaryota/meyerozyma_athensensis.yaml`
- Reviewed: `2026-09-23T16:26:51Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:304220`
- Label: `Meyerozyma athensensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766728` (`Meyerozyma`)

## Validation

- `just validate data/taxa/eukaryota/meyerozyma_athensensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/meyerozyma_amylolytica.yaml data/taxa/eukaryota/meyerozyma_athensensis.yaml data/taxa/eukaryota/meyerozyma_caribbica.yaml data/taxa/eukaryota/meyerozyma_carpophila.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:62156` has the same identifier, label, species rank, `NCBITaxon:766728` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The `Candida athensensis` exact synonym, three provisional Candida strain-name synonyms, and Meyerozyma recombination authority string match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Meyerozyma`.

## Evidence

- `data/seed_scope.tsv:55096` includes `NCBITaxon:304220` with reason `attested rule: Meyerozyma athensensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:30517` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism evidence for `Go0517168` / `NRRL Y-27644`, with two project rows, `Gp0441206` and `Gp0780266`, and two native analysis rows linked through those project IDs.
- A complete `rg --no-ignore --hidden` scan found ten NCBI type-material rows at `data/raw/ncbi_type_material.tsv:159116-159125`, covering `ATCC MYA-4324`, `BG02-5-23-003I-4`, `CBS 9840`, and `NRRL Y-27644` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:304220`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1148564`, `NCBITaxon:234575`, `NCBITaxon:261688`, and `NCBITaxon:261689` into `NCBITaxon:304220`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the ten type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the three exact StrainInfo hits for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the four omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:304220`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
