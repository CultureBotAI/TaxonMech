# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_chrysogenum.yaml`
- Taxon: `NCBITaxon:5076` (`Penicillium chrysogenum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5076`, label `Penicillium chrysogenum`.
- It is grounded exactly under `NCBITaxon:254878` (`Penicillium chrysogenum species complex`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through the `Penicillium chrysogenum species complex`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_chrysogenum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_chrysogenum.yaml data/taxa/eukaryota/penicillium_chrzaszczii.yaml data/taxa/eukaryota/penicillium_cinereoatrum.yaml data/taxa/eukaryota/penicillium_cinnamopurpureum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51927` contains the seeded identifier with reason `attested rule: Penicillium chrysogenum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2218` matches the YAML identity: parent `NCBITaxon:254878`, rank `SPECIES`, three exact synonyms, six related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2218` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37448`, where `NCBITaxon:5076` has `organism_count` 69.
- The native GOLD exact current-taxid scan found 68 organism rows, 69 project rows, and 62 analysis rows linked through `AP PROJECT GOLD IDS` for `NCBITaxon:5076`; the generated GOLD aggregate count matches the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 50 rows: 34 culture-from-neotype spellings across `ATCC 10106`, `BCRC 30564`, `CBS 306.48`, `CCRC 30564`, `FRR 807`, `IBT 5233`, `NCTC 589`, `NRRL 807`, and `NRRL 810`; four neotype spellings for `IMI 24314`; and 12 culture-from-holotype spellings for `Penicillium notatum`.
- Exact StrainInfo side evidence has 353 direct `NCBITaxon:5076` records and 614 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:5076`.
- Eight merged-ID side rows map old `NCBITaxon:115827`, `NCBITaxon:1297592`, `NCBITaxon:1452524`, `NCBITaxon:1846263`, `NCBITaxon:1846264`, `NCBITaxon:5080`, `NCBITaxon:947850`, and `NCBITaxon:947851` to current `NCBITaxon:5076`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
