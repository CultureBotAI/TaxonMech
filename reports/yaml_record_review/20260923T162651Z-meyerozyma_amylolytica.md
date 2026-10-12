# YAML Record Review: Meyerozyma amylolytica

- Record: `data/taxa/eukaryota/meyerozyma_amylolytica.yaml`
- Reviewed: `2026-09-23T16:26:51Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2039224`
- Label: `Meyerozyma amylolytica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766728` (`Meyerozyma`)

## Validation

- `just validate data/taxa/eukaryota/meyerozyma_amylolytica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/meyerozyma_amylolytica.yaml data/taxa/eukaryota/meyerozyma_athensensis.yaml data/taxa/eukaryota/meyerozyma_caribbica.yaml data/taxa/eukaryota/meyerozyma_carpophila.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:513022` has the same identifier, label, species rank, `NCBITaxon:766728` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The two `Meyerozyma amylolytica` authority strings plus `Candida sp. NCAIM Y.01955` and `Meyerozyma sp. NCAIM Y.02179` provisional-name synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Meyerozyma`.

## Evidence

- `data/seed_scope.tsv:62133` includes `NCBITaxon:2039224` with reason `attested rule: Meyerozyma amylolytica, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:19302` reports GOLD organism count `4`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism evidence for `Go0616530` / `NCAIM Y.02140`, `Go0616531` / `MUCL 56454`, `Go0616532` / `DSM 27310`, and `Go0616533` / `AY700`; no native project or analysis rows join to those organism rows.
- A complete `rg --no-ignore --hidden` scan found five NCBI type-material rows at `data/raw/ncbi_type_material.tsv:80139-80143`, covering `MUCL 56454`, `NCAIM Y.02140`, and `DSM 27310` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:2039224`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:92788` maps side-inventory old ID `NCBITaxon:697918` into `NCBITaxon:2039224`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the five type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact `MUCL 56454` / `DSM 27310` StrainInfo deposit for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:697918` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2039224`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
