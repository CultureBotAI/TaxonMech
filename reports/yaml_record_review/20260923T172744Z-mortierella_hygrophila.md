# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_hygrophila.yaml`
- Taxon: `NCBITaxon:979708` (`Mortierella hygrophila`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979708`, label `Mortierella hygrophila`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_hygrophila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_claussenii.yaml ... mortierella_hygrophila.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57048` contains the seeded identifier with reason `attested rule: Mortierella hygrophila, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204261` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and no related synonyms.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204261` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45187`, where `NCBITaxon:979708` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0452954` / `Mortierella hygrophila NRRL 2591`, linked to project `Gp0317579`; no native analysis row linked to that project.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:979708` type-material rows.

## Completeness

- Exact StrainInfo has one direct record with one deposit, `ATCC 16270`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979708`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:979708`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The transformed GOLD aggregate asserts two organisms, while the local native exact current-taxid scan currently exposes one organism JSONL row.
