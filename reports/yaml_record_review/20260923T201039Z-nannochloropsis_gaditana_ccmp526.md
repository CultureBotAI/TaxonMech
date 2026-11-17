# YAML Record Review

- Target: `data/taxa/eukaryota/nannochloropsis_gaditana_ccmp526.yaml`
- Taxon: `NCBITaxon:1093141` (`Nannochloropsis gaditana CCMP526`)
- Verdict: pass

## Target

- The record is the seeded retired strain `NCBITaxon:1093141`, label `Nannochloropsis gaditana CCMP526`.
- It is marked `mapping_status: DEPRECATED` and its NCBI row has `retired_into` `NCBITaxon:72520`.
- The retained prior taxonomy places it under `NCBITaxon:72520` (`Microchloropsis gaditana`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 11 lineage entries from `root` through `Microchloropsis gaditana`.

## Validation

- `just validate data/taxa/eukaryota/nannochloropsis_gaditana_ccmp526.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nannochloropsis_gaditana_ccmp526.yaml data/taxa/eukaryota/nannochloropsis_oceanica.yaml data/taxa/eukaryota/nannochloropsis_oceanica_strain_imet1.yaml data/taxa/eukaryota/nannochloropsis_oculata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57585` contains the seeded identifier with reason `attested rule: Nannochloropsis gaditana CCMP526, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:235163` matches the YAML identity: rank `STRAIN`, parent `NCBITaxon:72520`, `retired_into` `NCBITaxon:72520`, genetic code `1`, and the retained 2026-09-11T23:57:26Z taxonomy snapshot.
- All 11 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:235163` and its retired-identifier note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1695`, where `NCBITaxon:1093141` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0019168` / `Nannochloropsis gaditana CCMP 526`, linked to project `Gp0019168`.
- A native GOLD analysis for `Nannochloropsis gaditana CCMP 526` is linked through `AP PROJECT GOLD IDS` to `Gp0019168`.

## Completeness

- Exact ignored-file-inclusive scans of `data/raw/ncbi_type_material.tsv` and `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1093141`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1093141`.
- Because this is the retained retired record itself, the absence of old IDs merging into it is consistent with the YAML's absence of `replaces`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains or changes retained retired-ID provenance for `NCBITaxon:1093141`.

## Additional Notes

- None.
