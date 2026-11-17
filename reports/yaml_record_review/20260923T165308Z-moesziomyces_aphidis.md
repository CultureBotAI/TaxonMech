# YAML Record Review: Moesziomyces aphidis

- Record: `data/taxa/eukaryota/moesziomyces_aphidis.yaml`
- Reviewed: `2026-09-23T16:53:08Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:84754`
- Label: `Moesziomyces aphidis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:63261` (`Moesziomyces`)

## Validation

- `just validate data/taxa/eukaryota/moesziomyces_aphidis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/moelleriella_libera.yaml data/taxa/eukaryota/moesziomyces_antarcticus.yaml data/taxa/eukaryota/moesziomyces_aphidis.yaml data/taxa/eukaryota/mollisia_scopiformis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:13065` has the same identifier, label, species rank, `NCBITaxon:63261` parent, genetic code `1`, three exact synonyms, four related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves the `Moesziomyces`, `Pseudozyma`, and `Sterigmatomyces` synonym set from the NCBI exact and related synonym fields.
- The YAML lineage contains the expected 12 entries from `root` through `Moesziomyces`.

## Evidence

- `curation/seed_scope.tsv:53414` includes `NCBITaxon:84754` with reason `attested rule: Moesziomyces aphidis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:43200` reports GOLD organism count `5`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot currently has four exact organism rows for `ATCC 32657`, `CBS 6821`, `NRRL Y-7954`, and `St-0401`, with no linked native GOLD project or analysis rows.
- A complete `rg --no-ignore --hidden` scan found 16 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:267890-267905`, covering `CBS 517.83`, `DSM 70725`, `JCM 10318`, and `MUCL 30674` aliases under the `Sterigmatomyces aphidis` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:84754` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:14474` redirects `NCBITaxon:1391700` into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Reconcile the transformed GOLD aggregate count of 5 with the four exact native GOLD organism rows on the next GOLD refresh.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:84754`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
