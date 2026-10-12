# YAML Record Review

- Target: `data/taxa/eukaryota/naohidea_sebacea.yaml`
- Taxon: `NCBITaxon:112072` (`Naohidea sebacea`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:112072`, label `Naohidea sebacea`.
- It is grounded exactly under `NCBITaxon:112071` (`Naohidea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Naohidea`.

## Validation

- `just validate data/taxa/eukaryota/naohidea_sebacea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nanofrustulum_trainorii.yaml data/taxa/eukaryota/naohidea_sebacea.yaml data/taxa/eukaryota/naohidea_sebacea_cbs_8477.yaml data/taxa/eukaryota/naumovozyma_baii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53779` contains the seeded identifier with reason `attested rule: Naohidea sebacea, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:20391` matches the YAML identity: parent `NCBITaxon:112071`, rank `SPECIES`, exact synonym `Dacrymyces sebaceus`, two related synonyms, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:20391` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:2153`, where `NCBITaxon:112072` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0036592` / `Naohidea sebacea CBS 8477 (P95)`, linked to projects `Gp0036591` and `Gp0036592`, and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 4 reference-material rows for `NCBITaxon:112072`, covering variants of `AFTOL-ID 1761` and `CBS 8477`.
- Exact StrainInfo side inventory has 1 direct row and 1 deposit entry for `NCBITaxon:112072`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows redirecting old IDs into `NCBITaxon:112072`, matching the absent `replaces` list.
- The GOLD attestation explicitly covers records filed directly under `NCBITaxon:112072`; descendant taxa are not gathered, matching the attestation note.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
