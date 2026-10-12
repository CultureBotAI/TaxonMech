# YAML Record Review

- Target: `data/taxa/eukaryota/paraphoma_chrysanthemicola.yaml`
- Taxon: `NCBITaxon:798071` (`Paraphoma chrysanthemicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:798071`, label `Paraphoma chrysanthemicola`.
- It is grounded exactly under `NCBITaxon:798070` (`Paraphoma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Paraphoma`.

## Validation

- `just validate data/taxa/eukaryota/paraphoma_chrysanthemicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paranamyces_uniporus.yaml data/taxa/eukaryota/paraphaeosphaeria_minitans.yaml data/taxa/eukaryota/paraphaeosphaeria_sporulosa.yaml data/taxa/eukaryota/paraphoma_chrysanthemicola.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56720` contains the seeded identifier with reason `attested rule: Paraphoma chrysanthemicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:180010` matches the YAML identity: parent `NCBITaxon:798070`, rank `SPECIES`, one exact synonym, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:180010` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42849`, where `NCBITaxon:798071` has `organism_count` 3.
- The native GOLD exact current-taxid scan found three organism rows, five project rows, and one analysis row for `NCBITaxon:798071`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-neotype spellings centered on `CBS 522.66` and two neotype spellings centered on `CBS H-5161` for `NCBITaxon:798071`.
- Exact StrainInfo side evidence has 12 direct `NCBITaxon:798071` records and 14 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:798071`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains two old IDs that now point at `NCBITaxon:798071`: `NCBITaxon:1848037` and `NCBITaxon:646063`; neither is retained as a retired taxon, so the YAML correctly has no `replaces` entries.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
