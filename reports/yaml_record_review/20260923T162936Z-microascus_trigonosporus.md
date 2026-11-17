# YAML Record Review: Microascus trigonosporus

- Record: `data/taxa/eukaryota/microascus_trigonosporus.yaml`
- Reviewed: `2026-09-23T16:29:36Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:36921`
- Label: `Microascus trigonosporus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5594` (`Microascus`)

## Validation

- `just validate data/taxa/eukaryota/microascus_trigonosporus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/meyerozyma_elateridarum.yaml data/taxa/eukaryota/meyerozyma_guilliermondii.yaml data/taxa/eukaryota/meyerozyma_smithsonii.yaml data/taxa/eukaryota/microascus_trigonosporus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4191` has the same identifier, label, species rank, `NCBITaxon:5594` parent, genetic code `1`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The `Scopulariopsis trigonospora` exact synonym, `Microascaceae sp. MUT 4885`, and `Microascus trigonosporus` authority string match the NCBI row.
- The YAML lineage contains the expected 16 entries from `root` through `Microascus`.

## Evidence

- `data/seed_scope.tsv:52363` includes `NCBITaxon:36921` with reason `attested rule: Microascus trigonosporus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:33544` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- A complete exact scan of the native GOLD snapshot contains organism `Go0033164` / `CBS 218.31` and 31 direct project rows for that organism; a complete `AP PROJECT GOLD IDS` scan found no native analysis rows for those 31 projects.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:196275-196280`, covering `CBS 218.31`, `HACC 178`, and `IMI 113702` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:36921`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:22413` maps side-inventory old ID `NCBITaxon:1635067` into `NCBITaxon:36921`; no retained old-ID row was present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the large exact StrainInfo hit set for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted `NCBITaxon:1635067` old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:36921`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
