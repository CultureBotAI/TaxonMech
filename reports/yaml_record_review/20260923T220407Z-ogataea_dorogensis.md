# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_dorogensis.yaml`
- Taxon: `NCBITaxon:169506` (`Ogataea dorogensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:169506`, label `Ogataea dorogensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_dorogensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_degrootiae.yaml data/taxa/eukaryota/ogataea_dorogensis.yaml data/taxa/eukaryota/ogataea_ganodermae.yaml data/taxa/eukaryota/ogataea_glucozyma.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54252` contains the seeded identifier with reason `attested rule: Ogataea dorogensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:34589` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:34589` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:14626`, where `NCBITaxon:169506` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705459` / `Ogataea dorogensis NRRL Y-27599`, linked to project `Gp0831502`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to 10 `Ogataea dorogensis` designations for `CBS 9260`, `NCAIM Y-1539`, and `NRRL Y-27599`.
- Exact StrainInfo side inventory found one direct record and 5 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:169506`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:169506`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
