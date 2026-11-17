# YAML Record Review

- Target: `data/taxa/eukaryota/naematelia_encephala.yaml`
- Taxon: `NCBITaxon:71784` (`Naematelia encephala`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:71784`, label `Naematelia encephala`.
- It is grounded exactly under `NCBITaxon:1910899` (`Naematelia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Naematelia`.

## Validation

- `just validate data/taxa/eukaryota/naematelia_encephala.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naegleria_lovaniensis.yaml data/taxa/eukaryota/naematelia_encephala.yaml data/taxa/eukaryota/naganishia_albida.yaml data/taxa/eukaryota/naganishia_friedmannii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53222` contains the seeded identifier with reason `attested rule: Naematelia encephala, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10051` matches the YAML identity: parent `NCBITaxon:1910899`, rank `SPECIES`, exact synonym `Tremella encephala`, and two related synonyms.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10051` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41931`, where `NCBITaxon:71784` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0112321` / `Naematelia encephala UCDFST 68-887.2`, linked to projects `Gp0114585` and `Gp0114586`; both native analyses link through `Gp0114585`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for `NCBITaxon:71784`, under synonym name `Tremella encephala` and covering `CBS 8207` variants.
- Exact StrainInfo side inventory has 9 direct rows and 26 deposit entries for `NCBITaxon:71784`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:71784`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
