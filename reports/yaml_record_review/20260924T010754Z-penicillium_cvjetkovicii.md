# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_cvjetkovicii.yaml`
- Taxon: `NCBITaxon:1465813` (`Penicillium cvjetkovicii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1465813`, label `Penicillium cvjetkovicii`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_cvjetkovicii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_crystallinum.yaml data/taxa/eukaryota/penicillium_curticaule.yaml data/taxa/eukaryota/penicillium_cvjetkovicii.yaml data/taxa/eukaryota/penicillium_cyaneum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60229` contains the seeded identifier with reason `attested rule: Penicillium cvjetkovicii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:372703` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:372703` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11266`, where `NCBITaxon:1465813` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, two project rows for that organism, and no analysis rows for `NCBITaxon:1465813`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-holotype spellings centered on `NRRL 35841` and two holotype spellings centered on `BPI 881283`.

## Completeness

- BacDive, retained retired old-ID, exact StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:1465813`.
- Two merged-ID side rows map old `NCBITaxon:1465814` and `NCBITaxon:456882` to current `NCBITaxon:1465813`, and the YAML correctly uses the current identifier.
- With no BacDive or StrainInfo exact matches, there were no generated rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
