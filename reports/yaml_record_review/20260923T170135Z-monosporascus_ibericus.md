# YAML Record Review: Monosporascus ibericus

- Record: `data/taxa/eukaryota/monosporascus_ibericus.yaml`
- Reviewed: `2026-09-23T17:01:35Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:155417`
- Label: `Monosporascus ibericus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:155415` (`Monosporascus`)

## Validation

- `just validate data/taxa/eukaryota/monosporascus_ibericus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/monosiga_ovata.yaml data/taxa/eukaryota/monosporascus_cannonballus.yaml data/taxa/eukaryota/monosporascus_ibericus.yaml data/taxa/eukaryota/monosporozyma_aerobia.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:32224` has the same identifier, label, species rank, `NCBITaxon:155415` parent, genetic code `1`, related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Monosporascus ibericus Collado, Ant. Gonzalez, Stchigel, Guarro & Pelaez, 2002` as a related synonym from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Monosporascus`.

## Evidence

- `curation/seed_scope.tsv:54112` includes `NCBITaxon:155417` with reason `attested rule: Monosporascus ibericus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:12442` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot has one exact organism row, `Go0518018` for `Monosporascus ibericus CBS 110550`, one linked project row, `Gp0442085`, and one linked native analysis.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:42082-42087`, covering `AG224`, `CBS 110550`, and `MA Fungi 48050` culture-from-holotype or holotype aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and one exact deposit row for `NCBITaxon:155417`, but it is not represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:155417`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:155417`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
