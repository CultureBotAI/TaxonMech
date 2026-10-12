# YAML Record Review

- Target: `data/taxa/eukaryota/nematocida_displodere.yaml`
- Taxon: `NCBITaxon:1805483` (`Nematocida displodere`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1805483`, label `Nematocida displodere`.
- It is grounded exactly under `NCBITaxon:586132` (`Nematocida`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Nematocida`.

## Validation

- `just validate data/taxa/eukaryota/nematocida_displodere.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nematocida_displodere.yaml data/taxa/eukaryota/nematocida_ironsii.yaml data/taxa/eukaryota/nematodospora_anomalae.yaml data/taxa/eukaryota/nematodospora_valgi.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61288` contains the seeded identifier with reason `attested rule: Nematocida displodere, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:471693` matches the YAML identity: parent `NCBITaxon:586132`, rank `SPECIES`, two related synonyms, and genetic code `1`.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:471693` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15886`, where `NCBITaxon:1805483` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0144240` / `Nematocida displodere JUm2807`.
- That native organism ID links to project `Gp0149837`, which has one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1805483`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1805483`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:1805483`.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this taxon.

## Additional Notes

- None.
