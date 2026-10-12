# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_fuscum.yaml`
- Taxon: `NCBITaxon:70104` (`Penicillium fuscum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:70104`, label `Penicillium fuscum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_fuscum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_fuscoglaucum.yaml data/taxa/eukaryota/penicillium_fuscum.yaml data/taxa/eukaryota/penicillium_gallaicum.yaml data/taxa/eukaryota/penicillium_glabrum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53204` contains the seeded identifier with reason `attested rule: Penicillium fuscum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9774` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonyms `Citromyces fuscus` and `Eupenicillium pinetorum`, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9774` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41621`, where `NCBITaxon:70104` has `organism_count` 8.
- The local native GOLD exact current-taxid scan found 7 organism rows, 0 project rows, and 0 analysis rows for `NCBITaxon:70104`; all 7 organism rows were filed under the synonymous GOLD name `Eupenicillium pinetorum`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 7 `culture-from-type-material` rows on lines 258682-258688 under `Citromyces fuscus`, centered on ATCC 14770, BCRC or CCRC 31517, and CBS 295.62.
- Exact StrainInfo side evidence has 28 direct `NCBITaxon:70104` records and 65 deposits across those records.
- Exact merged-ID scanning found retired `NCBITaxon:1196337` and `NCBITaxon:69800` merged into current `NCBITaxon:70104`.

## Completeness

- BacDive, retained retired old-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:70104`.
- The 8-organism transformed GOLD aggregate and 7-row local native GOLD exact scan differ at the source-cache layer; the YAML correctly follows the transformed aggregate evidence row.
- The two merged IDs are NCBI old-ID side evidence only: neither appeared as retained retired rows with `retired_into` evidence requiring a generated `replaces` entry in the YAML.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
