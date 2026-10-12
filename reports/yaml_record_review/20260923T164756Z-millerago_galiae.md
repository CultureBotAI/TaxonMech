# YAML Record Review: Millerago galiae

- Record: `data/taxa/eukaryota/millerago_galiae.yaml`
- Reviewed: `2026-09-23T16:47:56Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:3379938`
- Label: `Millerago galiae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:3379936` (`Millerago`)

## Validation

- `just validate data/taxa/eukaryota/millerago_galiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/millerago_galiae.yaml data/taxa/eukaryota/millerozyma_acaciae.yaml data/taxa/eukaryota/millerozyma_farinosa.yaml data/taxa/eukaryota/millerozyma_farinosa_cbs_7064.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:623343` has the same identifier, label, species rank, `NCBITaxon:3379936` parent, genetic code `1`, exact synonym, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Candida galis` as an exact synonym and preserves the `Candida` and 2024 `Millerago galiae` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Millerago`.

## Evidence

- `curation/seed_scope.tsv:63606` includes `NCBITaxon:3379938` with reason `attested rule: Millerago galiae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:32539` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0705522` / `NRRL Y-48037` / `Gp0831565`; no native GOLD analysis rows are linked to that project ID.
- A complete `rg --no-ignore --hidden` scan found five NCBI type-material rows at `data/raw/ncbi_type_material.tsv:181779-181783`, covering `CBS 8842` holotype aliases and the `UWO(PS) 00-159.2` isotype.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and one exact deposit row for `NCBITaxon:3379938`, but no corresponding local strain inventory row is generated.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:18751` redirects `NCBITaxon:152264` into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the four `CBS 8842` spellings and the `UWO(PS) 00-159.2` isotype remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:3379938`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
