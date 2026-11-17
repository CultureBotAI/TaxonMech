# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_vitilis.yaml`
- Taxon: `NCBITaxon:1033281` (`Mycena vitilis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1033281`, label `Mycena vitilis`.
- It is grounded exactly under `NCBITaxon:41247` (`Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_vitilis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_sanguinolenta.yaml data/taxa/eukaryota/mycena_venus.yaml data/taxa/eukaryota/mycena_vitilis.yaml data/taxa/eukaryota/mycena_vulgaris.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57241` contains the seeded identifier with reason `attested rule: Mycena vitilis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:220942` matches the YAML identity: parent `NCBITaxon:41247`, rank `SPECIES`, one exact synonym, and three related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:220942` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:439`, where `NCBITaxon:1033281` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0367702` / `Mycena vitilis CBHHK169m`, linked to native projects `Gp0208003` and `Gp0251454` and one native analysis for `Gp0208003`.

## Completeness

- Exact StrainInfo has 1 direct record and 1 deposit row for `NCBITaxon:1033281`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:1033281`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1033281`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
