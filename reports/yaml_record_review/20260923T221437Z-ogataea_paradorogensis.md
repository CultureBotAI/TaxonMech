# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_paradorogensis.yaml`
- Taxon: `NCBITaxon:529654` (`Ogataea paradorogensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:529654`, label `Ogataea paradorogensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_paradorogensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_nonfermentans.yaml data/taxa/eukaryota/ogataea_ortonii.yaml data/taxa/eukaryota/ogataea_ovalis.yaml data/taxa/eukaryota/ogataea_paradorogensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55918` contains the seeded identifier with reason `attested rule: Ogataea paradorogensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:120562` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:120562` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38009`, where `NCBITaxon:529654` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0704983` / `Ogataea paradorogensis CBS 10978`, linked to project `Gp0831000`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to seven `Ogataea paradorogensis` culture-from-holotype and type-material rows for `NBRC 100261`, `CBS 10978`, and `NRRL Y-63813`.
- Exact NCBI merged-ID, BacDive, StrainInfo, generated strain, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:529654`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
