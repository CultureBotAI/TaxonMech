# YAML Record Review

- Target: `data/taxa/eukaryota/mycocalia_denudata.yaml`
- Taxon: `NCBITaxon:404356` (`Mycocalia denudata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:404356`, label `Mycocalia denudata`.
- It is grounded exactly under `NCBITaxon:404355` (`Mycocalia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycocalia`.

## Validation

- `just validate data/taxa/eukaryota/mycocalia_denudata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycetophylax_conformis_symbiont_g26.yaml data/taxa/eukaryota/mycobernardia_incrustans.yaml data/taxa/eukaryota/mycocalia_denudata.yaml data/taxa/eukaryota/mycoemilia_scoparia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55531` contains the seeded identifier with reason `attested rule: Mycocalia denudata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:86890` matches the YAML identity: parent `NCBITaxon:404355`, rank `SPECIES`, one exact synonym, and two related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:86890` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34541`, where `NCBITaxon:404356` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0551226` / `Mycocalia denudata CBS 494.85` and `Go0580406` / `Mycocalia denudata Canada CBS 494.85`, linked to two native projects and no native analyses.

## Completeness

- Exact StrainInfo has 2 direct records and 2 deposit rows for `NCBITaxon:404356`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:404356`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:404356`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
