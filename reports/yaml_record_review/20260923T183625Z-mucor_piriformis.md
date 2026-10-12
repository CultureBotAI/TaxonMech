# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_piriformis.yaml`
- Taxon: `NCBITaxon:105697` (`Mucor piriformis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:105697`, label `Mucor piriformis`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_piriformis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_philippovii_nom_inval.yaml ... mucor_plumbeus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53696` contains the seeded identifier with reason `attested rule: Mucor piriformis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:18957` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:18957` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1066`, where `NCBITaxon:105697` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0411511` / `Mucor piriformis NRRL 3318` and `Go0470790` / `Mucor piriformis NRRL 3637`, linked to two native projects and no native analyses.
- `data/raw/ncbi_type_material.tsv:3662-3663` has the `CBS 169.25` and `CBS:169.25` culture-from-neotype aliases.

## Completeness

- Exact StrainInfo has 40 direct records and 66 deposit rows for `NCBITaxon:105697`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:105697`.
- `data/raw/ncbi_merged_ids.tsv:7287` contains side-inventory old ID `NCBITaxon:1196558` merged into `NCBITaxon:105697`; the record has no `replaces` entries because no retained retired-ID rows were present in the local NCBI taxon inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
