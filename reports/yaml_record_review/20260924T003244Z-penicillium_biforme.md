# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_biforme.yaml`
- Taxon: `NCBITaxon:707954` (`Penicillium biforme`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:707954`, label `Penicillium biforme`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_biforme.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_balearicum.yaml data/taxa/eukaryota/penicillium_beceitense.yaml data/taxa/eukaryota/penicillium_bialowiezense.yaml data/taxa/eukaryota/penicillium_biforme.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56509` contains the seeded identifier with reason `attested rule: Penicillium biforme, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:165583` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:165583` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41736`, where `NCBITaxon:707954` has `organism_count` 3.
- The native GOLD exact current-taxid scan found three organism rows, six project rows, and no analysis rows for `NCBITaxon:707954`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 17 type-material spellings centered on `ATCC 10416`, `CBS 297.48`, `FRR 885`, `IFO 7722`, `IMI 039820`, `LSHB P72`, `MUCL 29165`, `NRRL 885`, and `QM 7492`.
- Exact StrainInfo side evidence has four direct `NCBITaxon:707954` records and six deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:707954`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
