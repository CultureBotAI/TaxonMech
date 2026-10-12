# YAML Record Review: Mixia osmundae

- Record: `data/taxa/eukaryota/mixia_osmundae.yaml`
- Reviewed: `2026-09-23T16:51:19Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:34349`
- Label: `Mixia osmundae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:34348` (`Mixia`)

## Validation

- `just validate data/taxa/eukaryota/mixia_osmundae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/minutocellus_polymorphus.yaml data/taxa/eukaryota/mitosporidium_daphniae.yaml data/taxa/eukaryota/mixia_osmundae.yaml data/taxa/eukaryota/modicella_reniformis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:3824` has the same identifier, label, species rank, `NCBITaxon:34348` parent, genetic code `1`, two exact synonyms, three related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Phytoceratiomyxa osmundae` and `Taphrina osmundae` as exact synonyms and preserves the `Mixia`, `Phytoceratiomyxa`, and `Taphrina` authority strings as related synonyms from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Mixia`.

## Evidence

- `curation/seed_scope.tsv:52268` includes `NCBITaxon:34349` with reason `attested rule: Mixia osmundae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:32843` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism evidence for `Go0010141` / `IAM 14324`, with three native GOLD projects and three native GOLD analyses linked to that organism.
- A complete `rg --no-ignore --hidden` scan found four NCBI reference-material rows at `data/raw/ncbi_type_material.tsv:188376-188379`, covering `AFTOL-ID 1773` and `JCM 22182` aliases under the `Taphrina osmundae` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:34349` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:34349`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the four `AFTOL-ID 1773` and `JCM 22182` aliases remain grouped as reference material.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:34349`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
