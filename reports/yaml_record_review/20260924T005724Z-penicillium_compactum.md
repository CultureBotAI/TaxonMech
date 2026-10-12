# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_compactum.yaml`
- Taxon: `NCBITaxon:1882267` (`Penicillium compactum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1882267`, label `Penicillium compactum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_compactum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_coccotrypicola.yaml data/taxa/eukaryota/penicillium_coffeae.yaml data/taxa/eukaryota/penicillium_commune.yaml data/taxa/eukaryota/penicillium_compactum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61423` contains the seeded identifier with reason `attested rule: Penicillium compactum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:490183` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:490183` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:16902`, where `NCBITaxon:1882267` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1882267`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 10 culture-from-holotype spellings centered on `AS 3.15411`, `CBS 138918`, `CGMCC 3.15411`, `DTO 316-B8`, and `IBT 33393`, plus two holotype spellings centered on `HMAS 245701`.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, exact StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:1882267`.
- With no BacDive or StrainInfo exact matches, there were no generated rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
