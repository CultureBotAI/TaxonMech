# YAML Record Review: Moesziomyces antarcticus

- Record: `data/taxa/eukaryota/moesziomyces_antarcticus.yaml`
- Reviewed: `2026-09-23T16:53:08Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:84753`
- Label: `Moesziomyces antarcticus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:63261` (`Moesziomyces`)

## Validation

- `just validate data/taxa/eukaryota/moesziomyces_antarcticus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/moelleriella_libera.yaml data/taxa/eukaryota/moesziomyces_antarcticus.yaml data/taxa/eukaryota/moesziomyces_aphidis.yaml data/taxa/eukaryota/mollisia_scopiformis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:13064` has the same identifier, label, species rank, `NCBITaxon:63261` parent, genetic code `1`, five exact synonyms, one related synonym, and `gold` attestation copied into the YAML.
- The YAML preserves `Candida antarctica`, `Moesziomyces antarcticus`, `Pseudozyma antarctica`, `Sporobolomyces antarcticus`, and `Trichosporon oryzae` as exact synonyms from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Moesziomyces`.

## Evidence

- `curation/seed_scope.tsv:53413` includes `NCBITaxon:84753` with reason `attested rule: Moesziomyces antarcticus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:43199` reports GOLD organism count `4`, matching the YAML GOLD `assertion_count`.
- The native GOLD JSONL snapshot currently has three exact organism/project/analysis chains for `T-34`, `JCM 10317`, and `ATCC 34888`.
- A complete `rg --no-ignore --hidden` scan found 29 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:267861-267889`, covering the `Sporobolomyces antarcticus` type-material alias cluster.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:84753` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:70558` and `:86053` redirect `NCBITaxon:34362` and `NCBITaxon:5555` into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Reconcile the transformed GOLD aggregate count of 4 with the three exact native GOLD organism rows on the next GOLD refresh.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:84753`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
