# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_javanicus.yaml`
- Taxon: `NCBITaxon:51122` (`Mucor javanicus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:51122`, label `Mucor javanicus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_javanicus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_intermedius.yaml ... mucor_laxorrhizus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52823` contains the seeded identifier with reason `attested rule: Mucor javanicus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6429` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and no related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6429` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37505`, where `NCBITaxon:51122` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows, `Go0470857`, `Go0527584`, and `Go0527634`, linked to three projects; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:51122` type-material rows.

## Completeness

- Exact StrainInfo has 17 direct records and 22 deposit rows for `NCBITaxon:51122`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:51122`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:51122`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The source NCBI row has no exact, broad, or related synonyms.
