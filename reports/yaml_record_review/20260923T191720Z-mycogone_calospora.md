# YAML Record Review

- Target: `data/taxa/eukaryota/mycogone_calospora.yaml`
- Taxon: `NCBITaxon:129586` (`Mycogone calospora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:129586`, label `Mycogone calospora`.
- It is grounded exactly under `NCBITaxon:129584` (`Mycogone`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Mycogone`.

## Validation

- `just validate data/taxa/eukaryota/mycogone_calospora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycogloea_nipponica.yaml data/taxa/eukaryota/mycogone_calospora.yaml data/taxa/eukaryota/mycogone_perniciosa.yaml data/taxa/eukaryota/mycogone_rosea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53925` contains the seeded identifier with reason `attested rule: Mycogone calospora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:24782` matches the YAML identity: parent `NCBITaxon:129584`, rank `SPECIES`, exact synonym `Coccosporella calospora`, and related synonyms `Coccosporella calospora P. Karst., 1893` and `Mycogone calospora (P. Karst.) Hohn., 1923`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:24782` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7035`, where `NCBITaxon:129586` has `organism_count` 1.
- Exact native GOLD scans found no organism, project, or analysis rows for this current taxid; the GOLD assertion is present only in the transformed aggregate table checked above.

## Completeness

- The exact file scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:129586`.
- Exact StrainInfo has 3 direct records and 3 deposit rows for `NCBITaxon:129586`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:129586`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:129586`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
