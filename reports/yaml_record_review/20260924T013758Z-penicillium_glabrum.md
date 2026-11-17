# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_glabrum.yaml`
- Taxon: `NCBITaxon:69773` (`Penicillium glabrum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69773`, label `Penicillium glabrum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_glabrum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_fuscoglaucum.yaml data/taxa/eukaryota/penicillium_fuscum.yaml data/taxa/eukaryota/penicillium_gallaicum.yaml data/taxa/eukaryota/penicillium_glabrum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53183` contains the seeded identifier with reason `attested rule: Penicillium glabrum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9670` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Citromyces glaber`, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9670` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41541`, where `NCBITaxon:69773` has `organism_count` 3.
- The local native GOLD exact current-taxid scan found 3 organism rows, 4 project rows, and 3 analysis rows for `NCBITaxon:69773`, covering `Penicillium glabrum DAOM 239074`, `Penicillium glabrum IBT 35677`, and `Penicillium glabrum IBT 35679`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 2 `neotype` rows on lines 258112-258113 under `Citromyces glaber`, centered on CBS 125543.
- Exact StrainInfo side evidence has 139 direct `NCBITaxon:69773` records and 222 deposits across those records.
- Exact merged-ID scanning found retired `NCBITaxon:1195892` merged into current `NCBITaxon:69773`.

## Completeness

- BacDive, retained retired old-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:69773`.
- The three native GOLD organisms are fully accounted for by the generated GOLD aggregate row with `organism_count: 3`.
- The merged ID is NCBI old-ID side evidence only: it did not appear as a retained retired row with `retired_into` evidence requiring a generated `replaces` entry in the YAML.
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
