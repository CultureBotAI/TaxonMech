# YAML Record Review

- Target: `data/taxa/eukaryota/pelagococcus_subviridis.yaml`
- Taxon: `NCBITaxon:35679` (`Pelagococcus subviridis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:35679`, label `Pelagococcus subviridis`.
- It is grounded exactly under `NCBITaxon:35678` (`Pelagococcus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Pelagococcus`.

## Validation

- `just validate data/taxa/eukaryota/pelagococcus_subviridis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paxillus_rubicundulus.yaml data/taxa/eukaryota/pecoramyces_ruminantium.yaml data/taxa/eukaryota/pedinellales_sp_ccmp2098.yaml data/taxa/eukaryota/pelagococcus_subviridis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52291` contains the seeded identifier with reason `attested rule: Pelagococcus subviridis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:3920` matches the YAML identity: parent `NCBITaxon:35678`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:3920` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33105`, where `NCBITaxon:35679` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0368783`, and no project or analysis rows for `NCBITaxon:35679`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:35679` record, `siID` 211729 with DOI `10.60712/SI-ID211729.2`, and two non-type deposits.

## Completeness

- BacDive, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:35679`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
