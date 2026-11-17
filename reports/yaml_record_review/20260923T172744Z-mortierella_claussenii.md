# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_claussenii.yaml`
- Taxon: `NCBITaxon:1343614` (`Mortierella claussenii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1343614`, label `Mortierella claussenii`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_claussenii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_claussenii.yaml ... mortierella_hygrophila.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59582` contains the seeded identifier with reason `attested rule: Mortierella claussenii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:322898` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella claussenii Linnem., 1958`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:322898` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:8376`, where `NCBITaxon:1343614` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0368132` / `Mortierella claussenii NRRL 2760`, linked to project `Gp0209170`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:24349-24350` has two syntype aliases, `CBS 294.59` and `CBS:294.59`.

## Completeness

- Exact StrainInfo has three direct records and four deposit rows for `NCBITaxon:1343614`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1343614`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1343614`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The native GOLD row, the NCBI syntype alias, and a StrainInfo deposit all reference CBS/NRRL-style local strain identifiers without producing generated local strain rows.
