# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_latifolia.yaml`
- Taxon: `NCBITaxon:1033247` (`Mycena latifolia`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1033247`, label `Mycena latifolia`.
- It is grounded exactly under `NCBITaxon:41247` (`Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_latifolia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_haematopus.yaml data/taxa/eukaryota/mycena_kentingensis_nom_inval.yaml data/taxa/eukaryota/mycena_latifolia.yaml data/taxa/eukaryota/mycena_leptocephala.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57238` contains the seeded identifier with reason `attested rule: Mycena latifolia, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:220938` matches the YAML identity: parent `NCBITaxon:41247`, rank `SPECIES`, two exact synonyms, and two related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:220938` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:436`, where `NCBITaxon:1033247` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0370912` / `Mycena latifolia 10383`, linked to native projects `Gp0217298` and `Gp0251434` and one native analysis for `Gp0217298`.

## Completeness

- Exact StrainInfo has 1 direct record and 1 deposit row for `NCBITaxon:1033247`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:1033247`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1033247`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
