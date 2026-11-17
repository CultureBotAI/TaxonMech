# YAML Record Review

- Target: `data/taxa/eukaryota/panaeolus_cyanescens.yaml`
- Taxon: `NCBITaxon:181874` (`Panaeolus cyanescens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:181874`, label `Panaeolus cyanescens`.
- It is grounded exactly under `NCBITaxon:71684` (`Panaeolus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Panaeolus`.

## Validation

- `just validate data/taxa/eukaryota/panaeolus_cyanescens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/palpitomonas_bilix.yaml data/taxa/eukaryota/panaeolus_cyanescens.yaml data/taxa/eukaryota/panaeolus_papilionaceus.yaml data/taxa/eukaryota/pandora_neoaphidis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54361` contains the seeded identifier with reason `attested rule: Panaeolus cyanescens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:36428` matches the YAML identity: parent `NCBITaxon:71684`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:36428` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:16132`, where `NCBITaxon:181874` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0632195` / `Panaeolus cyanescens 2629`, linked to project `Gp0646035` and one analysis row via that project.
- Exact StrainInfo side evidence has three direct `NCBITaxon:181874` records and four deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:181874`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD or StrainInfo side inventories.

## Additional Notes

- None.
