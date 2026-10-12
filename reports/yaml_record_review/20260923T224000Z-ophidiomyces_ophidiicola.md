# YAML Record Review

- Target: `data/taxa/eukaryota/ophidiomyces_ophidiicola.yaml`
- Taxon: `NCBITaxon:1387563` (`Ophidiomyces ophidiicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1387563`, label `Ophidiomyces ophidiicola`.
- It is grounded exactly under `NCBITaxon:1387562` (`Ophidiomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Ophidiomyces`.

## Validation

- `just validate data/taxa/eukaryota/ophidiomyces_ophidiicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/opeltia_flavorubescens.yaml data/taxa/eukaryota/operculomyces_laminatus.yaml data/taxa/eukaryota/ophidiomyces_ophidiicola.yaml data/taxa/eukaryota/ophiobolus_disseminans.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59809` contains the seeded identifier with reason `attested rule: Ophidiomyces ophidiicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:339450` matches the YAML identity: parent `NCBITaxon:1387562`, rank `SPECIES`, two exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:339450` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9170`, where `NCBITaxon:1387563` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0384208` / `Ophidiomyces ophidiicola MYCO-ARIZ AN0400001`, linked to project `Gp0235298` and one analysis row via that project.

## Completeness

- Exact NCBI type material has 2 `CBS 122913` culture-from-holotype rows for `Chrysosporium ophidiicola`.
- Exact StrainInfo side inventory found 1 direct record and 2 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:1387563`.
- Exact NCBI merged-ID side inventory maps old `NCBITaxon:536880` to `NCBITaxon:1387563`, while BacDive, retained retired old-ID, and checked auxiliary source rows were empty; the record correctly has no `replaces` entry and `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, native GOLD, or NCBI merged-ID side inventories.

## Additional Notes

- None.
