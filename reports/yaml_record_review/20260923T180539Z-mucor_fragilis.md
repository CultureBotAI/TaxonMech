# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_fragilis.yaml`
- Taxon: `NCBITaxon:64491` (`Mucor fragilis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64491`, label `Mucor fragilis`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_fragilis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_exponens.yaml ... mucor_fragilis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53077` contains the seeded identifier with reason `attested rule: Mucor fragilis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8164` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonyms `Mucor fragilis Bainier, 1884`, `Mucor sp. AH-2011b`, and `Mucor sp. AH-2011c`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8164` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40303`, where `NCBITaxon:64491` has `organism_count` 5.
- Native GOLD has five exact current-taxid organism rows, `Go0456302`, `Go0470848`, `Go0527563`, `Go0527571`, and `Go0527610`, linked to five projects; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:64491` type-material rows.

## Completeness

- Exact StrainInfo has 18 direct records and 27 deposit rows for `NCBITaxon:64491`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64491`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1091292` and `NCBITaxon:1091293` into this current taxon.
- The bounded retained-row scan found no local retired-ID provenance, so the YAML's empty `replaces` list is consistent.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
