# YAML Record Review

- Target: `data/taxa/eukaryota/paramecium_sonneborni.yaml`
- Taxon: `NCBITaxon:65129` (`Paramecium sonneborni`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:65129`, label `Paramecium sonneborni`.
- It is grounded exactly under `NCBITaxon:5884` (`Paramecium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `6`.
- The YAML carries 11 lineage entries from `root` through `Paramecium`.

## Validation

- `just validate data/taxa/eukaryota/paramecium_sonneborni.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paramecium_primaurelia.yaml data/taxa/eukaryota/paramecium_sexaurelia.yaml data/taxa/eukaryota/paramecium_sonneborni.yaml data/taxa/eukaryota/paramecium_tetraurelia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53123` contains the seeded identifier with reason `attested rule: Paramecium sonneborni, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8323` matches the YAML identity: parent `NCBITaxon:5884`, rank `SPECIES`, one related synonym, genetic code `6`, and the 2026-09-13 taxonomy snapshot.
- All 11 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8323` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40480`, where `NCBITaxon:65129` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for `GCA_905182985.1`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:65129` record and one deposit.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:65129`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
