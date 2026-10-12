# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_boreae.yaml`
- Taxon: `NCBITaxon:189054` (`Penicillium boreae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:189054`, label `Penicillium boreae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_boreae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_bilaiae.yaml data/taxa/eukaryota/penicillium_boreae.yaml data/taxa/eukaryota/penicillium_brasilianum.yaml data/taxa/eukaryota/penicillium_brevicompactum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54394` contains the seeded identifier with reason `attested rule: Penicillium boreae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:37457` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:37457` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17022`, where `NCBITaxon:189054` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:189054`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-holotype spellings centered on `NRRL 31002` and two holotype spellings centered on `BPI 841395`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:189054` record, `siID` 240069 with DOI `10.60712/SI-ID240069.2`, and two deposits.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:189054`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
