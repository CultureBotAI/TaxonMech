# YAML Record Review

- Target: `data/taxa/eukaryota/myrothecium_inundatum.yaml`
- Taxon: `NCBITaxon:110576` (`Myrothecium inundatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:110576`, label `Myrothecium inundatum`.
- It is grounded exactly under `NCBITaxon:5531` (`Myrothecium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Myrothecium`.

## Validation

- `just validate data/taxa/eukaryota/myrothecium_inundatum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myriosclerotinia_curreyana.yaml data/taxa/eukaryota/myriosclerotinia_duriaeana.yaml data/taxa/eukaryota/myriosclerotinia_scirpicola.yaml data/taxa/eukaryota/myrothecium_inundatum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53770` contains the seeded identifier with reason `attested rule: Myrothecium inundatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:19922` matches the YAML identity: parent `NCBITaxon:5531`, rank `SPECIES`, and related synonym `Myrothecium inundatum Tode, 1790`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:19922` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1957`, where `NCBITaxon:110576` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0036288` / `Myrothecium inundatum CBS 120646`, linked to projects `Gp0036288` and `Gp0036289` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 4 culture-from-epitype rows for `NCBITaxon:110576`, covering `CBS 275.48` and `IMI 008983`.
- Exact StrainInfo has 10 direct records and 12 deposit rows for `NCBITaxon:110576`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:110576`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:110576`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- The transformed GOLD aggregate has one more organism assertion than the 1 exact local native GOLD organism row for this current taxid.
