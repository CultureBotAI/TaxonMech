# YAML Record Review: Metschnikowia koreensis

- Record: `data/taxa/eukaryota/metschnikowia_koreensis.yaml`
- Reviewed: `2026-09-23T16:05:52Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:164924`
- Label: `Metschnikowia koreensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_koreensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_kamakouana.yaml data/taxa/eukaryota/metschnikowia_kipukae.yaml data/taxa/eukaryota/metschnikowia_kofuensis_nom_inval.yaml data/taxa/eukaryota/metschnikowia_koreensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:33834` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The related synonyms `Metschnikowia koreensis S.G. Hong, J. Chun, H.W. Oh & Bae, 2001` and `Metschnikowia sp. KCTC 7998` match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54211` includes `NCBITaxon:164924` with reason `attested rule: Metschnikowia koreensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14160` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0527707` / `Y137` and `Go0705159` / `CBS 8854`, with projects `Gp0456069`, `Gp0488152`, and `Gp0831182`.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:49672-49677`, covering `CBS 8854`, `KCTC 7998`, and `SG99-34` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:164924`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:164924`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:164924`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
