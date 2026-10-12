# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_lusitanicus_cbs_277_49.yaml`
- Taxon: `NCBITaxon:747725` (`Mucor lusitanicus CBS 277.49`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:747725`, label `Mucor lusitanicus CBS 277.49`.
- It is grounded exactly under `NCBITaxon:29924` (`Mucor lusitanicus`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mucor lusitanicus`.

## Validation

- `just validate data/taxa/eukaryota/mucor_lusitanicus_cbs_277_49.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_lusitanicus.yaml ... mucor_megalocarpus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56611` contains the seeded identifier with reason `attested rule: Mucor lusitanicus CBS 277.49, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:172499` matches the YAML identity: parent `NCBITaxon:29924`, rank `STRAIN`, no synonyms, and genetic code `1`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:172499` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42245`, where `NCBITaxon:747725` has `organism_count` 1.
- Exact native GOLD current-taxid scans found no organism, project, or analysis rows for `747725`; the generated GOLD attestation is limited to the transformed aggregate row.

## Completeness

- The bounded scan found no exact type-material, BacDive, StrainInfo, generated raw strain, generated StrainInfo, or auxiliary source rows for `NCBITaxon:747725`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:747725`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if additional GOLD rows are transformed into exact native current-taxid evidence for `NCBITaxon:747725`.

## Additional Notes

- None.
