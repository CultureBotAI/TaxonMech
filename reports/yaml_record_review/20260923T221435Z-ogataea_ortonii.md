# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_ortonii.yaml`
- Taxon: `NCBITaxon:150208` (`Ogataea ortonii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:150208`, label `Ogataea ortonii`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_ortonii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ogataea_nonfermentans.yaml data/taxa/eukaryota/ogataea_ortonii.yaml data/taxa/eukaryota/ogataea_ovalis.yaml data/taxa/eukaryota/ogataea_paradorogensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54064` contains the seeded identifier with reason `attested rule: Ogataea ortonii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:30979` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:30979` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11767`, where `NCBITaxon:150208` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705523` / `Candida ortonii NRRL Y-48038`, linked to project `Gp0831566`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material is limited to 10 `Ogataea ortonii` culture-from-holotype and holotype rows for `NRRL Y-48038`, `UWO(PS) 00-159.3`, and `CBS 8843`.
- Exact StrainInfo side inventory found one direct record and one deposit group, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:150208`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:150208`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
