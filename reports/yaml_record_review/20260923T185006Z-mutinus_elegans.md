# YAML Record Review

- Target: `data/taxa/eukaryota/mutinus_elegans.yaml`
- Taxon: `NCBITaxon:288524` (`Mutinus elegans`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:288524`, label `Mutinus elegans`.
- It is grounded exactly under `NCBITaxon:90952` (`Mutinus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mutinus`.

## Validation

- `just validate data/taxa/eukaryota/mutinus_elegans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_zychae.yaml ... mutinus_elegans.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55006` contains the seeded identifier with reason `attested rule: Mutinus elegans, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:58940` matches the YAML identity: parent `NCBITaxon:90952`, rank `SPECIES`, two exact synonyms, and three related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:58940` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:28104`, where `NCBITaxon:288524` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0036295` / `Mutinus elegans ME.BST`, linked to two native projects and no native analyses.

## Completeness

- Exact StrainInfo has 1 direct record and 1 deposit row for `NCBITaxon:288524`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:288524`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:288524`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
