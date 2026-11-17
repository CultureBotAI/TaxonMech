# YAML Record Review

- Target: `data/taxa/eukaryota/myxozyma_neglecta.yaml`
- Taxon: `NCBITaxon:383838` (`Myxozyma neglecta`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:383838`, label `Myxozyma neglecta`.
- It is grounded exactly under `NCBITaxon:54096` (`Myxozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Myxozyma`.

## Validation

- `just validate data/taxa/eukaryota/myxozyma_neglecta.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_neglecta.yaml data/taxa/eukaryota/myxozyma_neotropica.yaml data/taxa/eukaryota/myxozyma_nipponensis.yaml data/taxa/eukaryota/myxozyma_sirexii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55453` contains the seeded identifier with reason `attested rule: Myxozyma neglecta, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:80593` matches the YAML identity: parent `NCBITaxon:54096`, rank `SPECIES`, and related synonym `Myxozyma neglecta Spaaij, Van der Walt & G. Weber, 1998`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:80593` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33971`, where `NCBITaxon:383838` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705438` / `Myxozyma neglecta NRRL Y-27508`, linked to project `Gp0831481` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 14 type-material rows for `NCBITaxon:383838`, covering variants of `ATCC 52277`, `CBS 7058`, `JCM 5197`, and `NRRL Y-27508`.
- Exact StrainInfo has 1 direct record and 5 deposit rows for `NCBITaxon:383838`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:383838`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:383838`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
