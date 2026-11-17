# YAML Record Review

- Target: `data/taxa/eukaryota/nigrograna_mackinnonii.yaml`
- Taxon: `NCBITaxon:1489893` (`Nigrograna mackinnonii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1489893`, label `Nigrograna mackinnonii`.
- It is grounded exactly under `NCBITaxon:1234310` (`Nigrograna`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nigrograna`.

## Validation

- `just validate data/taxa/eukaryota/nigrograna_mackinnonii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nidularia_deformis.yaml data/taxa/eukaryota/niesslia_exilis.yaml data/taxa/eukaryota/niesslia_gamsii.yaml data/taxa/eukaryota/nigrograna_mackinnonii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60266` contains the seeded identifier with reason `attested rule: Nigrograna mackinnonii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:381449` matches the YAML identity: parent `NCBITaxon:1234310`, rank `SPECIES`, two exact synonyms, five related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:381449` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11545`, where `NCBITaxon:1489893` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0039092` / `Nigrograna mackinnonii E5202H`, linked to project `Gp0039092` and one native analysis for that project.

## Completeness

- `data/raw/ncbi_type_material.tsv:35741-35744` has culture-from-holotype spellings for `CBS 674.75` and `CBS:674.75`, plus type-material spellings for `FMC 270` and `FMC:270`, under `Pyrenochaeta mackinnonii`.
- Exact StrainInfo side inventory found 2 direct records and 2 deposit entries: `CBS 110022` and `CBS 674.75`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1278233` and `NCBITaxon:798132` into `NCBITaxon:1489893`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:1489893`; the record correctly has `strain_count: 0`.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
