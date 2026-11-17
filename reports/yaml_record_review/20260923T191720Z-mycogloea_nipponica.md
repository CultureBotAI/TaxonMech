# YAML Record Review

- Target: `data/taxa/eukaryota/mycogloea_nipponica.yaml`
- Taxon: `NCBITaxon:215669` (`Mycogloea nipponica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:215669`, label `Mycogloea nipponica`.
- It is grounded exactly under `NCBITaxon:45046` (`Mycogloea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mycogloea`.

## Validation

- `just validate data/taxa/eukaryota/mycogloea_nipponica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycogloea_nipponica.yaml data/taxa/eukaryota/mycogone_calospora.yaml data/taxa/eukaryota/mycogone_perniciosa.yaml data/taxa/eukaryota/mycogone_rosea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54553` contains the seeded identifier with reason `attested rule: Mycogloea nipponica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:42463` matches the YAML identity: parent `NCBITaxon:45046`, rank `SPECIES`, and related synonym `Mycogloea nipponica Bandoni, 1998`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:42463` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:20395`, where `NCBITaxon:215669` has `organism_count` 1.
- Exact native GOLD scans found no organism, project, or analysis rows for this current taxid; the GOLD assertion is present only in the transformed aggregate table checked above.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 3 holotype rows for `NCBITaxon:215669`, all designations of Bandoni 8992 in TNS at lines 85942-85944.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:215669`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:215669`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories.

## Additional Notes

- None.
