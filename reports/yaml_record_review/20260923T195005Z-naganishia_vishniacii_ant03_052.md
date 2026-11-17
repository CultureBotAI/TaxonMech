# YAML Record Review

- Target: `data/taxa/eukaryota/naganishia_vishniacii_ant03_052.yaml`
- Taxon: `NCBITaxon:1314774` (`Naganishia vishniacii ANT03-052`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1314774`, label `Naganishia vishniacii ANT03-052`.
- It is grounded exactly under `NCBITaxon:89929` (`Naganishia vishniacii`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Naganishia vishniacii`.

## Validation

- `just validate data/taxa/eukaryota/naganishia_vishniacii_ant03_052.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naganishia_vishniacii.yaml data/taxa/eukaryota/naganishia_vishniacii_ant03_052.yaml data/taxa/eukaryota/nakaseomyces_bracarensis.yaml data/taxa/eukaryota/nakaseomyces_bracarensis_cbs_10154.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59384` contains the seeded identifier with reason `attested rule: Naganishia vishniacii ANT03-052, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:312644` matches the YAML identity: parent `NCBITaxon:89929`, rank `STRAIN`, and exact synonym `Cryptococcus vishniacii ANT03-052`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:312644` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7695`, where `NCBITaxon:1314774` has `organism_count` 1.
- The local native GOLD exact-current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1314774`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1314774`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1314774`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1314774`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local native GOLD or strain rows for this strain taxon.

## Additional Notes

- The generated GOLD assertion count follows transformed `data/raw/gold_organisms.tsv`; the local native `ANT03-052` GOLD organism row is keyed to species `NCBITaxon:89929`, not this strain taxon.
