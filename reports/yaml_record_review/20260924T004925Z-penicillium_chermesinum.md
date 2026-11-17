# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_chermesinum.yaml`
- Taxon: `NCBITaxon:63820` (`Penicillium chermesinum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:63820`, label `Penicillium chermesinum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_chermesinum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/penicillium_cavernicola.yaml data/taxa/eukaryota/penicillium_cf_griseofulvum.yaml data/taxa/eukaryota/penicillium_chermesinum.yaml data/taxa/eukaryota/penicillium_christenseniae.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53067` contains the seeded identifier with reason `attested rule: Penicillium chermesinum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8020` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Penicillium vietnamense`, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8020` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40165`, where `NCBITaxon:63820` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row linked through `AP PROJECT GOLD IDS` for `NCBITaxon:63820`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-neotype spellings centered on `NRRL 2048` and two neotype spellings centered on `CBS 231.81`.
- Exact StrainInfo side evidence has 22 direct `NCBITaxon:63820` records and 44 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:63820`.
- Two merged-ID side rows map old `NCBITaxon:1111109` and `NCBITaxon:3019913` to current `NCBITaxon:63820`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
