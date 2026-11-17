# YAML Record Review

- Target: `data/taxa/eukaryota/multiclavula_mucida.yaml`
- Taxon: `NCBITaxon:40107` (`Multiclavula mucida`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:40107`, label `Multiclavula mucida`.
- It is grounded exactly under `NCBITaxon:40106` (`Multiclavula`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Multiclavula`.

## Validation

- `just validate data/taxa/eukaryota/multiclavula_mucida.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_zychae.yaml ... mutinus_elegans.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52416` contains the seeded identifier with reason `attested rule: Multiclavula mucida, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4556` matches the YAML identity: parent `NCBITaxon:40106`, rank `SPECIES`, exact synonym `Clavaria mucida`, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4556` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34459`, where `NCBITaxon:40107` has `organism_count` 1.
- Exact native GOLD current-taxid scans found no organism, project, or analysis rows for `40107`; the generated GOLD attestation is limited to the transformed aggregate row.

## Completeness

- Exact StrainInfo has 1 direct record and 1 deposit row for `NCBITaxon:40107`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:40107`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:40107`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if native GOLD current-taxid rows are transformed for `NCBITaxon:40107`.

## Additional Notes

- None.
