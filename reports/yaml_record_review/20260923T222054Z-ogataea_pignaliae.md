# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_pignaliae.yaml`
- Taxon: `NCBITaxon:51923` (`Ogataea pignaliae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:51923`, label `Ogataea pignaliae`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_pignaliae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_pignaliae.yaml data/taxa/eukaryota/ogataea_pilisensis.yaml data/taxa/eukaryota/ogataea_pini.yaml data/taxa/eukaryota/ogataea_pinus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52848` contains the seeded identifier with reason `attested rule: Ogataea pignaliae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6531` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6531` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37689`, where `NCBITaxon:51923` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705325` / `Ogataea pignaliae NRRL Y-17664`, linked to project `Gp0831361`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 16 duplicated spelling rows for `Ogataea pignaliae`, covering `ATCC 36592`, `BCRC` / `CCRC 21625`, `CBS 6071`, `IFO 10307`, `JCM 9836`, `LY 1431`, and `NRRL Y-17664`.
- Exact StrainInfo side inventory found 1 direct record and 12 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:51923`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:51923`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
