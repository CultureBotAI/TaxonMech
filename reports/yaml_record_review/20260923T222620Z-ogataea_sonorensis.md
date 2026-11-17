# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_sonorensis.yaml`
- Taxon: `NCBITaxon:51926` (`Ogataea sonorensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:51926`, label `Ogataea sonorensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_sonorensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_saltuana.yaml data/taxa/eukaryota/ogataea_siamensis.yaml data/taxa/eukaryota/ogataea_sithepensis.yaml data/taxa/eukaryota/ogataea_sonorensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52851` contains the seeded identifier with reason `attested rule: Ogataea sonorensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6534` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6534` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37692`, where `NCBITaxon:51926` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705653` / `Candida sonorensis NRRL Y-7800`, linked to project `Gp0831702`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 25 culture-from-holotype rows for `Torulopsis sonorensis` covering `ATCC 32108`, `IFO 10027`, `JCM 1827`, `NCYC 855`, `NRRL Y-7800`, and `UCD 71-148`, plus 4 `CBS 6792` holotype spellings.
- Exact StrainInfo side inventory found 6 direct records and 27 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:51926`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:51926`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
