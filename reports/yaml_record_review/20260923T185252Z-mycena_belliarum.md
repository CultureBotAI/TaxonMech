# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_belliarum.yaml`
- Taxon: `NCBITaxon:1033014` (`Mycena belliarum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1033014`, label `Mycena belliarum`.
- It is grounded exactly under `NCBITaxon:41247` (`Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_belliarum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_albidolilacea.yaml data/taxa/eukaryota/mycena_alexandri.yaml data/taxa/eukaryota/mycena_amicta.yaml data/taxa/eukaryota/mycena_belliarum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57235` contains the seeded identifier with reason `attested rule: Mycena belliarum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:220933` matches the YAML identity: parent `NCBITaxon:41247`, rank `SPECIES`, three exact synonyms, and the related synonym `reed bonnet`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:220933` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:433`, where `NCBITaxon:1033014` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0302581` / `Mycena belliae CBHHK173m`, linked to native projects `Gp0157073` and `Gp0197056` and one native analysis for `Gp0157073`.

## Completeness

- Exact StrainInfo has 2 direct records and 0 deposit rows for `NCBITaxon:1033014`; it has no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:1033014`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1033014`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The native GOLD organism row spells the organism as `Mycena belliae CBHHK173m`, but it carries the exact current NCBI taxid `1033014` and therefore still backs the generated GOLD assertion for `NCBITaxon:1033014`.
