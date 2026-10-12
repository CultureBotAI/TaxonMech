# YAML Record Review

- Target: `data/taxa/eukaryota/penicilliopsis_zonata.yaml`
- Taxon: `NCBITaxon:41063` (`Penicilliopsis zonata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:41063`, label `Penicilliopsis zonata`.
- It is grounded exactly under `NCBITaxon:70110` (`Penicilliopsis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicilliopsis`.

## Validation

- `just validate data/taxa/eukaryota/penicilliopsis_zonata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/peltaster_fructicola.yaml data/taxa/eukaryota/penicilliopsis_zonata.yaml data/taxa/eukaryota/penicilliopsis_zonata_cbs_506_65.yaml data/taxa/eukaryota/penicillium_adametzioides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52465` contains the seeded identifier with reason `attested rule: Penicilliopsis zonata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4766` matches the YAML identity: parent `NCBITaxon:70110`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4766` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34719`, where `NCBITaxon:41063` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0009569`, two project rows, and no analysis rows for `NCBITaxon:41063`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found six culture-from-type-material spellings centered on `CBS 506.65`, `IMI 124936`, and `NRRL 5079`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:41063` record, `siID` 63714 with DOI `10.60712/SI-ID63714.3`, and 13 deposits.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:41063`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
