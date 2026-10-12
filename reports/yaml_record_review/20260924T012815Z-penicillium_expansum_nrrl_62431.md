# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_expansum_nrrl_62431.yaml`
- Taxon: `NCBITaxon:1208580` (`Penicillium expansum NRRL 62431`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1208580`, label `Penicillium expansum NRRL 62431`.
- It is grounded exactly under `NCBITaxon:27334` (`Penicillium expansum`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Penicillium expansum`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_expansum_nrrl_62431.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_expansum.yaml data/taxa/eukaryota/penicillium_expansum_nrrl_62431.yaml data/taxa/eukaryota/penicillium_ezekielii.yaml data/taxa/eukaryota/penicillium_fellutanum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58391` contains the seeded identifier with reason `attested rule: Penicillium expansum NRRL 62431, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:273167` matches the YAML identity: parent `NCBITaxon:27334`, rank `STRAIN`, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:273167` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4942`, where `NCBITaxon:1208580` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found 1 organism row, 1 project row, and 1 analysis row for `NCBITaxon:1208580`, centered on organism `Go0038385` / project `Gp0038385`. The native GOLD organism and project names still say `Penicillium aurantiogriseum NRRL 62431`, but their NCBI taxid is the current `1208580`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found no rows for `NCBITaxon:1208580`.
- Exact StrainInfo side evidence was empty for `NCBITaxon:1208580`.

## Completeness

- BacDive, StrainInfo, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1208580`.
- The native GOLD organism/project/analysis chain is fully accounted for by the single generated GOLD aggregate row with `organism_count: 1`.
- The record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
