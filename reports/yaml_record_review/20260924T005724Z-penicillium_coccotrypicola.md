# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_coccotrypicola.yaml`
- Taxon: `NCBITaxon:1552301` (`Penicillium coccotrypicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1552301`, label `Penicillium coccotrypicola`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_coccotrypicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_coccotrypicola.yaml data/taxa/eukaryota/penicillium_coffeae.yaml data/taxa/eukaryota/penicillium_commune.yaml data/taxa/eukaryota/penicillium_compactum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60452` contains the seeded identifier with reason `attested rule: Penicillium coccotrypicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:400316` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:400316` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12425`, where `NCBITaxon:1552301` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, two project rows for that organism, and no analysis rows for `NCBITaxon:1552301`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found the two holotype spellings `BRIP 59608` and `BRIP:59608`.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, exact StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:1552301`.
- With no BacDive or StrainInfo exact matches, there were no generated rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
