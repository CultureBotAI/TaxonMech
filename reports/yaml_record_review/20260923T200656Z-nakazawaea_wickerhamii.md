# YAML Record Review

- Target: `data/taxa/eukaryota/nakazawaea_wickerhamii.yaml`
- Taxon: `NCBITaxon:1538186` (`Nakazawaea wickerhamii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1538186`, label `Nakazawaea wickerhamii`.
- It is grounded exactly under `NCBITaxon:460521` (`Nakazawaea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `26`.
- The YAML carries 13 lineage entries from `root` through `Nakazawaea`.

## Validation

- `just validate data/taxa/eukaryota/nakazawaea_wickerhamii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakazawaea_siamensis.yaml data/taxa/eukaryota/nakazawaea_wickerhamii.yaml data/taxa/eukaryota/nakazawaea_wyomingensis.yaml data/taxa/eukaryota/nannochloropsis_gaditana.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60428` contains the seeded identifier with reason `attested rule: Nakazawaea wickerhamii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:396335` matches the YAML identity: parent `NCBITaxon:460521`, rank `SPECIES`, exact synonyms `Candida wickerhamii` and `Torulopsis wickerhamii`, two related synonyms, and genetic code `26`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:396335` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12235`, where `NCBITaxon:1538186` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0519923` / `Nakazawaea wickerhamii NRRL Y-2563`, linked to projects `Gp0444093` and `Gp0780259`.
- Native GOLD has two analyses for `Nakazawaea wickerhamii NRRL Y-2563`, linked through those two project IDs.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 14 type-material rows for `NCBITaxon:1538186`, covering variants of `ATCC 36540`, `BCRC 21495`, `CBS 2928`, `CCRC 21495`, `IFO 10322`, `JCM 9568`, and `NRRL Y-2563`.
- Exact StrainInfo side inventory has 7 direct rows and 28 deposit entries for `NCBITaxon:1538186`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:35521`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.
