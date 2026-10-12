# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_bainieri.yaml`
- Taxon: `NCBITaxon:1095379` (`Mucor bainieri`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1095379`, label `Mucor bainieri`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_bainieri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_bainieri.yaml ... mucor_circinatus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57613` contains the seeded identifier with reason `attested rule: Mucor bainieri, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:235546` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact synonym `Circinomucor bainieri`, and related synonyms `Mucor bainieri B.S. Mehrotra & Baijal, 1963` and `Mucor sp. LW-2017c`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:235546` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1757`, where `NCBITaxon:1095379` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0535977` / `Mucor bainieri NRRL 2988`, linked to project `Gp0484455`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:6135-6136` has the `CBS 293.63` and `CBS:293.63` culture-from-isotype aliases.

## Completeness

- Exact StrainInfo has two direct records and nine deposit rows for `NCBITaxon:1095379`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1095379`.
- `data/raw/ncbi_merged_ids.tsv:35105` maps side-inventory old ID `NCBITaxon:2021225` into this current taxon, but the retained retired-row inventory is empty, so the YAML's empty `replaces` list is consistent with local `replaces` provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The native GOLD culture collection ID is `NRRL 2988`, while the NCBI type-material evidence for this target is the `CBS 293.63` isotype culture pair.
