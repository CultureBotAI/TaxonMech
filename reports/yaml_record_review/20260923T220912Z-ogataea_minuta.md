# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_minuta.yaml`
- Taxon: `NCBITaxon:36026` (`Ogataea minuta`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36026`, label `Ogataea minuta`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_minuta.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_maris.yaml data/taxa/eukaryota/ogataea_mattraensis.yaml data/taxa/eukaryota/ogataea_methanolica.yaml data/taxa/eukaryota/ogataea_minuta.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52307` contains the seeded identifier with reason `attested rule: Ogataea minuta, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4038` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, six exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4038` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33249`, where `NCBITaxon:36026` has `organism_count` 20.
- Native GOLD has 20 exact current-taxid organism rows for `NCBITaxon:36026`; one native project and one native analysis row link to this taxon in the local exact native-GOLD scan.

## Completeness

- Exact NCBI type material is split across 21 `Hansenula minuta` type-material rows and 13 `Torulopsis methanolovescens` type-material rows.
- Exact StrainInfo side inventory found 10 direct records and 60 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:36026`.
- `data/raw/ncbi_merged_ids.tsv:82395` and `data/raw/ncbi_merged_ids.tsv:85223` map side-inventory old IDs `NCBITaxon:50261` and `NCBITaxon:53936` into `NCBITaxon:36026`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` generated `replaces` entries.
- Exact BacDive and checked auxiliary source rows were empty for `NCBITaxon:36026`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
