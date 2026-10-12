# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_sinensis.yaml`
- Taxon: `NCBITaxon:1196548` (`Mucor sinensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1196548`, label `Mucor sinensis`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_sinensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_rouxianus.yaml ... mucor_sinensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58297` contains the seeded identifier with reason `attested rule: Mucor sinensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:269153` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor sinensis Milko & Beliakova, 1971`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:269153` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4745`, where `NCBITaxon:1196548` has `organism_count` 5.
- Native GOLD has five exact current-taxid organism rows for `NRRL 6352`, `CBS 204.74`, `CCF 2020`, `DSM 2227`, and `VKM F-638`; only `Go0535938` / `Mucor sinensis NRRL 6352` links to a native project.
- `data/raw/ncbi_type_material.tsv:12986-12997` has 12 type-material aliases covering `BCRC 32104`, `CBS 204.74`, `CCF 2020`, `CCRC 32104`, `DSM 2227`, `VKM F-638`, and their punctuation variants.

## Completeness

- Exact StrainInfo has 1 direct record and 6 deposit rows for `NCBITaxon:1196548`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1196548`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1196548`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if native GOLD project links are added for the four current-taxid organism rows without projects.

## Additional Notes

- None.
