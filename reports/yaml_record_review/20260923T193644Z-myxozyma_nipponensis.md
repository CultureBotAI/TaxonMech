# YAML Record Review

- Target: `data/taxa/eukaryota/myxozyma_nipponensis.yaml`
- Taxon: `NCBITaxon:383839` (`Myxozyma nipponensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:383839`, label `Myxozyma nipponensis`.
- It is grounded exactly under `NCBITaxon:54096` (`Myxozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Myxozyma`.

## Validation

- `just validate data/taxa/eukaryota/myxozyma_nipponensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_neglecta.yaml data/taxa/eukaryota/myxozyma_neotropica.yaml data/taxa/eukaryota/myxozyma_nipponensis.yaml data/taxa/eukaryota/myxozyma_sirexii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55454` contains the seeded identifier with reason `attested rule: Myxozyma nipponensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:80594` matches the YAML identity: parent `NCBITaxon:54096`, rank `SPECIES`, and related synonym `Myxozyma nipponensis Spaaij & G. Weber, 1993`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:80594` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33972`, where `NCBITaxon:383839` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705463` / `Myxozyma nipponensis NRRL Y-27625`, linked to project `Gp0831506` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 9 culture-from-holotype rows for `NCBITaxon:383839`, covering variants of `NRRL Y-27625` and `UOFS Y-2051`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:383839`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:383839`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories.

## Additional Notes

- None.
