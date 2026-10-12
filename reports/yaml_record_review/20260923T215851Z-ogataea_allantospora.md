# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_allantospora.yaml`
- Taxon: `NCBITaxon:434199` (`Ogataea allantospora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:434199`, label `Ogataea allantospora`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_allantospora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/oculimacula_yallundae.yaml data/taxa/eukaryota/odontella_aurita.yaml data/taxa/eukaryota/oehlia_diaphana.yaml data/taxa/eukaryota/ogataea_allantospora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55645` contains the seeded identifier with reason `attested rule: Ogataea allantospora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:95821` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:95821` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:35388`, where `NCBITaxon:434199` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705534` / `Ogataea allantospora NRRL Y-48267`, linked to project `Gp0831577`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to six designations for the same type set: `CBS 10576`, `CBS:10576`, `NCAIM Y.01822`, `NRRL Y-48267`, `NRRL:Y-48267`, and `NRRL:Y:48267`.
- Exact StrainInfo side inventory found one direct record and one type-strain deposit, `IHEM 24839`, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:434199`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:434199`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
