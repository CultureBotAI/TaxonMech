# YAML Record Review: Metarhizium robertsii ARSEF 23

- Record: `data/taxa/eukaryota/metarhizium_robertsii_arsef_23.yaml`
- Reviewed: `2026-09-23T15:40:44Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:655844`
- Label: `Metarhizium robertsii ARSEF 23`
- Rank/domain: `STRAIN` / `EUKARYOTA`
- Parent: `NCBITaxon:568076` (`Metarhizium robertsii`)

## Validation

- `just validate data/taxa/eukaryota/metarhizium_robertsii_arsef_23.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_pingshaense.yaml data/taxa/eukaryota/metarhizium_rileyi.yaml data/taxa/eukaryota/metarhizium_robertsii.yaml data/taxa/eukaryota/metarhizium_robertsii_arsef_23.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:151714` has the same identifier, label, strain rank, `NCBITaxon:568076` parent, genetic code `1`, empty synonym fields, and `gold` attestation copied into the YAML.
- The YAML lineage contains the expected 17 entries from `root` through parent species `Metarhizium robertsii`.
- The species-level parent is also present as `data/taxa/eukaryota/metarhizium_robertsii.yaml`, so this strain is represented as its own exact seeded taxon.

## Evidence

- `data/seed_scope.tsv:56256` includes `NCBITaxon:655844` with reason `attested rule: Metarhizium robertsii ARSEF 23, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:40557` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project/analysis chain for `Metarhizium anisopliae var. anisopliae ARSEF 23`: `Go0006292`, `Gp0006292`, strain `ARSEF 23`.
- The bounded scan found no NCBI type-material rows for this exact strain taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:655844`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether `Go0006292` should stay as GOLD aggregate evidence or become a concrete `ARSEF 23` strain attached to this exact taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:655844`.
