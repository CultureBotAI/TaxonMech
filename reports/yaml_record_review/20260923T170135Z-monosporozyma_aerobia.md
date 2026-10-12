# YAML Record Review: Monosporozyma aerobia

- Record: `data/taxa/eukaryota/monosporozyma_aerobia.yaml`
- Reviewed: `2026-09-23T17:01:35Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:271218`
- Label: `Monosporozyma aerobia`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3162981` (`Monosporozyma`)

## Validation

- `just validate data/taxa/eukaryota/monosporozyma_aerobia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosiga_ovata.yaml data/taxa/eukaryota/monosporascus_cannonballus.yaml data/taxa/eukaryota/monosporascus_ibericus.yaml data/taxa/eukaryota/monosporozyma_aerobia.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:56025` has the same identifier, label, species rank, `NCBITaxon:3162981` parent, genetic code `1`, exact synonym, related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Kazachstania aerobia F.Y. Bai & Y.M. Cai, 2004` as an exact synonym and `Monosporozyma aerobia (F.Y. Bai & Y.M. Cai) Q.M. Wang, Yurkov & Boekhout, 2024` as a related synonym from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Monosporozyma`.

## Evidence

- `curation/seed_scope.tsv:54916` includes `NCBITaxon:271218` with reason `attested rule: Monosporozyma aerobia, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25122` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0517023` for `Kazachstania aerobia NRRL Y-27976`, one linked project row, `Gp0441061`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found nine NCBI type-material rows at `data/raw/ncbi_type_material.tsv:112498-112506`, covering `AS 2.2384`, `CBS 9918`, `CGMCC 2.2384`, and `NRRL Y-27976` aliases under the `Kazachstania aerobia` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has two exact direct rows and five exact deposit-bearing rows for `NCBITaxon:271218`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:271218`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:271218`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
