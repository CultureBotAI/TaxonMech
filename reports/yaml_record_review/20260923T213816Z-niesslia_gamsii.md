# YAML Record Review

- Target: `data/taxa/eukaryota/niesslia_gamsii.yaml`
- Taxon: `NCBITaxon:2052550` (`Niesslia gamsii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2052550`, label `Niesslia gamsii`.
- It is grounded exactly under `NCBITaxon:267679` (`Niesslia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Niesslia`.

## Validation

- `just validate data/taxa/eukaryota/niesslia_gamsii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nidularia_deformis.yaml data/taxa/eukaryota/niesslia_exilis.yaml data/taxa/eukaryota/niesslia_gamsii.yaml data/taxa/eukaryota/nigrograna_mackinnonii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62206` contains the seeded identifier with reason `attested rule: Niesslia gamsii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:513985` matches the YAML identity: parent `NCBITaxon:267679`, rank `SPECIES`, exact synonym `Monocillium gamsii`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:513985` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19544`, where `NCBITaxon:2052550` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0621403` / `Monocillium gamsii DSM 105458` and `Go0621404` / `Monocillium gamsii 25DP-SE-SA`; no native project or analysis rows linked to those organisms.

## Completeness

- A complete exact scan of `data/raw/ncbi_type_material.tsv` found six rows at lines 81235-81240: culture-from-holotype spellings for `DSM 105458`, `DSM-105458`, `DSM105458`, and `DSM:105458`, plus type-material spellings for `B 70 0016491` and `B:70 0016491`.
- Exact StrainInfo side inventory found 4 direct records and 4 deposit entries: `DSM 105460`, `DSM 105461`, `DSM 105459`, and type-strain deposit `DSM 105458`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:2052550`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
