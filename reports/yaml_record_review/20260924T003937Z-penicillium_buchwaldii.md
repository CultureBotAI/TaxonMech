# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_buchwaldii.yaml`
- Taxon: `NCBITaxon:1263195` (`Penicillium buchwaldii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1263195`, label `Penicillium buchwaldii`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_buchwaldii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_brevistipitatum.yaml data/taxa/eukaryota/penicillium_brocae.yaml data/taxa/eukaryota/penicillium_brunneoconidiatum.yaml data/taxa/eukaryota/penicillium_buchwaldii.yaml` exited successfully for the four-file batch.

## Identity and Grounding

- `curation/seed_scope.tsv:58798` contains the seeded identifier with reason `attested rule: Penicillium buchwaldii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:292390` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:292390` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:6204`, where `NCBITaxon:1263195` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1263195`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found eight culture-from-holotype spellings centered on `CBS 117181` and `IBT 6005`, plus four holotype spellings centered on `IMI 304286`.
- Exact StrainInfo side evidence has five direct `NCBITaxon:1263195` records and six deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1263195`.
- The sole merged-ID side row maps old `NCBITaxon:1167580` to current `NCBITaxon:1263195`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
