# YAML Record Review

- Target: `data/taxa/eukaryota/naegleria_lovaniensis.yaml`
- Taxon: `NCBITaxon:51637` (`Naegleria lovaniensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:51637`, label `Naegleria lovaniensis`.
- It is grounded exactly under `NCBITaxon:5761` (`Naegleria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Naegleria`.

## Validation

- `just validate data/taxa/eukaryota/naegleria_lovaniensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naegleria_lovaniensis.yaml data/taxa/eukaryota/naematelia_encephala.yaml data/taxa/eukaryota/naganishia_albida.yaml data/taxa/eukaryota/naganishia_friedmannii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52833` contains the seeded identifier with reason `attested rule: Naegleria lovaniensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6478` matches the YAML identity: parent `NCBITaxon:5761`, rank `SPECIES`, and no synonyms.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6478` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37621`, where `NCBITaxon:51637` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0574229` / `Naegleria lovaniensis ATCC 30569`, linked to project `Gp0548920` and one native analysis.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:51637`.
- Exact StrainInfo side inventory has 3 direct rows and 3 deposit entries for `NCBITaxon:51637`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:51637`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
