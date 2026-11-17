# YAML Record Review

- Target: `data/taxa/eukaryota/pelomyxa_schiedti.yaml`
- Taxon: `NCBITaxon:1580589` (`Pelomyxa schiedti`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1580589`, label `Pelomyxa schiedti`.
- It is grounded exactly under `NCBITaxon:168131` (`Pelomyxa`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Pelomyxa`.

## Validation

- `just validate data/taxa/eukaryota/pelomyxa_schiedti.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pelagodinium_bei.yaml data/taxa/eukaryota/pelagomonas_calceolata.yaml data/taxa/eukaryota/pelagophyceae_sp_ccmp2097.yaml data/taxa/eukaryota/pelomyxa_schiedti.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60511` contains the seeded identifier with reason `attested rule: Pelomyxa schiedti, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:407553` matches the YAML identity: parent `NCBITaxon:168131`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:407553` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12746`, where `NCBITaxon:1580589` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0598289`, one project row, `Gp0616717`, and one analysis row for `NCBITaxon:1580589`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1580589`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
