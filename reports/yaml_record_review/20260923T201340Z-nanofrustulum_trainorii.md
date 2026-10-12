# YAML Record Review

- Target: `data/taxa/eukaryota/nanofrustulum_trainorii.yaml`
- Taxon: `NCBITaxon:3687704` (`Nanofrustulum trainorii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:3687704`, label `Nanofrustulum trainorii`.
- It is grounded exactly under `NCBITaxon:210601` (`Nanofrustulum`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Nanofrustulum`.

## Validation

- `just validate data/taxa/eukaryota/nanofrustulum_trainorii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nanofrustulum_trainorii.yaml data/taxa/eukaryota/naohidea_sebacea.yaml data/taxa/eukaryota/naohidea_sebacea_cbs_8477.yaml data/taxa/eukaryota/naumovozyma_baii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63691` contains the seeded identifier with reason `attested rule: Nanofrustulum trainorii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:641550` matches the YAML identity: parent `NCBITaxon:210601`, rank `SPECIES`, exact synonym `Pseudostaurosira trainorii`, two related synonyms, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:641550` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33532`, where `NCBITaxon:3687704` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0690944` / `Nanofrustulum trainorii DCG 0449`.
- A complete exact native GOLD project join found 7 transcriptome projects for `Go0690944`, `Gp0798025` through `Gp0798031`, and no native analyses.

## Completeness

- Exact ignored-file-inclusive scans of `data/raw/ncbi_type_material.tsv` and `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:3687704`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:3687704`.
- The record has no generated local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains or retained retired-ID provenance for this record.

## Additional Notes

- None.
