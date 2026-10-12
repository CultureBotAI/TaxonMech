# YAML Record Review

- Target: `data/taxa/eukaryota/paecilomyces_sp.yaml`
- Taxon: `NCBITaxon:40383` (`Paecilomyces sp.`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:40383`, label `Paecilomyces sp.`.
- It is grounded exactly under `NCBITaxon:2970110` (`unclassified Paecilomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `unclassified Paecilomyces`.

## Validation

- `just validate data/taxa/eukaryota/paecilomyces_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pachysolen_tannophilus.yaml data/taxa/eukaryota/paecilomyces_fulvus.yaml data/taxa/eukaryota/paecilomyces_sp.yaml data/taxa/eukaryota/paecilomyces_sp_m2901.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52428` contains the seeded identifier with reason `attested rule: Paecilomyces sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4590` matches the YAML identity: parent `NCBITaxon:2970110`, rank `SPECIES`, three exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4590` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34520`, where `NCBITaxon:40383` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:40383`.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:40383`; the record correctly has `strain_count: 0`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1880989` and `NCBITaxon:2046664` to `NCBITaxon:40383`, but no retained retired source row generated a YAML `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
