# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_nonfermentans.yaml`
- Taxon: `NCBITaxon:53937` (`Ogataea nonfermentans`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:53937`, label `Ogataea nonfermentans`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_nonfermentans.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ogataea_nonfermentans.yaml data/taxa/eukaryota/ogataea_ortonii.yaml data/taxa/eukaryota/ogataea_ovalis.yaml data/taxa/eukaryota/ogataea_paradorogensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52897` contains the seeded identifier with reason `attested rule: Ogataea nonfermentans, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6804` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, three exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6804` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38255`, where `NCBITaxon:53937` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517118` / `Ogataea nonfermentans NRRL YB-2203`, linked to project `Gp0441156`; one native analysis row links through `Gp0441156`.

## Completeness

- Exact NCBI type material is limited to seven `Hansenula nonfermentans` type-material rows for `CBS 5764`, `IFO 1473`, and `NRRL YB-2203`.
- Exact StrainInfo side inventory found 5 direct records and 14 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:53937`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:53937`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
