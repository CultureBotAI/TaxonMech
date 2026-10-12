# YAML Record Review

- Target: `data/taxa/eukaryota/pachysolen_tannophilus.yaml`
- Taxon: `NCBITaxon:4918` (`Pachysolen tannophilus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:4918`, label `Pachysolen tannophilus`.
- It is grounded exactly under `NCBITaxon:4917` (`Pachysolen`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `26`.
- The YAML carries 13 lineage entries from `root` through `Pachysolen`.

## Validation

- `just validate data/taxa/eukaryota/pachysolen_tannophilus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/pachysolen_tannophilus.yaml data/taxa/eukaryota/paecilomyces_fulvus.yaml data/taxa/eukaryota/paecilomyces_sp.yaml data/taxa/eukaryota/paecilomyces_sp_m2901.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51875` contains the seeded identifier with reason `attested rule: Pachysolen tannophilus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2139` matches the YAML identity: parent `NCBITaxon:4917`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `26`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2139` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37118`, where `NCBITaxon:4918` has `organism_count` 8.
- Native GOLD has eight exact current-taxid organism rows and no linked projects or analysis rows for `NCBITaxon:4918`.
- Exact StrainInfo side evidence has 30 direct `NCBITaxon:4918` records and 86 deposits across those records.

## Completeness

- Exact NCBI type material has 18 rows for `NCBITaxon:4918`, covering paired or colonized variants across ATCC, BCRC, CBS, CCRC, DBVPG, IMI, MUCL, NCYC, and NRRL designations.
- Exact BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:4918`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, native GOLD, or StrainInfo side inventories.

## Additional Notes

- None.
