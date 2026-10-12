# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_glucozyma.yaml`
- Taxon: `NCBITaxon:36023` (`Ogataea glucozyma`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36023`, label `Ogataea glucozyma`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_glucozyma.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_degrootiae.yaml data/taxa/eukaryota/ogataea_dorogensis.yaml data/taxa/eukaryota/ogataea_ganodermae.yaml data/taxa/eukaryota/ogataea_glucozyma.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52304` contains the seeded identifier with reason `attested rule: Ogataea glucozyma, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4035` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4035` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33245`, where `NCBITaxon:36023` has `organism_count` 7.
- Native GOLD has 7 exact current-taxid organism rows for `NCBITaxon:36023`; one native project, `Gp0441161`, and one native analysis row link through the `Ogataea glucozyma NRRL YB-2185` organism row.

## Completeness

- Exact NCBI type material is limited to 14 `Hansenula glucozyma` designations for the `ATCC 18938`, `BCRC 20465` / `CCRC 20465`, `CBS 5766`, `IFO 1472`, `JCM 3607`, and `NRRL YB-2185` type set.
- Exact StrainInfo side inventory found 4 direct records and 18 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:36023`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:36023`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
