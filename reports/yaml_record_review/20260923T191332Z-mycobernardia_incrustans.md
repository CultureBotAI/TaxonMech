# YAML Record Review

- Target: `data/taxa/eukaryota/mycobernardia_incrustans.yaml`
- Taxon: `NCBITaxon:202708` (`Mycobernardia incrustans`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:202708`, label `Mycobernardia incrustans`.
- It is grounded exactly under `NCBITaxon:2873591` (`Mycobernardia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mycobernardia`.

## Validation

- `just validate data/taxa/eukaryota/mycobernardia_incrustans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycetophylax_conformis_symbiont_g26.yaml data/taxa/eukaryota/mycobernardia_incrustans.yaml data/taxa/eukaryota/mycocalia_denudata.yaml data/taxa/eukaryota/mycoemilia_scoparia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54467` contains the seeded identifier with reason `attested rule: Mycobernardia incrustans, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:39992` matches the YAML identity: parent `NCBITaxon:2873591`, rank `SPECIES`, one exact synonym, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:39992` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19078`, where `NCBITaxon:202708` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0357140` / `Mycobernardia incrustans CBS 104901`, linked to native projects `Gp0191684` and `Gp0306508` and one native analysis for `Gp0191684`.

## Completeness

- Exact StrainInfo has 1 direct record and 1 deposit row for `NCBITaxon:202708`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:202708`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:202708`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
