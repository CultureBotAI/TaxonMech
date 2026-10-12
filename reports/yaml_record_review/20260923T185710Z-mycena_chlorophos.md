# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_chlorophos.yaml`
- Taxon: `NCBITaxon:658473` (`Mycena chlorophos`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:658473`, label `Mycena chlorophos`.
- It is grounded exactly under `NCBITaxon:41247` (`Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_chlorophos.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_capillaripes.yaml data/taxa/eukaryota/mycena_chlorophos.yaml data/taxa/eukaryota/mycena_citricolor.yaml data/taxa/eukaryota/mycena_crocata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56294` contains the seeded identifier with reason `attested rule: Mycena chlorophos, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:152371` matches the YAML identity: parent `NCBITaxon:41247`, rank `SPECIES`, one exact synonym, and two related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:152371` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40624`, where `NCBITaxon:658473` has `organism_count` 1.
- Native GOLD has two exact current-taxid organism rows, `Go0144093` / `Mycena chlorophos` and `Go0632079` / `Mycena chlorophos 110903Hualien_Pintung`, linked to native projects `Gp0149686` and `Gp0645900` and two native analyses.

## Completeness

- Exact StrainInfo has 2 direct records and 3 deposit rows for `NCBITaxon:658473`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:658473`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:658473`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
