# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_paraovalis.yaml`
- Taxon: `NCBITaxon:1943672` (`Ogataea paraovalis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1943672`, label `Ogataea paraovalis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_paraovalis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ogataea_paraovalis.yaml data/taxa/eukaryota/ogataea_parapolymorpha_dl_1.yaml data/taxa/eukaryota/ogataea_philodendri.yaml data/taxa/eukaryota/ogataea_piceae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61700` contains the seeded identifier with reason `attested rule: Ogataea paraovalis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:498085` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:498085` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17881`, where `NCBITaxon:1943672` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705107` / `Ogataea paraovalis CBS 14697`, linked to project `Gp0831129`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to six `Ogataea paraovalis` culture-from-holotype and holotype rows for `CBS 14697` and `NYNU 167106`.
- Exact NCBI merged-ID, BacDive, StrainInfo, generated strain, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1943672`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
