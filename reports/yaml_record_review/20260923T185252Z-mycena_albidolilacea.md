# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_albidolilacea.yaml`
- Taxon: `NCBITaxon:1033008` (`Mycena albidolilacea`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1033008`, label `Mycena albidolilacea`.
- It is grounded exactly under `NCBITaxon:41247` (`Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_albidolilacea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_albidolilacea.yaml data/taxa/eukaryota/mycena_alexandri.yaml data/taxa/eukaryota/mycena_amicta.yaml data/taxa/eukaryota/mycena_belliarum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57234` contains the seeded identifier with reason `attested rule: Mycena albidolilacea, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:220932` matches the YAML identity: parent `NCBITaxon:41247`, rank `SPECIES`, and exact synonym `Mycena albidolilacea Kuhner & Maire, 1938`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:220932` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:432`, where `NCBITaxon:1033008` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0367701` / `Mycena albidolilacea CBHHK002`, linked to native projects `Gp0208002` and `Gp0251455` and one native analysis for `Gp0208002`.

## Completeness

- Exact StrainInfo has 2 direct records and 2 deposit rows for `NCBITaxon:1033008`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:1033008`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1033008`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
