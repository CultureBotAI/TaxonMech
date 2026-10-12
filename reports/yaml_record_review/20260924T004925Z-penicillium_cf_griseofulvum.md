# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_cf_griseofulvum.yaml`
- Taxon: `NCBITaxon:2972120` (`Penicillium cf. griseofulvum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2972120`, label `Penicillium cf. griseofulvum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_cf_griseofulvum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/penicillium_cavernicola.yaml data/taxa/eukaryota/penicillium_cf_griseofulvum.yaml data/taxa/eukaryota/penicillium_chermesinum.yaml data/taxa/eukaryota/penicillium_christenseniae.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63479` contains the seeded identifier with reason `attested rule: Penicillium cf. griseofulvum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:580331` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, no NCBI synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:580331` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:29665`, where `NCBITaxon:2972120` has `organism_count` 2.
- The native GOLD exact current-taxid scan found two organism rows, two project rows, and two analysis rows linked through `AP PROJECT GOLD IDS` for `NCBITaxon:2972120`.
- No exact `data/raw/ncbi_type_material.tsv` rows were present for `NCBITaxon:2972120`.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, exact StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:2972120`.
- With no BacDive or StrainInfo exact matches, there were no generated rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
