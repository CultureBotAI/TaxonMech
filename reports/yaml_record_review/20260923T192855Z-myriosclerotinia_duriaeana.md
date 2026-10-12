# YAML Record Review

- Target: `data/taxa/eukaryota/myriosclerotinia_duriaeana.yaml`
- Taxon: `NCBITaxon:108355` (`Myriosclerotinia duriaeana`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:108355`, label `Myriosclerotinia duriaeana`.
- It is grounded exactly under `NCBITaxon:38442` (`Myriosclerotinia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Myriosclerotinia`.

## Validation

- `just validate data/taxa/eukaryota/myriosclerotinia_duriaeana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myriosclerotinia_curreyana.yaml data/taxa/eukaryota/myriosclerotinia_duriaeana.yaml data/taxa/eukaryota/myriosclerotinia_scirpicola.yaml data/taxa/eukaryota/myrothecium_inundatum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53728` contains the seeded identifier with reason `attested rule: Myriosclerotinia duriaeana, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:19605` matches the YAML identity: parent `NCBITaxon:38442`, rank `SPECIES`, exact synonym `Peziza duriaeana`, and related synonyms `Myriosclerotinia duriaeana (Tul. & C. Tul.) N.F. Buchw., 1947` and `Peziza duriaeana Tul. & C. Tul., 1865`.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:19605` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1539`, where `NCBITaxon:108355` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0384661` / `Myriosclerotinia duriaeana LMK 746`, linked to project `Gp0235775` and one native analysis for `Myriosclerotinia duriaeana LMK 746`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:108355`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:108355`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:108355`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains or exact type-material side inventories.

## Additional Notes

- None.
