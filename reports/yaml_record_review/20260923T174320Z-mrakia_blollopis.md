# YAML Record Review

- Target: `data/taxa/eukaryota/mrakia_blollopis.yaml`
- Taxon: `NCBITaxon:696254` (`Mrakia blollopis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:696254`, label `Mrakia blollopis`.
- It is grounded exactly under `NCBITaxon:29901` (`Mrakia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mrakia`.

## Validation

- `just validate data/taxa/eukaryota/mrakia_blollopis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_umbellata.yaml ... mrakia_blollopis.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56447` contains the seeded identifier with reason `attested rule: Mrakia blollopis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:163224` matches the YAML identity: parent `NCBITaxon:29901`, rank `SPECIES`, no exact synonyms, and the five related synonyms represented in YAML.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:163224` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41505`, where `NCBITaxon:696254` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0144878` / `Mrakia blollopis SK-4`, linked to project `Gp0150507` and one native analysis row, `Mrakia blollopis SK-4`.
- `data/raw/ncbi_type_material.tsv:257950-257951` has `CBS 8921` holotype aliases.

## Completeness

- Exact StrainInfo had no direct records or deposit rows for `NCBITaxon:696254`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:696254`.
- `data/raw/ncbi_merged_ids.tsv` carries side-inventory old IDs `NCBITaxon:162227`, `NCBITaxon:162228`, `NCBITaxon:162229`, and `NCBITaxon:1652683` that all merge into `NCBITaxon:696254`, but the bounded scan found no retained retired rows in `data/raw/ncbitaxon_taxa.tsv`; generated `replaces` omission is consistent with local retained-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strain rows for `Mrakia blollopis SK-4`.

## Additional Notes

- The single native GOLD analysis row links through `AP PROJECT GOLD IDS` to the exact native project `Gp0150507`.
