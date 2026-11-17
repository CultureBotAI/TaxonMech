# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_ramosissimus.yaml`
- Taxon: `NCBITaxon:90264` (`Mucor ramosissimus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:90264`, label `Mucor ramosissimus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_ramosissimus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_racemosus.yaml ... mucor_ramosissimus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53500` contains the seeded identifier with reason `attested rule: Mucor ramosissimus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14504` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor ramosissimus Samouts., 1927`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14504` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44109`, where `NCBITaxon:90264` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0456313` / `Mucor ramosissimus NRRL 3042` and `Go0527640` / `Mucor ramosissimus NRRL A-11829`, linked to two native projects and no native analyses.
- `data/raw/ncbi_type_material.tsv:271849-271850` has the `CBS 135.65` and `CBS:135.65` culture-from-neotype aliases.

## Completeness

- Exact StrainInfo has 2 direct records and 10 deposit rows for `NCBITaxon:90264`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:90264`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:90264`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
