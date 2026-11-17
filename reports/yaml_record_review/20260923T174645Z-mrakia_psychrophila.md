# YAML Record Review

- Target: `data/taxa/eukaryota/mrakia_psychrophila.yaml`
- Taxon: `NCBITaxon:72568` (`Mrakia psychrophila`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:72568`, label `Mrakia psychrophila`.
- It is grounded exactly under `NCBITaxon:29901` (`Mrakia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mrakia`.

## Validation

- `just validate data/taxa/eukaryota/mrakia_psychrophila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mrakia_cryoconiti.yaml ... mrakia_psychrophila.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53245` contains the seeded identifier with reason `attested rule: Mrakia psychrophila, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10146` matches the YAML identity: parent `NCBITaxon:29901`, rank `SPECIES`, no exact synonyms, and both related synonyms represented in YAML.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10146` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42016`, where `NCBITaxon:72568` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0384831` / `Mrakia psychrophila NN053900`, linked to project `Gp0235960` and one native analysis row, `Mrakia psychrophila NN053900`.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:72568` type-material rows.

## Completeness

- Exact StrainInfo has two direct records and two deposit rows for `NCBITaxon:72568`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:72568`.
- `data/raw/ncbi_merged_ids.tsv:62487` carries side-inventory old ID `NCBITaxon:307566 -> NCBITaxon:72568`, but the bounded scan found no retained retired row in `data/raw/ncbitaxon_taxa.tsv`; generated `replaces` omission is consistent with local retained-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The single native GOLD analysis row links through `AP PROJECT GOLD IDS` to the exact native project `Gp0235960`.
