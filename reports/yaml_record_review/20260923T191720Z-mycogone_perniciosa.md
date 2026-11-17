# YAML Record Review

- Target: `data/taxa/eukaryota/mycogone_perniciosa.yaml`
- Taxon: `NCBITaxon:494059` (`Mycogone perniciosa`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:494059`, label `Mycogone perniciosa`.
- It is grounded exactly under `NCBITaxon:129584` (`Mycogone`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Mycogone`.

## Validation

- `just validate data/taxa/eukaryota/mycogone_perniciosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycogloea_nipponica.yaml data/taxa/eukaryota/mycogone_calospora.yaml data/taxa/eukaryota/mycogone_perniciosa.yaml data/taxa/eukaryota/mycogone_rosea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55833` contains the seeded identifier with reason `attested rule: Mycogone perniciosa, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:112246` matches the YAML identity: parent `NCBITaxon:129584`, rank `SPECIES`, and related synonym `Mycogone perniciosa Magnus, 1888`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:112246` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37197`, where `NCBITaxon:494059` has `organism_count` 1.
- Exact native GOLD scans found no organism, project, or analysis rows for this current taxid; the GOLD assertion is present only in the transformed aggregate table checked above.

## Completeness

- The exact file scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:494059`.
- Exact StrainInfo has 39 direct records and 39 deposit rows for `NCBITaxon:494059`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:494059`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:494059`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
