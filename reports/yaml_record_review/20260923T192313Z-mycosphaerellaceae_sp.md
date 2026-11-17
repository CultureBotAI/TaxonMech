# YAML Record Review

- Target: `data/taxa/eukaryota/mycosphaerellaceae_sp.yaml`
- Taxon: `NCBITaxon:1933429` (`Mycosphaerellaceae sp.`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1933429`, label `Mycosphaerellaceae sp.`.
- It is grounded exactly under `NCBITaxon:243630` (`unclassified Mycosphaerellaceae`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `unclassified Mycosphaerellaceae`.

## Validation

- `just validate data/taxa/eukaryota/mycosphaerellaceae_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycosphaerellaceae_sp.yaml data/taxa/eukaryota/mycosphaerelloides_madeirae.yaml data/taxa/eukaryota/mycothermus_thermophilus.yaml data/taxa/eukaryota/mycothermus_thermophilus_atcc_16453.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61665` contains the seeded identifier with reason `attested rule: Mycosphaerellaceae sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:496543` matches the YAML identity: parent `NCBITaxon:243630`, rank `SPECIES`, no synonyms, and no retirement target.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:496543` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17743`, where `NCBITaxon:1933429` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583397` / `Mycosphaerellaceae sp. 406A_T16_1`, linked to projects `Gp0587360` and `Gp0749127` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1933429`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1933429`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1933429`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this unclassified placeholder taxon.

## Additional Notes

- None.
