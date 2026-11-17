# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_doidgeae.yaml`
- Taxon: `NCBITaxon:3080660` (`Penicillium doidgeae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:3080660`, label `Penicillium doidgeae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_doidgeae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_dipodomyus.yaml data/taxa/eukaryota/penicillium_discolor.yaml data/taxa/eukaryota/penicillium_doidgeae.yaml data/taxa/eukaryota/penicillium_donkii.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63544` contains the seeded identifier with reason `attested rule: Penicillium doidgeae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:595694` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Penicillium sp. C3 CMV-2012`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:595694` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:31210`, where `NCBITaxon:3080660` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:3080660`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 18 rows on lines 165153-165170, all `culture-from-holotype` spellings centered on CBS 138947, CBS H-22038, CV 2189, DAOM 241107, DTO 183-G7, and IBT 31950.
- Exact StrainInfo side evidence was empty for `NCBITaxon:3080660`.
- Exact merged-ID scanning found retired `NCBITaxon:1195902` and `NCBITaxon:1295599` merged into current `NCBITaxon:3080660`.

## Completeness

- BacDive, StrainInfo, retained retired old-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:3080660`.
- The two merged IDs are NCBI old-ID side evidence only: neither appeared as retained retired rows with `retired_into` evidence requiring a generated `replaces` entry in the YAML.
- The record correctly has `strain_count: 0`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
