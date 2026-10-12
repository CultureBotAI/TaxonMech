# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_laxorrhizus.yaml`
- Taxon: `NCBITaxon:1196536` (`Mucor laxorrhizus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1196536`, label `Mucor laxorrhizus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_laxorrhizus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_intermedius.yaml ... mucor_laxorrhizus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58292` contains the seeded identifier with reason `attested rule: Mucor laxorrhizus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:269148` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor laxorrhizus Y. Ling, 1930`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:269148` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4740`, where `NCBITaxon:1196536` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0456298` / `Mucor laxorrhizus NRRL 2814`, linked to project `Gp0325308`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:12972-12973` has the `CBS 143.85` and `CBS:143.85` culture-from-neotype aliases.

## Completeness

- Exact StrainInfo has 12 direct records and 18 deposit rows for `NCBITaxon:1196536`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1196536`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1196536`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
