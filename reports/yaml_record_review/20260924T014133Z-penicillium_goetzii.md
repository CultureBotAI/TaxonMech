# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_goetzii.yaml`
- Taxon: `NCBITaxon:1304712` (`Penicillium goetzii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1304712`, label `Penicillium goetzii`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_goetzii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_gladioli.yaml data/taxa/eukaryota/penicillium_glandicola.yaml data/taxa/eukaryota/penicillium_goetzii.yaml data/taxa/eukaryota/penicillium_gorlenkoanum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59312` contains the seeded identifier with reason `attested rule: Penicillium goetzii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:308411` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:308411` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7449`, where `NCBITaxon:1304712` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1304712`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 4 rows on lines 21184-21187: 2 `culture-from-holotype` spellings centered on CBS 285.73 and 2 `type-material` spellings centered on DTO 088-G6.
- Exact StrainInfo side evidence was empty for `NCBITaxon:1304712`.
- Exact merged-ID scanning found retired `NCBITaxon:1303713` merged into current `NCBITaxon:1304712`.

## Completeness

- BacDive, StrainInfo, retained retired old-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1304712`.
- The merged ID is NCBI old-ID side evidence only: it did not appear as a retained retired row with `retired_into` evidence requiring a generated `replaces` entry in the YAML.
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
