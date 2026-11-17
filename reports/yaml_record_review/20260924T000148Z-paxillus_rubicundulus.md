# YAML Record Review

- Target: `data/taxa/eukaryota/paxillus_rubicundulus.yaml`
- Taxon: `NCBITaxon:463315` (`Paxillus rubicundulus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:463315`, label `Paxillus rubicundulus`.
- It is grounded exactly under `NCBITaxon:5395` (`Paxillus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Paxillus`.

## Validation

- `just validate data/taxa/eukaryota/paxillus_rubicundulus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/paxillus_rubicundulus.yaml data/taxa/eukaryota/pecoramyces_ruminantium.yaml data/taxa/eukaryota/pedinellales_sp_ccmp2098.yaml data/taxa/eukaryota/pelagococcus_subviridis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55742` contains the seeded identifier with reason `attested rule: Paxillus rubicundulus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:103828` matches the YAML identity: parent `NCBITaxon:5395`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:103828` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36281`, where `NCBITaxon:463315` has `organism_count` 2.
- The native GOLD exact current-taxid scan found two organism rows, four project rows, and two analysis rows for `NCBITaxon:463315`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two holotype spellings centered on `K M190474` and three type-material spellings centered on `Orton 2905`.

## Completeness

- BacDive, exact StrainInfo side evidence, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:463315`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
