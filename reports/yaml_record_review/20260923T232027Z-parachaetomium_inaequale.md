# YAML Record Review

- Target: `data/taxa/eukaryota/parachaetomium_inaequale.yaml`
- Taxon: `NCBITaxon:2588326` (`Parachaetomium inaequale`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2588326`, label `Parachaetomium inaequale`.
- It is grounded exactly under `NCBITaxon:2795251` (`Parachaetomium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Parachaetomium`.

## Validation

- `just validate data/taxa/eukaryota/parachaetomium_inaequale.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/parachaetomium_inaequale.yaml data/taxa/eukaryota/paracoccidioides_brasiliensis.yaml data/taxa/eukaryota/paracoccidioides_lutzii_pb01.yaml data/taxa/eukaryota/paraconiothyrium_cyclothyrioides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62869` contains the seeded identifier with reason `attested rule: Parachaetomium inaequale, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:534404` matches the YAML identity: parent `NCBITaxon:2795251`, rank `SPECIES`, two exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:534404` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23690`, where `NCBITaxon:2588326` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row and one project row for `Corynascella inaequalis CBS 284.82`; it found no analysis rows.
- Exact `data/raw/ncbi_type_material.tsv` scanning found seven type-material spellings for `NCBITaxon:2588326` on lines 103548-103554, all under `Thielavia inaequalis`.
- Exact StrainInfo side evidence has seven direct `NCBITaxon:2588326` records and 11 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2588326`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:2588326`: `NCBITaxon:1126959`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
