# YAML Record Review

- Target: `data/taxa/eukaryota/myrothecium_sp.yaml`
- Taxon: `NCBITaxon:1756106` (`Myrothecium sp.`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1756106`, label `Myrothecium sp.`.
- It is grounded exactly under `NCBITaxon:2619772` (`unclassified Myrothecium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `unclassified Myrothecium`.

## Validation

- `just validate data/taxa/eukaryota/myrothecium_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myrothecium_sp.yaml data/taxa/eukaryota/mytilinidion_resinicola.yaml data/taxa/eukaryota/myxozyma_geophila.yaml data/taxa/eukaryota/myxozyma_kluyveri.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61211` contains the seeded identifier with reason `attested rule: Myrothecium sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:458291` matches the YAML identity: parent `NCBITaxon:2619772`, rank `SPECIES`, no synonyms, and no retirement target.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:458291` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15279`, where `NCBITaxon:1756106` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0692389` / `Myrothecium sp. GLBRC256`, linked to projects `Gp0803355` and `Gp0803356` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1756106`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1756106`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1756106`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this unclassified placeholder taxon.

## Additional Notes

- None.
