# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_piceae.yaml`
- Taxon: `NCBITaxon:96497` (`Ogataea piceae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:96497`, label `Ogataea piceae`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_piceae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_paraovalis.yaml data/taxa/eukaryota/ogataea_parapolymorpha_dl_1.yaml data/taxa/eukaryota/ogataea_philodendri.yaml data/taxa/eukaryota/ogataea_piceae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53566` contains the seeded identifier with reason `attested rule: Ogataea piceae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:16294` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:16294` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45112`, where `NCBITaxon:96497` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705687` / `Candida piceae NRRL YB-2107`, linked to project `Gp0831739`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to seven `Candida piceae` culture-from-holotype and holotype rows for `NRRL YB-2107` and `CBS 8701`.
- Exact StrainInfo side inventory found 2 direct records and 5 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:96497`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:96497`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
