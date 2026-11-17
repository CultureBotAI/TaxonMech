# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_racemosus_f_racemosus.yaml`
- Taxon: `NCBITaxon:91628` (`Mucor racemosus f. racemosus`)
- Verdict: pass

## Target

- The record is the seeded forma `NCBITaxon:91628`, label `Mucor racemosus f. racemosus`.
- It is grounded exactly under `NCBITaxon:4841` (`Mucor racemosus`) with rank `FORMA`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mucor racemosus`.

## Validation

- `just validate data/taxa/eukaryota/mucor_racemosus_f_racemosus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_racemosus.yaml ... mucor_ramosissimus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53518` contains the seeded identifier with reason `attested rule: Mucor racemosus f. racemosus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14829` matches the YAML identity: parent `NCBITaxon:4841`, rank `FORMA`, no exact synonyms, and related synonym `Mucor racemosus f. racemosus Bull., 1791`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14829` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44468`, where `NCBITaxon:91628` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0402564` / `Mucor varians NRRL 1760`, linked to project `Gp0290189`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:272906-272922` has 17 type-material aliases covering `ATCC 22365`, `ATHUM 2885`, `BCCM/IHEM:3158`, `CBS 260.68`, `IHEM 3158`, `IP 1249.80`, `LCP 86.2552`, `MUCL 29302`, `NRRL 3640`, and their punctuation variants.

## Completeness

- Exact StrainInfo has 48 direct records and 60 deposit rows for `NCBITaxon:91628`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:91628`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:91628`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
