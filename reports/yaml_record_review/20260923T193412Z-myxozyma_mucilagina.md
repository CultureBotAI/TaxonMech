# YAML Record Review

- Target: `data/taxa/eukaryota/myxozyma_mucilagina.yaml`
- Taxon: `NCBITaxon:58630` (`Myxozyma mucilagina`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:58630`, label `Myxozyma mucilagina`.
- It is grounded exactly under `NCBITaxon:54096` (`Myxozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Myxozyma`.

## Validation

- `just validate data/taxa/eukaryota/myxozyma_mucilagina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_lipomycoides.yaml data/taxa/eukaryota/myxozyma_melibiosi.yaml data/taxa/eukaryota/myxozyma_monticola.yaml data/taxa/eukaryota/myxozyma_mucilagina.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52990` contains the seeded identifier with reason `attested rule: Myxozyma mucilagina, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:7423` matches the YAML identity: parent `NCBITaxon:54096`, rank `SPECIES`, exact synonym `Candida mucilagina`, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:7423` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39514`, where `NCBITaxon:58630` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705718` / `Myxozyma mucilagina yHDO354`, linked to project `Gp0831773` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 16 type-material rows for `NCBITaxon:58630`, all under `Candida mucilagina` and covering variants of `ATCC 42174`, `BCRC 22183`, `CCRC 22183`, `CBS 7071`, `JCM 1834`, `NRRL Y-11823`, `UCD 76-236.3`, and `UCD 76-236C`.
- Exact StrainInfo has 6 direct records and 21 deposit rows for `NCBITaxon:58630`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:58630`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:58630`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
