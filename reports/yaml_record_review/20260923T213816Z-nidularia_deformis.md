# YAML Record Review

- Target: `data/taxa/eukaryota/nidularia_deformis.yaml`
- Taxon: `NCBITaxon:566112` (`Nidularia deformis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:566112`, label `Nidularia deformis`.
- It is grounded exactly under `NCBITaxon:440094` (`Nidularia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Nidularia`.

## Validation

- `just validate data/taxa/eukaryota/nidularia_deformis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nidularia_deformis.yaml data/taxa/eukaryota/niesslia_exilis.yaml data/taxa/eukaryota/niesslia_gamsii.yaml data/taxa/eukaryota/nigrograna_mackinnonii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56058` contains the seeded identifier with reason `attested rule: Nidularia deformis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:133550` matches the YAML identity: parent `NCBITaxon:440094`, rank `SPECIES`, exact synonym `Cyathus deformis`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:133550` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39001`, where `NCBITaxon:566112` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0551227` / `Nidularia deformis CBS 156.42`, linked to project `Gp0502588`; no native analysis row linked to that project.

## Completeness

- The bounded exact scan found no NCBI type-material rows, no exact StrainInfo rows, and no NCBI merged-ID side rows for `NCBITaxon:566112`; no retained retired old-ID rows were present either.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:566112`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact native GOLD organism and project rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
