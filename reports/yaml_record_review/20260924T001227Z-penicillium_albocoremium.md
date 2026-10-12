# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_albocoremium.yaml`
- Taxon: `NCBITaxon:74831` (`Penicillium albocoremium`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:74831`, label `Penicillium albocoremium`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_albocoremium.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_aethiopicum.yaml data/taxa/eukaryota/penicillium_albocoremium.yaml data/taxa/eukaryota/penicillium_alexiae.yaml data/taxa/eukaryota/penicillium_allaniae.yaml` exited successfully for the four-file batch.

## Identity and Grounding

- `curation/seed_scope.tsv:53271` contains the seeded identifier with reason `attested rule: Penicillium albocoremium, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10645` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10645` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42252`, where `NCBITaxon:74831` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0685622`, one project row, `Gp0792441`, and no analysis rows for `NCBITaxon:74831`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found ten type-material spellings centered on `CBS 472.84`, `FRR 2931`, `IBT 10682`, `IBT 21502`, and `IMI 285511`.
- Exact StrainInfo side evidence has 14 direct `NCBITaxon:74831` records and 16 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:74831`.
- The sole merged-ID side row maps old `NCBITaxon:60178` to current `NCBITaxon:74831`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
