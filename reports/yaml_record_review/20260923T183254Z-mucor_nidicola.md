# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_nidicola.yaml`
- Taxon: `NCBITaxon:1095377` (`Mucor nidicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1095377`, label `Mucor nidicola`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_nidicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_nidicola.yaml ... mucor_petropolitanus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57612` contains the seeded identifier with reason `attested rule: Mucor nidicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:235545` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor nidicola Madden, Stchigel, Guarro, Sutton & Starks, 2012`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:235545` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1756`, where `NCBITaxon:1095377` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0402561` / `Mucor nidicola NRRL 54520`, linked to project `Gp0290186`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:6133-6134` has the `NRRL 54520` and `NRRL:54520` type-material aliases.

## Completeness

- The bounded scan found no exact BacDive, StrainInfo, generated raw strain, generated StrainInfo, or auxiliary source rows for `NCBITaxon:1095377`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1095377`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if additional StrainInfo, BacDive, or generated strain evidence is added for this taxon.

## Additional Notes

- None.
