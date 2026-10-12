# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_henricii.yaml`
- Taxon: `NCBITaxon:36024` (`Ogataea henricii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36024`, label `Ogataea henricii`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_henricii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_haglerorum.yaml data/taxa/eukaryota/ogataea_henricii.yaml data/taxa/eukaryota/ogataea_kodamae.yaml data/taxa/eukaryota/ogataea_krabiensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52305` contains the seeded identifier with reason `attested rule: Ogataea henricii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4036` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4036` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33246`, where `NCBITaxon:36024` has `organism_count` 6.
- Native GOLD has 6 exact current-taxid organism rows for `NCBITaxon:36024`; one native project, `Gp0441231`, and one native analysis row link through the `Ogataea henricii NRRL YB-2194` organism row.

## Completeness

- Exact NCBI type material is limited to 14 `Hansenula henricii` designations for the `ATCC 18939`, `BCRC 22170` / `CCRC 22170`, `CBS 5765`, `IFO 1477`, `JCM 3611`, and `NRRL YB-2194` type set.
- Exact StrainInfo side inventory found 6 direct records and 26 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:36024`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:36024`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
