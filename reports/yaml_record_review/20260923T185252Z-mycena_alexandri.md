# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_alexandri.yaml`
- Taxon: `NCBITaxon:1745969` (`Mycena alexandri`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1745969`, label `Mycena alexandri`.
- It is grounded exactly under `NCBITaxon:41247` (`Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_alexandri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_albidolilacea.yaml data/taxa/eukaryota/mycena_alexandri.yaml data/taxa/eukaryota/mycena_amicta.yaml data/taxa/eukaryota/mycena_belliarum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61192` contains the seeded identifier with reason `attested rule: Mycena alexandri, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:455799` matches the YAML identity: parent `NCBITaxon:41247`, rank `SPECIES`, and related synonym `Mycena alexandri Singer, 1962`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:455799` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15178`, where `NCBITaxon:1745969` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0373436` / `Mycena alexandri CBHHK200`, linked to native projects `Gp0220537` and `Gp0251431` and one native analysis for `Gp0220537`.

## Completeness

- Exact StrainInfo has 1 direct record and 1 deposit row for `NCBITaxon:1745969`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:1745969`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1745969`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
