# YAML Record Review

- Target: `data/taxa/eukaryota/pecoramyces_ruminantium.yaml`
- Taxon: `NCBITaxon:1987568` (`Pecoramyces ruminantium`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1987568`, label `Pecoramyces ruminantium`.
- It is grounded exactly under `NCBITaxon:1987567` (`Pecoramyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Pecoramyces`.

## Validation

- `just validate data/taxa/eukaryota/pecoramyces_ruminantium.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paxillus_rubicundulus.yaml data/taxa/eukaryota/pecoramyces_ruminantium.yaml data/taxa/eukaryota/pedinellales_sp_ccmp2098.yaml data/taxa/eukaryota/pelagococcus_subviridis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61826` contains the seeded identifier with reason `attested rule: Pecoramyces ruminantium, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:508586` matches the YAML identity: parent `NCBITaxon:1987567`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:508586` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:18414`, where `NCBITaxon:1987568` has `organism_count` 6.
- The native GOLD exact current-taxid scan found one organism row, three project rows, and three analysis rows for `NCBITaxon:1987568`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found four type-material spellings centered on `C1A`.

## Completeness

- BacDive, exact StrainInfo side evidence, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1987568`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains old IDs `NCBITaxon:1117330` and `NCBITaxon:2100153`, which now point at `NCBITaxon:1987568`; neither is retained as a retired taxon, so the YAML correctly has no `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
