# YAML Record Review: Microsporum canis

- Record: `data/taxa/eukaryota/microsporum_canis.yaml`
- Reviewed: `2026-09-23T16:44:24Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:63405`
- Label: `Microsporum canis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:34392` (`Microsporum`)

## Validation

- `just validate data/taxa/eukaryota/microsporum_canis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microscypha_sp.yaml data/taxa/eukaryota/microsporum_canis.yaml data/taxa/eukaryota/microstoma_floccosum.yaml data/taxa/eukaryota/microstroma_glucosiphilum.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7972` has the same identifier, label, species rank, `NCBITaxon:34392` parent, genetic code `1`, three exact synonyms, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML preserves `Arthroderma otae`, its authority string, and `Nannizzia otae` as exact synonyms, with `Microsporum canis E. Bodin ex Gueg., 1902` and `Nannizzia otae A. Haseg. & Usui 1974` as related synonyms.
- The YAML lineage contains the expected 15 entries from `root` through `Microsporum`.

## Evidence

- `curation/seed_scope.tsv:53056` includes `NCBITaxon:63405` with reason `attested rule: Microsporum canis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:40100` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains the exact organism/project/analysis triplets for `BMU 08102`, `BMU 08359`, and `BMU 11032`.
- A complete `rg --no-ignore --hidden` scan found two NCBI type-material rows at `data/raw/ncbi_type_material.tsv:243232-243233`, covering `CBS 496.86` neotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:63405` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:70598` and `:96210` redirect `NCBITaxon:34394` and `NCBITaxon:82078` into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If the generator starts materializing StrainInfo-only fungal records, re-check the 301 direct and 327 deposit-level native StrainInfo hits for `NCBITaxon:63405` against the expected local-strain policy.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:63405`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
