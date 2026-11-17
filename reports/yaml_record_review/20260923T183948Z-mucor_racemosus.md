# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_racemosus.yaml`
- Taxon: `NCBITaxon:4841` (`Mucor racemosus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:4841`, label `Mucor racemosus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_racemosus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_racemosus.yaml ... mucor_ramosissimus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51857` contains the seeded identifier with reason `attested rule: Mucor racemosus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2090` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, exact synonym `Mucor varians`, and three related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2090` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36841`, where `NCBITaxon:4841` has `organism_count` 18.
- Native GOLD has 18 exact current-taxid organism rows linked to 19 native projects and no native analyses.
- `data/raw/ncbi_type_material.tsv:221324-221340` has 17 type-material aliases covering `ATCC 22365`, `ATHUM 2885`, `BCCM/IHEM:3158`, `CBS 260.68`, `IHEM 3158`, `IP 1249.80`, `LCP 86.2552`, `MUCL 29302`, `NRRL 3640`, and their punctuation variants.

## Completeness

- Exact StrainInfo has 88 direct records and 111 deposit rows for `NCBITaxon:4841`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:4841`.
- `data/raw/ncbi_merged_ids.tsv:79412` contains side-inventory old ID `NCBITaxon:463691` merged into `NCBITaxon:4841`; the record has no `replaces` entries because no retained retired-ID rows were present in the local NCBI taxon inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
