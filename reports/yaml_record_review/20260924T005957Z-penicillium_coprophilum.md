# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_coprophilum.yaml`
- Taxon: `NCBITaxon:36646` (`Penicillium coprophilum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36646`, label `Penicillium coprophilum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_coprophilum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_confertum.yaml data/taxa/eukaryota/penicillium_consobrinum.yaml data/taxa/eukaryota/penicillium_coprobium.yaml data/taxa/eukaryota/penicillium_coprophilum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52342` contains the seeded identifier with reason `attested rule: Penicillium coprophilum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4085` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4085` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33427`, where `NCBITaxon:36646` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row linked through `AP PROJECT GOLD IDS` for `NCBITaxon:36646`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 13 culture-from-epitype spellings centered on `CBS 110760`, `IBT 5551`, `NRRL 13627`, and `T 129` under the synonym `Coremium coprophilum`.
- Exact StrainInfo side evidence has 25 direct `NCBITaxon:36646` records and 31 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:36646`.
- The sole merged-ID side row maps old `NCBITaxon:2082142` to current `NCBITaxon:36646`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
