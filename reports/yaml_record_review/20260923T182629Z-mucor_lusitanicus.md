# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_lusitanicus.yaml`
- Taxon: `NCBITaxon:29924` (`Mucor lusitanicus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:29924`, label `Mucor lusitanicus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_lusitanicus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_lusitanicus.yaml ... mucor_megalocarpus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52233` contains the seeded identifier with reason `attested rule: Mucor lusitanicus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:3310` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, three exact synonyms, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:3310` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:29987`, where `NCBITaxon:29924` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows: `Go0017712` / `Mucor lusitanicus CBS 277.49`, `Go0446219` / `Mucor lusitanicus MU402`, and `Go0535983` / `Mucor circinelloides f.lusitanicus NRRL 3631`.
- Those GOLD organism rows link to eight native projects and three native analyses through project IDs `Gp0017712`, `Gp0019319`, and `Gp0312513`.
- `data/raw/ncbi_type_material.tsv:153488-153489` has the `CBS 108.17` and `CBS:108.17` culture-from-type-material aliases.

## Completeness

- Exact StrainInfo has 23 direct records and 35 deposit rows for `NCBITaxon:29924`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:29924`.
- `data/raw/ncbi_merged_ids.tsv:3316` contains side-inventory old ID `NCBITaxon:1095375` merged into `NCBITaxon:29924`; the record has no `replaces` entries because no retained retired-ID rows were present in the local NCBI taxon inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
