# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_chonburiensis.yaml`
- Taxon: `NCBITaxon:447320` (`Ogataea chonburiensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:447320`, label `Ogataea chonburiensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_chonburiensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_angusta.yaml data/taxa/eukaryota/ogataea_arabinofermentans.yaml data/taxa/eukaryota/ogataea_chonburiensis.yaml data/taxa/eukaryota/ogataea_corticis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55682` contains the seeded identifier with reason `attested rule: Ogataea chonburiensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:99560` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:99560` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:35766`, where `NCBITaxon:447320` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0704953` / `Ogataea chonburiensis CBS 10363`, linked to project `Gp0830969`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to 13 `Ogataea chonburiensis` culture-from-holotype and holotype designations for `ATCC MYA-4462`, `CBS 10363`, `NBRC 101965`, `BCC<THA> 21227`, and `PT44`.
- Exact NCBI merged-ID, BacDive, StrainInfo, generated strain, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:447320`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
