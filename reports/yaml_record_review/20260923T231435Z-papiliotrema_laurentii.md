# YAML Record Review

- Target: `data/taxa/eukaryota/papiliotrema_laurentii.yaml`
- Taxon: `NCBITaxon:5418` (`Papiliotrema laurentii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5418`, label `Papiliotrema laurentii`.
- It is grounded exactly under `NCBITaxon:189450` (`Papiliotrema`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Papiliotrema`.

## Validation

- `just validate data/taxa/eukaryota/papiliotrema_laurentii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/panellus_stipticus.yaml data/taxa/eukaryota/panus_rudis.yaml data/taxa/eukaryota/papiliotrema_flavescens.yaml data/taxa/eukaryota/papiliotrema_laurentii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51989` contains the seeded identifier with reason `attested rule: Papiliotrema laurentii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2404` matches the YAML identity: parent `NCBITaxon:189450`, rank `SPECIES`, four exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2404` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38316`, where `NCBITaxon:5418` has `organism_count` 10.
- The native GOLD exact current-taxid scan found 10 organism rows, three project rows, and one analysis row for `NCBITaxon:5418`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 25 type-material spellings for `NCBITaxon:5418` on lines 231609-231633, all under `Torula laurentii`.
- Exact StrainInfo side evidence has 86 direct `NCBITaxon:5418` records and 146 deposits across those records.

## Completeness

- Exact BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:5418`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
