# YAML Record Review: Metschnikowia matae

- Record: `data/taxa/eukaryota/metschnikowia_matae.yaml`
- Reviewed: `2026-09-23T16:11:17Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1697385`
- Label: `Metschnikowia matae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_matae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_matae.yaml data/taxa/eukaryota/metschnikowia_matae_var_maris.yaml data/taxa/eukaryota/metschnikowia_matae_var_matae.yaml data/taxa/eukaryota/metschnikowia_mauinuiana.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:441933` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The related synonym `Metschnikowia matae A.R.O. Santos, C.A. Rosa & Lachance, 2015` matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:61033` includes `NCBITaxon:1697385` with reason `attested rule: Metschnikowia matae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14642` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count` and `Records filed directly under this taxon; descendant taxa are not gathered` note.
- The native GOLD snapshot contains exact direct organism/project evidence for `Go0705594` / `NRRL Y-63736` and `Go0705595` / `NRRL Y-63737`, with projects `Gp0831638` and `Gp0831639`.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:53059-53065`, covering `UFMG-CM-Y395T`, `CBS 13986`, and `NRRL Y-63736` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1697385`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven parent-level type-material spellings remain grouped as source aliases.
- If parent-level GOLD expansion starts gathering descendant rows, revisit the direct-only GOLD count against both varietas child records.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1697385`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
