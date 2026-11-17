# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_corticola.yaml`
- Taxon: `NCBITaxon:1969505` (`Mucor corticola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1969505`, label `Mucor corticola`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_corticola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_circinelloides.yaml ... mucor_durus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61767` contains the seeded identifier with reason `attested rule: Mucor corticola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:505689` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact synonym `Mucor corticolus`, and related synonym `Mucor corticola Hagem, 1910`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:505689` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:18164`, where `NCBITaxon:1969505` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0470811` / `Mucor corticolus NRRL A-16258`, linked to project `Gp0345299`; no native analysis row linked to that project.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:1969505` type-material rows.

## Completeness

- Exact StrainInfo has one direct record and one deposit row for `NCBITaxon:1969505`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1969505`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1969505`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- Native GOLD uses the synonym-bearing organism name `Mucor corticolus NRRL A-16258`, which is compatible with the NCBI exact synonym `Mucor corticolus`.
