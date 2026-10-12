# YAML Record Review

- Target: `data/taxa/eukaryota/mycoemilia_scoparia.yaml`
- Taxon: `NCBITaxon:417184` (`Mycoemilia scoparia`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:417184`, label `Mycoemilia scoparia`.
- It is grounded exactly under `NCBITaxon:417183` (`Mycoemilia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mycoemilia`.

## Validation

- `just validate data/taxa/eukaryota/mycoemilia_scoparia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycetophylax_conformis_symbiont_g26.yaml data/taxa/eukaryota/mycobernardia_incrustans.yaml data/taxa/eukaryota/mycocalia_denudata.yaml data/taxa/eukaryota/mycoemilia_scoparia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55576` contains the seeded identifier with reason `attested rule: Mycoemilia scoparia, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:91291` matches the YAML identity: parent `NCBITaxon:417183`, rank `SPECIES`, and related synonym `Mycoemilia scoparia Kurihara, Degawa & Tokum., 2004`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:91291` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34919`, where `NCBITaxon:417184` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0515254` / `Mycoemilia scoparia NBRC 100468`, linked to native project `Gp0436022` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 7 type-material rows for `NCBITaxon:417184`, covering 4 culture-from-holotype rows and 3 holotype rows.
- Exact StrainInfo has 1 direct record and 2 deposit rows for `NCBITaxon:417184`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:417184`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:417184`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
