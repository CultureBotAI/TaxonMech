# YAML Record Review

- Target: `data/taxa/eukaryota/nectriaceae_sp.yaml`
- Taxon: `NCBITaxon:1756110` (`Nectriaceae sp.`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1756110`, label `Nectriaceae sp.`.
- It is grounded exactly under `NCBITaxon:359652` (`unclassified Nectriaceae`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `unclassified Nectriaceae`.

## Validation

- `just validate data/taxa/eukaryota/nectriaceae_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nectriaceae_sp.yaml data/taxa/eukaryota/nectriopsis_sporangiicola.yaml data/taxa/eukaryota/nectriopsis_tremellicola.yaml data/taxa/eukaryota/nemania_abortiva.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61213` contains the seeded identifier with reason `attested rule: Nectriaceae sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:458293` matches the YAML identity: parent `NCBITaxon:359652`, rank `SPECIES`, no retained synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:458293` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15281`, where `NCBITaxon:1756110` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0583395` / `Nectriaceae sp. 302B_17_2` and `Go0583403` / `Nectriaceae sp. 308B_c4_1`.
- Those two native organism IDs link to four native projects and no native analyses.

## Completeness

- Exact ignored-file-inclusive scans of `data/raw/ncbi_type_material.tsv` and `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1756110`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1756110`.
- The record has no generated local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains or retained retired-ID provenance for this record.

## Additional Notes

- None.
