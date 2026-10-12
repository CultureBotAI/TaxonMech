# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_alpina.yaml`
- Taxon: `NCBITaxon:64518` (`Mortierella alpina`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64518`, label `Mortierella alpina`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_alpina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_alliacea.yaml ... mortierella_antarctica.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53088` contains the seeded identifier with reason `attested rule: Mortierella alpina, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8178` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonyms `Mortierella alpina Peyronel, 1913` and `Mortierella sp. JZ-157`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8178` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40321`, where `NCBITaxon:64518` has `organism_count` 28.
- Complete native GOLD expansion found 15 exact current-taxid organism rows and 16 projects, spanning strains `CCTCC M207067`, `AD021`, `AD071`, `AD072`, `AD075`, `CK1249`, `CK1268`, `GBA31`, `NRRL 66262`, `AD 266`, `FSU 9789`, `GBAus 30`, `NVP 153`, `312A_T17_1`, and `LL118`.
- Native analyses link to `Mortierella alpina CCTCC M207067` via `Gp0118032` and `Mortierella alpina LL118` via `Gp0644957`.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:64518` type-material rows.

## Completeness

- Exact StrainInfo has 43 direct records and 65 deposit rows for `NCBITaxon:64518`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64518`.
- `data/raw/ncbi_merged_ids.tsv:99135` maps retired `NCBITaxon:929673` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` row, so the retired ID is side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the large StrainInfo exact-match side inventory.

## Additional Notes

- The transformed GOLD aggregate asserts 28 organisms, while the local native exact current-taxid scan currently exposes 15 of those as organism JSONL rows.
