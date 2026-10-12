# YAML Record Review

- Target: `data/taxa/eukaryota/pelagomonas_calceolata.yaml`
- Taxon: `NCBITaxon:35677` (`Pelagomonas calceolata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:35677`, label `Pelagomonas calceolata`.
- It is grounded exactly under `NCBITaxon:35676` (`Pelagomonas`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Pelagomonas`.

## Validation

- `just validate data/taxa/eukaryota/pelagomonas_calceolata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pelagodinium_bei.yaml data/taxa/eukaryota/pelagomonas_calceolata.yaml data/taxa/eukaryota/pelagophyceae_sp_ccmp2097.yaml data/taxa/eukaryota/pelomyxa_schiedti.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52290` contains the seeded identifier with reason `attested rule: Pelagomonas calceolata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:3918` matches the YAML identity: parent `NCBITaxon:35676`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:3918` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33104`, where `NCBITaxon:35677` has `organism_count` 3.
- The native GOLD exact current-taxid scan found four organism rows, two project rows, and one analysis row for `NCBITaxon:35677`.
- Exact StrainInfo side evidence has 54 direct `NCBITaxon:35677` records and 59 deposits across those records.

## Completeness

- BacDive, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:35677`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
