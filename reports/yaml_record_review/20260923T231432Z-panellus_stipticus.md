# YAML Record Review

- Target: `data/taxa/eukaryota/panellus_stipticus.yaml`
- Taxon: `NCBITaxon:5636` (`Panellus stipticus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5636`, label `Panellus stipticus`.
- It is grounded exactly under `NCBITaxon:5635` (`Panellus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Panellus`.

## Validation

- `just validate data/taxa/eukaryota/panellus_stipticus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/panellus_stipticus.yaml data/taxa/eukaryota/panus_rudis.yaml data/taxa/eukaryota/papiliotrema_flavescens.yaml data/taxa/eukaryota/papiliotrema_laurentii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52050` contains the seeded identifier with reason `attested rule: Panellus stipticus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2507` matches the YAML identity: parent `NCBITaxon:5635`, rank `SPECIES`, five exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2507` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38898`, where `NCBITaxon:5636` has `organism_count` 4.
- The native GOLD exact current-taxid scan found two organism rows, four project rows, and one analysis row for `NCBITaxon:5636`; the rows cover strains `KUC8834` and `LUM`.
- Exact StrainInfo side evidence has 23 direct `NCBITaxon:5636` records and 29 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:5636`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
