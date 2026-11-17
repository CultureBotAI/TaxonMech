# YAML Record Review

- Target: `data/taxa/eukaryota/paraeutypella_vitis.yaml`
- Taxon: `NCBITaxon:140563` (`Paraeutypella vitis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:140563`, label `Paraeutypella vitis`.
- It is grounded exactly under `NCBITaxon:2962501` (`Paraeutypella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Paraeutypella`.

## Validation

- `just validate data/taxa/eukaryota/paraeutypella_vitis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paracorniculantispora_psalliotae.yaml data/taxa/eukaryota/paraeutypella_vitis.yaml data/taxa/eukaryota/parafenestella_ontariensis.yaml data/taxa/eukaryota/paraglomus_brasilianum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54012` contains the seeded identifier with reason `attested rule: Paraeutypella vitis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:28450` matches the YAML identity: parent `NCBITaxon:2962501`, rank `SPECIES`, two exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:28450` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9647`, where `NCBITaxon:140563` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:140563`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:140563` record and one deposit.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:140563`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
