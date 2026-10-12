# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_circinatus.yaml`
- Taxon: `NCBITaxon:2054153` (`Mucor circinatus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2054153`, label `Mucor circinatus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_circinatus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_bainieri.yaml ... mucor_circinatus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62229` contains the seeded identifier with reason `attested rule: Mucor circinatus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:514205` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonyms `Mucor circinatus D.X. Lima, G. Walther & A.L. Santiago, 2017` and `Mucor sp. RO-2017a`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:514205` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19601`, where `NCBITaxon:2054153` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0631674` / `Mucor circinatus CBS 142.35`, linked to project `Gp0645222`, plus one native analysis row with `AP NAME` `Mucor circinatus CBS 142.35` and `AP PROJECT GOLD IDS` `Gp0645222`.
- `data/raw/ncbi_type_material.tsv:81470-81472` has the `URM 90063`, `URM:90063`, and `URM<BRA>:90063` holotype aliases.

## Completeness

- Exact StrainInfo direct and deposit rows were empty for `NCBITaxon:2054153`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:2054153`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:2054153`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the native GOLD organism, project, and analysis rows.

## Additional Notes

- The native GOLD analysis row links to this record by `AP PROJECT GOLD IDS` rather than by `AP ORGANISM GOLD ID`, which is empty on that row.
