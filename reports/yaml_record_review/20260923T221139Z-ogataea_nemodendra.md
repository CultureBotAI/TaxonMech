# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_nemodendra.yaml`
- Taxon: `NCBITaxon:51932` (`Ogataea nemodendra`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:51932`, label `Ogataea nemodendra`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_nemodendra.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_nakhonphanomensis.yaml data/taxa/eukaryota/ogataea_nemodendra.yaml data/taxa/eukaryota/ogataea_neopini.yaml data/taxa/eukaryota/ogataea_nitratoaversa.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52854` contains the seeded identifier with reason `attested rule: Ogataea nemodendra, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6537` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6537` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37696`, where `NCBITaxon:51932` has `organism_count` 6.
- Native GOLD has 6 exact current-taxid organism rows for `NCBITaxon:51932` and one project, `Gp0831693`, linked through the `Candida nemodendra NRRL Y-7779` organism row; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to 13 `Torulopsis nemodendra` culture-from-holotype and holotype rows for `ATCC 36593`, `IFO 10299`, `JCM 9855`, `NRRL Y-7779`, and `CBS 6280`.
- Exact StrainInfo side inventory found 3 direct records and 15 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:51932`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:51932`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
