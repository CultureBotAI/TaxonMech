# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_kuhlmanii.yaml`
- Taxon: `NCBITaxon:979711` (`Mortierella kuhlmanii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979711`, label `Mortierella kuhlmanii`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_kuhlmanii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_kuhlmanii.yaml ... mortierella_parazychae.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57049` contains the seeded identifier with reason `attested rule: Mortierella kuhlmanii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204262` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella kuhlmanii W. Gams, 1976`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204262` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45189`, where `NCBITaxon:979711` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583267` / `Mortierella kuhlmanii FSU 9827`, linked to project `Gp0586856`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:275883-275886` has `SZMC 11271` culture-from-type-material aliases and `CBS 157.71` type-material aliases.

## Completeness

- Exact StrainInfo has four direct records and four deposit rows for `NCBITaxon:979711`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979711`.
- `data/raw/ncbi_merged_ids.tsv:100528` carries side-inventory old ID `NCBITaxon:988180 -> NCBITaxon:979711`, but the bounded scan found no retained retired row in `data/raw/ncbitaxon_taxa.tsv`; generated `replaces` omission is consistent with local retained-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- `CBS 157.71` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella kuhlmanii FSU 9827`.
