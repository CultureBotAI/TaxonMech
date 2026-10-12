# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_atrolazulinum.yaml`
- Taxon: `NCBITaxon:1297656` (`Penicillium atrolazulinum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1297656`, label `Penicillium atrolazulinum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_atrolazulinum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_atrofulvum.yaml data/taxa/eukaryota/penicillium_atrolazulinum.yaml data/taxa/eukaryota/penicillium_atrosanguineum.yaml data/taxa/eukaryota/penicillium_atrovenetum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59255` contains the seeded identifier with reason `attested rule: Penicillium atrolazulinum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:305769` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:305769` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7268`, where `NCBITaxon:1297656` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1297656`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found eight culture-from-holotype spellings centered on `CBS 139136`, `DAOM 24108`, `DAOMC 24108`, and `DTO 180-H4`.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, exact StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:1297656`.
- With no BacDive or StrainInfo exact matches, there were no generated rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
