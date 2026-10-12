# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_baarnense.yaml`
- Taxon: `NCBITaxon:69793` (`Penicillium baarnense`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69793`, label `Penicillium baarnense`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_baarnense.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/penicillium_aurantiacobrunneum.yaml data/taxa/eukaryota/penicillium_ausonanum.yaml data/taxa/eukaryota/penicillium_austroafricanum.yaml data/taxa/eukaryota/penicillium_baarnense.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53193` contains the seeded identifier with reason `attested rule: Penicillium baarnense, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9680` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9680` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41552`, where `NCBITaxon:69793` has `organism_count` 3.
- The native GOLD exact current-taxid scan found three organism rows and no project or analysis rows for `NCBITaxon:69793`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 16 type-material spellings centered on `ATCC 10415`, `CBS 134.41`, `CSIR 729`, `IFO 6090`, `IFO 8846`, `IMI 040590`, `NRRL 2086`, and `QM 1871`.
- Exact StrainInfo side evidence has 19 direct `NCBITaxon:69793` records and 47 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:69793`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
