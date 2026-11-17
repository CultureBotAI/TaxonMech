# YAML Record Review

- Target: `data/taxa/eukaryota/pandora_neoaphidis.yaml`
- Taxon: `NCBITaxon:76017` (`Pandora neoaphidis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:76017`, label `Pandora neoaphidis`.
- It is grounded exactly under `NCBITaxon:76016` (`Pandora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Pandora`.

## Validation

- `just validate data/taxa/eukaryota/pandora_neoaphidis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/palpitomonas_bilix.yaml data/taxa/eukaryota/panaeolus_cyanescens.yaml data/taxa/eukaryota/panaeolus_papilionaceus.yaml data/taxa/eukaryota/pandora_neoaphidis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53289` contains the seeded identifier with reason `attested rule: Pandora neoaphidis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10895` matches the YAML identity: parent `NCBITaxon:76016`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10895` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42459`, where `NCBITaxon:76017` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:76017`.
- Exact StrainInfo side evidence has three direct `NCBITaxon:76017` records and four deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:76017`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
