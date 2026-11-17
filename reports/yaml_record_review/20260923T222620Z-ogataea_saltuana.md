# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_saltuana.yaml`
- Taxon: `NCBITaxon:490709` (`Ogataea saltuana`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:490709`, label `Ogataea saltuana`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_saltuana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_saltuana.yaml data/taxa/eukaryota/ogataea_siamensis.yaml data/taxa/eukaryota/ogataea_sithepensis.yaml data/taxa/eukaryota/ogataea_sonorensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55826` contains the seeded identifier with reason `attested rule: Ogataea saltuana, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:110556` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, no exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:110556` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37087`, where `NCBITaxon:490709` has `organism_count` 2.
- Native GOLD has 2 exact current-taxid organism rows, `Go0705539` / `Ogataea saltuana NRRL Y-48448` and `Go0705691` / `Ogataea saltuana NRRL YB-2437`, linked to two projects; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 1 holotype row for `NCAIM Y.01833` and 5 duplicated isotype rows for `CBS 10795` and `NRRL Y-48448`.
- Exact StrainInfo side inventory found 1 direct record and 2 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:490709`.
- Exact NCBI merged-ID side inventory maps old `NCBITaxon:1002908` to `NCBITaxon:490709`, while retained retired old-ID, BacDive, and checked auxiliary source rows were empty; the record correctly has no `replaces` entry and `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, native GOLD, or NCBI merged-ID side inventories.

## Additional Notes

- None.
