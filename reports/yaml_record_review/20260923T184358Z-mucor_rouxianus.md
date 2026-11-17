# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_rouxianus.yaml`
- Taxon: `NCBITaxon:2761406` (`Mucor rouxianus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2761406`, label `Mucor rouxianus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_rouxianus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_rouxianus.yaml ... mucor_sinensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63200` contains the seeded identifier with reason `attested rule: Mucor rouxianus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:551772` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor rouxianus Lendn., 1907`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:551772` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:26041`, where `NCBITaxon:2761406` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows for `NRRL 13036`, `NRRL 1429`, and `NRRL 1430`; those organism rows link to three native GOLD projects and no native analyses.

## Completeness

- Exact StrainInfo has 4 direct records and 6 deposit rows for `NCBITaxon:2761406`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:2761406`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:2761406`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
