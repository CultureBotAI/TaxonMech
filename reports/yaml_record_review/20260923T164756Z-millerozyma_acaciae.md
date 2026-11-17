# YAML Record Review: Millerozyma acaciae

- Record: `data/taxa/eukaryota/millerozyma_acaciae.yaml`
- Reviewed: `2026-09-23T16:47:56Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:28986`
- Label: `Millerozyma acaciae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766502` (`Millerozyma`)

## Validation

- `just validate data/taxa/eukaryota/millerozyma_acaciae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/millerago_galiae.yaml data/taxa/eukaryota/millerozyma_acaciae.yaml data/taxa/eukaryota/millerozyma_farinosa.yaml data/taxa/eukaryota/millerozyma_farinosa_cbs_7064.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2996` has the same identifier, label, species rank, `NCBITaxon:766502` parent, yeast genetic code `12`, two exact synonyms, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Pichia acaciae` and `Yamadazyma acaciae` as exact synonyms and preserves the `Millerozyma` and `Pichia` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Millerozyma`.

## Evidence

- `curation/seed_scope.tsv:52184` includes `NCBITaxon:28986` with reason `attested rule: Millerozyma acaciae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:28263` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0145222` / `JCM 10732` and `Go0705617` / `NRRL Y-7117`, with one native GOLD analysis linked to `Gp0150861`.
- A complete `rg --no-ignore --hidden` scan found 14 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:138050-138063`, covering `ATCC 22303`, `BCRC 22439`, `CBS 5656`, `CCRC 22439`, `CSIR Y-448`, `IFO 1681`, and `NRRL Y-7117` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:28986` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:28986`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 14 culture-collection spellings remain grouped as aliases of the same NCBI type-material set.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:28986`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
