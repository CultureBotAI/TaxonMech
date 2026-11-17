# YAML Record Review

- Target: `data/taxa/eukaryota/nothofagozyma_chilensis.yaml`
- Taxon: `NCBITaxon:45538` (`Nothofagozyma chilensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:45538`, label `Nothofagozyma chilensis`.
- It is grounded exactly under `NCBITaxon:3712558` (`Nothofagozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `12`.
- The YAML carries 13 lineage entries from `root` through `Nothofagozyma`.

## Validation

- `just validate data/taxa/eukaryota/nothofagozyma_chilensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nothofagozyma_chilensis.yaml data/taxa/eukaryota/nothomitra_cinnamomea.yaml data/taxa/eukaryota/nothophoma_quercina.yaml data/taxa/eukaryota/obba_rivulosa.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52642` contains the seeded identifier with reason `attested rule: Nothofagozyma chilensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:5596` matches the YAML identity: parent `NCBITaxon:3712558`, rank `SPECIES`, exact synonym `Candida chilensis`, two related synonyms, genetic code `12`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:5596` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36048`, where `NCBITaxon:45538` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705754` / `Candida chilensis NRRL Y-17141`, linked to project `Gp0831809`; no native analysis row linked to that project.

## Completeness

- A complete exact scan of `data/raw/ncbi_type_material.tsv` found 21 `Candida chilensis` rows at lines 214979-214999, covering culture-from-holotype aliases for `ATCC 22076`, `BCRC`/`CCRC 22319`, `IFO 10408`, `JCM 1693`, `NCYC 2632`, `NRRL Y-17141`, and `NRRL Y-7790`, plus holotype aliases for `CBS 5719`.
- Exact StrainInfo side inventory found 3 direct records and 15 deposit entries, including `JCM 1693`, type-strain deposit `ATCC 22076`, `CBS 5719`, `CCRC 22319`, type-strain deposit `IFO 10408`, `CBS 5720`, and `VKM Y-2178`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:45538`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
