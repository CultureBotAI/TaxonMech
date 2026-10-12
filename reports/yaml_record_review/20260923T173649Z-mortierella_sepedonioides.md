# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_sepedonioides.yaml`
- Taxon: `NCBITaxon:2789355` (`Mortierella sepedonioides`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2789355`, label `Mortierella sepedonioides`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_sepedonioides.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_rishikesha.yaml ... mortierella_sepedonioides.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63240` contains the seeded identifier with reason `attested rule: Mortierella sepedonioides, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:555405` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella sepedonioides Linnem., 1941`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:555405` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:26584`, where `NCBITaxon:2789355` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0368141` / `Mortierella sepedonioides NRRL 6425`, linked to project `Gp0484331`; no native analysis row linked to that project.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:2789355` type-material rows.

## Completeness

- Exact StrainInfo has no direct `NCBITaxon:2789355` record and one exact deposit-side match, `ATCC 42664` on `siID` 155758; no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows were present.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:2789355`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:2789355`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The bounded scan fully covered the native GOLD evidence for this target.
