# YAML Record Review

- Target: `data/taxa/eukaryota/neoaidaea_tothii.yaml`
- Taxon: `NCBITaxon:44089` (`Neoaidaea tothii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:44089`, label `Neoaidaea tothii`.
- It is grounded exactly under `NCBITaxon:3715007` (`Neoaidaea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Neoaidaea`.

## Validation

- `just validate data/taxa/eukaryota/neoaidaea_tothii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoaidaea_tothii.yaml data/taxa/eukaryota/neobodo_designis.yaml data/taxa/eukaryota/neobodo_saliens.yaml data/taxa/eukaryota/neoboletus_brunneissimus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52576` contains the seeded identifier with reason `attested rule: Neoaidaea tothii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:5337` matches the YAML identity: parent `NCBITaxon:3715007`, rank `SPECIES`, five synonyms, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:5337` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:35580`, where `NCBITaxon:44089` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows: `Go0583973` / `Dipodascopsis tothii CBS 759.85` and `Go0705221` / `Dipodascopsis tothii NRRL Y-12690`.
- Those native organism IDs link to projects `Gp0588866`, `Gp0595889`, and `Gp0831248`; no native GOLD analysis rows were found for the linked projects.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 9 type-material rows for `NCBITaxon:44089`, covering variants of `ATCC 76902`, `CBS 759.85`, `CSIR 31`, and `NRRL Y-12690`.
- Exact StrainInfo side inventory found two direct records, `SI-ID122620` and `SI-ID275058`, and 10 deposit assertions including `IFO 10813`, `ATCC 76902`, `CBS 759.85`, `IFO 10371`, `NRRL Y-12690`, `NBRC 10813`, `NBRC 10371`, `KCTC 17195`, `VKM F-1832`, and `NCAIM Y.00340`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:44089`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:44089`; the exact StrainInfo and type-material side inventories did not materialize local strain rows, so `strain_count: 0` is consistent with generated provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
