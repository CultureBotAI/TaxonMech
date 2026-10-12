# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_nakhonphanomensis.yaml`
- Taxon: `NCBITaxon:447321` (`Ogataea nakhonphanomensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:447321`, label `Ogataea nakhonphanomensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_nakhonphanomensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_nakhonphanomensis.yaml data/taxa/eukaryota/ogataea_nemodendra.yaml data/taxa/eukaryota/ogataea_neopini.yaml data/taxa/eukaryota/ogataea_nitratoaversa.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55683` contains the seeded identifier with reason `attested rule: Ogataea nakhonphanomensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:99561` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:99561` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:35767`, where `NCBITaxon:447321` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0704952` / `Ogataea nakhonphanomensis CBS 10362`, linked to project `Gp0830968`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to 18 `Ogataea nakhonphanomensis` culture-from-holotype and holotype rows for `ATCC MYA-4463`, `CBS 10362`, `NBRC 101966`, `BCC<THA> 21228`, and `S051`.
- Exact NCBI merged-ID, BacDive, StrainInfo, generated strain, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:447321`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
