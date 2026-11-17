# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_euglaucum.yaml`
- Taxon: `NCBITaxon:1131583` (`Penicillium euglaucum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1131583`, label `Penicillium euglaucum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_euglaucum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_ehrlichii.yaml data/taxa/eukaryota/penicillium_eickeri.yaml data/taxa/eukaryota/penicillium_elizabethiae.yaml data/taxa/eukaryota/penicillium_euglaucum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57835` contains the seeded identifier with reason `attested rule: Penicillium euglaucum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:245745` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Eupenicillium euglaucum`, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:245745` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:2682`, where `NCBITaxon:1131583` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1131583`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 8 rows on lines 8354-8361: 2 `culture-from-neotype` spellings centered on CBS 323.71 and 6 `type-material` spellings centered on CBS 339.61, NRRL 2087, and QM 7491.
- Exact StrainInfo side evidence has 21 direct `NCBITaxon:1131583` records and 51 deposits across those records.
- Exact merged-ID scanning found retired `NCBITaxon:64658` and `NCBITaxon:904682` merged into current `NCBITaxon:1131583`.

## Completeness

- BacDive, retained retired old-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:1131583`.
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
