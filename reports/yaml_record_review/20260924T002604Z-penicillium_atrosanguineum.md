# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_atrosanguineum.yaml`
- Taxon: `NCBITaxon:1132637` (`Penicillium atrosanguineum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1132637`, label `Penicillium atrosanguineum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_atrosanguineum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_atrofulvum.yaml data/taxa/eukaryota/penicillium_atrolazulinum.yaml data/taxa/eukaryota/penicillium_atrosanguineum.yaml data/taxa/eukaryota/penicillium_atrovenetum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57841` contains the seeded identifier with reason `attested rule: Penicillium atrosanguineum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:245941` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:245941` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:2709`, where `NCBITaxon:1132637` has `organism_count` 4.
- The native GOLD exact current-taxid scan found four organism rows, 18 project rows, and three analysis rows linked by `AP PROJECT GOLD IDS` for `NCBITaxon:1132637`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-holotype spellings centered on `CBS 380.75`, plus four culture-from-type-material spellings centered on `FRR 1726` and `IMI 197488`.
- Exact StrainInfo side evidence has 14 direct `NCBITaxon:1132637` records and 25 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1132637`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
