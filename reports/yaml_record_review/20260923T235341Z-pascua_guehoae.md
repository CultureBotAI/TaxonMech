# YAML Record Review

- Target: `data/taxa/eukaryota/pascua_guehoae.yaml`
- Taxon: `NCBITaxon:105714` (`Pascua guehoae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:105714`, label `Pascua guehoae`.
- It is grounded exactly under `NCBITaxon:2576016` (`Pascua`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Pascua`.

## Validation

- `just validate data/taxa/eukaryota/pascua_guehoae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/partenskyella_glossopodia.yaml data/taxa/eukaryota/parvodontia_relampaga.yaml data/taxa/eukaryota/pascua_guehoae.yaml data/taxa/eukaryota/paucimyces_polynucleatus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53699` contains the seeded identifier with reason `attested rule: Pascua guehoae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:18960` matches the YAML identity: parent `NCBITaxon:2576016`, rank `SPECIES`, two exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:18960` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1071`, where `NCBITaxon:105714` has `organism_count` 2.
- The native GOLD exact current-taxid scan found two organism rows, three project rows, and one analysis row for `NCBITaxon:105714`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-holotype spellings centered on `CBS 8521` for `NCBITaxon:105714`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:105714` record, `siID` 111544 with DOI `10.60712/SI-ID111544.2`, and two non-type deposits.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:105714`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
