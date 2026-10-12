# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_rufescens.yaml`
- Taxon: `NCBITaxon:1385757` (`Mucor rufescens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1385757`, label `Mucor rufescens`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_rufescens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_rouxianus.yaml ... mucor_sinensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59784` contains the seeded identifier with reason `attested rule: Mucor rufescens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:338511` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no synonyms, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:338511` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9099`, where `NCBITaxon:1385757` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0535967` / `Mucor rufescens NRRL 1661`, linked to project `Gp0484445`; no native analysis row linked to that project.

## Completeness

- The bounded scan found no exact type-material, BacDive, StrainInfo, generated raw strain, generated StrainInfo, or auxiliary source rows for `NCBITaxon:1385757`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1385757`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if additional StrainInfo, BacDive, or generated strain evidence is added for this taxon.

## Additional Notes

- None.
